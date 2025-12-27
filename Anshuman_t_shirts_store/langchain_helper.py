import os
from urllib.parse import quote_plus
from dotenv import load_dotenv


from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.vectorstores import Chroma

from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector

from few_shots import few_shots

load_dotenv()


def get_few_shot_db_chain():
    # ---------- DATABASE ----------
    db_user = os.environ["DB_USER"]
    db_password = quote_plus(os.environ["DB_PASSWORD"])
    db_host = os.environ["DB_HOST"]
    db_port = os.environ["DB_PORT"]
    db_name = os.environ["DB_NAME"]

    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}",
        sample_rows_in_table_info=3
    )

    # ---------- LLM ----------
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.1,
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )

    # ---------- EMBEDDINGS ----------
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )

    texts = [" ".join(example.values()) for example in few_shots]

    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        metadatas=few_shots
    )

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2
    )

    # ---------- PROMPT ----------
    mysql_prompt = """
You are a MySQL expert.

Generate a valid SQL query, execute it, and answer in plain English.

Format:
Question:
SQLQuery:
SQLResult:
Answer:
"""

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="""
Question: {Question}
SQLQuery: {SQLQuery}
SQLResult: {SQLResult}
Answer: {Answer}
"""
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix="""
Question: {input}
Tables:
{table_info}

SQLQuery:
""",
        input_variables=["input", "table_info"]
    )

    chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        prompt=few_shot_prompt,
        verbose=True,
        return_direct=True
    )

    return chain







