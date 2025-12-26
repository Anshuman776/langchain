import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI


from langchain_community.utilities import SQLDatabase
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_experimental.sql import SQLDatabaseChain

from langchain_community.vectorstores import Chroma

from langchain_core.prompts import (
    FewShotPromptTemplate,
    PromptTemplate
)
from langchain_core.example_selectors import SemanticSimilarityExampleSelector

from langchain_experimental.sql.prompt import PROMPT_SUFFIX


from few_shots import few_shots

load_dotenv()


@st.cache_resource
def get_few_shot_db_chain():
    # ---------- DATABASE ----------
    db_user = os.environ["DB_USER"]
    db_password = quote_plus(os.environ["DB_PASSWORD"])
    db_host = os.environ["DB_HOST"]
    db_name = os.environ["DB_NAME"]

    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{os.environ['DB_PORT']}/{db_name}",
        sample_rows_in_table_info=3
    )

    # ---------- LLM ----------
    
    llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.1
)


    # ---------- EMBEDDINGS ----------
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
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
        prompt=few_shot_prompt,
        verbose=True
    )

    return chain

