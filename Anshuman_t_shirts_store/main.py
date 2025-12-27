import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_helper import get_db_chain

st.set_page_config(page_title="Anshuman T-Shirts Store", page_icon="👕")

st.title("Anshuman T-Shirts Store 👕")

question = st.text_input("Ask a question about the database")

if question:
    chain = get_db_chain()

    # IMPORTANT: use run() (old LangChain)
    result = chain.run(question)

    # Clean SQL output
    if isinstance(result, list):
        result = result[0][0]

    st.subheader("Answer")
    st.write(result)
