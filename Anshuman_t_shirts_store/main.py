import os
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain_helper import get_few_shot_db_chain

st.title("Anshuman T-Shirts Store 👕")

question = st.text_input("Ask a question about the database")

if question:
    chain = get_few_shot_db_chain()

    # Run SQL query
    raw_result = chain.run(question)

    st.subheader("Answer")

    # SAFE result handling
    if isinstance(raw_result, list) and len(raw_result) > 0:
        value = raw_result[0][0]
        if value is None:
            st.write(0)
        else:
            st.write(int(value))
    else:
        st.write(0)
