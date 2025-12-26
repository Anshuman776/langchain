import os
from urllib.parse import quote_plus
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate

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
        model="gpt-3.5-turbo",
        temperature=0.1,
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )

    # ---------- OPENAI EMBEDDINGS ----------
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )

    # Example texts for semantic understanding (optional but useful)
    texts = [
        "How many Nike t-shirts are left",
        "Total stock of Levi t-shirts",
        "Which brand has the most t-shirts",
        "List t-shirts with discount",
    ]

    vectorstore = Chroma.from_texts(
        texts=texts,
        embedding=embeddings
    )

    # ---------- PROMPT ----------
    mysql_prompt = """
You are a MySQL expert.

Generate a valid MySQL query, execute it, and return the answer.

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
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"]
    )


    chain = SQLDatabaseChain.from_llm(
        llm=llm,
        db=db,
        prompt=prompt,
        verbose=True
    )

    return chain




