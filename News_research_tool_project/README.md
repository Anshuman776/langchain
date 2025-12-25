📰 News Research Tool (RAG Application)

🔗 Live App:
https://newsresearchtoolproject-mhpp2obhmmxfhuhn5qsj9a.streamlit.app/

📌 Overview<img width="1920" height="1080" alt="Screenshot 2025-12-25 171223" src="https://github.com/user-attachments/assets/6040da8d-1863-4b95-a155-96b8daebe9eb" />


RockyBot is a Retrieval-Augmented Generation (RAG) application that allows users to:

Input news article URLs

Automatically extract and process article content

Ask questions strictly based on those articles

Receive grounded answers with sources

Unlike a normal chatbot, RockyBot does not hallucinate or answer from general knowledge.
If the information is not present in the articles, it clearly says so.

🧠 What is RAG?

RAG (Retrieval-Augmented Generation) combines:

Retrieval – Fetch relevant information from your own data

Generation – Use an LLM to generate answers based only on that data

This makes the system:

Safer

More accurate

Suitable for research and analysis

🔍 How RockyBot Works

URL Ingestion
News article URLs are loaded using UnstructuredURLLoader.

Text Chunking
Articles are split into smaller chunks using RecursiveCharacterTextSplitter.

Embedding Generation
Each chunk is converted into vector embeddings using OpenAI embeddings.

Vector Storage (FAISS)
Embeddings are stored in a FAISS vector index for fast similarity search.

Retrieval
When a user asks a question, the most relevant chunks are retrieved.

Answer Generation
The LLM generates an answer only using the retrieved context.

Source Display
The app shows which articles were used to generate the answer.

✨ Key Features

✅ Context-grounded answers (no hallucination)

✅ Source citations

✅ Modern LangChain (LCEL / Runnable pipeline)

✅ FAISS vector search

✅ Streamlit UI

✅ Cloud-deployed

🚫 Why Pickle Is NOT Used

Earlier versions of LangChain used pickle to store vector databases.
This project does not use pickle because:

FAISS objects contain thread locks and C++ components

Pickle cannot safely serialize these objects

It leads to runtime errors

Instead, FAISS is stored using:

vectorstore.save_local("faiss_index")
FAISS.load_local("faiss_index", embeddings)


This is the official and safe approach.

🧪 Tech Stack

Python 3.11

Streamlit

LangChain 1.x

OpenAI API

FAISS

Unstructured

🛠️ Installation (Local Setup)
1️⃣ Clone the repository
git clone https://github.com/your-username/rockybot-news-research-tool.git
cd rockybot-news-research-tool

2️⃣ Create a virtual environment
conda create -n langchain311 python=3.11
conda activate langchain311

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here

5️⃣ Run the app
streamlit run main.py

📖 How to Use

Open the app

Enter up to 3 news article URLs

Click Process URLs

Ask a question related to the articles

View the answer and sources

🧠 Example Questions

“What is the main topic of these articles?”

“Summarize the key developments.”

“What are the risks mentioned?”

📌 Important Note

If you ask a question that is not answered in the articles, the app will respond with:

“I don’t know based on the provided context.”

This is intentional and ensures factual accuracy.

🚀 Future Improvements

Streaming responses

Multi-article comparison

Citation numbering

Hybrid search (BM25 + vectors)

Document preview UI

👨‍💻 Author

Built by Anshuman Maurya
Learning and experimenting with RAG, LangChain, and LLM applications

📜 License

MIT License
