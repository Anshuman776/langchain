import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_helper import get_few_shot_db_chain

st.title("Anshuman T-Shirts Store 👕")

question = st.text_input("Ask a question about the database")

if question:
    chain = get_few_shot_db_chain()

   
    raw_result = chain.run(question)

    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
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

    final_answer = llm.predict(explanation_prompt)

    st.subheader("Answer")
    st.write(final_answer)
)





