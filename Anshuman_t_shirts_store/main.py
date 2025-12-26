import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_helper import get_few_shot_db_chain

st.title("Anshuman T-Shirts Store 👕")

question = st.text_input("Ask a question about the database")

if question:
    # 1️⃣ Run SQLDatabaseChain (this may return SQL)
    chain = get_few_shot_db_chain()
    raw_result = chain.invoke({"input": question})["result"]

    # 2️⃣ Use LLM AGAIN to explain the result in English
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.1,
        openai_api_key=os.environ["OPENAI_API_KEY"]
    )

    explanation_prompt = f"""
User question:
{question}

Database output:
{raw_result}

Explain the result clearly in plain English.
Do NOT show SQL.
"""

    final_answer = llm.invoke(explanation_prompt).content

    # 3️⃣ Show final answer
    st.subheader("Answer")
    st.write(final_answer)



