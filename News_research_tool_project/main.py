import os
import time
import streamlit as st


from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser



# ---------------------------------------------------
# STREAMLIT UI
# ---------------------------------------------------
st.set_page_config(page_title="Bot", layout="wide")
st.title("📰 News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    if url:
        urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

INDEX_DIR = "faiss_index"

# ---------------------------------------------------
# LLM
# ---------------------------------------------------
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    max_tokens=500
)

# ---------------------------------------------------
# PROCESS URLS
# ---------------------------------------------------
if process_url_clicked:
    if not urls:
        st.warning("Please enter at least one URL.")
    else:
        try:
            st.info("🔄 Loading data from URLs...")
            loader = UnstructuredURLLoader(urls=urls)
            data = loader.load()

            st.info("✂️ Splitting documents...")
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            docs = splitter.split_documents(data)

            st.info("🧠 Creating embeddings & FAISS index...")
            embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
            vectorstore = FAISS.from_documents(docs, embeddings)

            # ✅ SAFE SAVE (NO PICKLE)
            vectorstore.save_local(INDEX_DIR)

            time.sleep(1)
            st.success("✅ FAISS index created and saved successfully!")

        except Exception as e:
            st.error(f"❌ Error processing URLs: {e}")

# ---------------------------------------------------
# QUESTION ANSWERING
# ---------------------------------------------------
query = st.text_input("Ask a question based on the articles:")

if query:
    if not os.path.exists(INDEX_DIR):
        st.warning("Please process URLs first.")
    else:
        # Load FAISS safely
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        vectorstore = FAISS.load_local(
            INDEX_DIR,
            embeddings,
            allow_dangerous_deserialization=True
        )

        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        prompt = ChatPromptTemplate.from_template(
            """
            Use the context below to answer the question.
            If the answer is not in the context, say you don't know.

            Context:
            {context}

            Question:
            {question}
            """
        )

        chain = (
            {
                "context": retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        answer = chain.invoke(query)

        st.header("Answer")
        st.write(answer)

        # -------------------------------
        # SOURCES
        # -------------------------------
        docs = retriever.invoke(query)

        sources = {doc.metadata.get("source", "Unknown") for doc in docs}

        if sources:
            st.subheader("Sources")
            for src in sources:
                st.write(src)


