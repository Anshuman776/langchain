import streamlit as st
import re
from langchain_helper import get_few_shot_db_chain

st.title("Anshuman T-Shirts Store 👕")

question = st.text_input("Ask a question about the database")

if question:
    chain = get_few_shot_db_chain()
    result = chain.run(question)

    # 🔥 FINAL SAFE CLEANING
    if isinstance(result, list) and len(result) > 0:
        if isinstance(result[0], tuple):
            result = result[0][0]
        else:
            result = result[0]

    # Convert result to number safely
    result_str = str(result)
    numbers = re.findall(r"\d+", result_str)

    st.subheader("Answer")
    if numbers:
        st.write(numbers[0])
    else:
        st.write("0")
