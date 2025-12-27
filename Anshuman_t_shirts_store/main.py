import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("Anshuman T-Shirts Store 👕")

question = st.text_input("Ask a question about the database")

if question:
    chain = get_few_shot_db_chain()
    result = chain.run(question)

    # ✅ SAFE extraction
    if isinstance(result, list) and len(result) > 0:
        if isinstance(result[0], tuple):
            result = result[0][0]
        else:
            result = result[0]

    st.subheader("Answer")
    st.write(int(result))
