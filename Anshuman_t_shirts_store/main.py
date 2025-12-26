import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Anshuman T-Shirts Store 👕")

question = st.text_input("Ask a question about the database:")

if question:
    chain = get_few_shot_db_chain()
    response = chain.run(question)

    st.subheader("Answer")
    st.write(response)
