![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)

# 📰 News Research Tool (RAG Application)

🔗 **Live App:**  
https://newsresearchtoolproject-mhpp2obhmmxfhuhn5qsj9a.streamlit.app/

---

## 📌 Overview

<img width="100%" alt="Application Screenshot" src="https://github.com/user-attachments/assets/6040da8d-1863-4b95-a155-96b8daebe9eb" />

**News Research Tool** is a **Retrieval-Augmented Generation (RAG)** application that allows users to:

- Input news article URLs  
- Automatically extract and process article content  
- Ask questions **strictly based on those articles**  
- Receive **grounded answers with sources**

Unlike a normal chatbot, this application **does not hallucinate** or answer from general knowledge.  
If the information is not present in the articles, it clearly says so.

---

## 🧠 What is RAG?

**RAG (Retrieval-Augmented Generation)** combines:

- **Retrieval** – Fetch relevant information from your own data  
- **Generation** – Use an LLM to generate answers based only on that data  

This makes the system:

- Safer  
- More accurate  
- Suitable for research and analysis  

---

## 🔍 How the Application Works

1. **URL Ingestion**  
   News article URLs are loaded using `UnstructuredURLLoader`.

2. **Text Chunking**  
   Articles are split into smaller chunks using `RecursiveCharacterTextSplitter`.

3. **Embedding Generation**  
   Each chunk is converted into vector embeddings using OpenAI embeddings.

4. **Vector Storage (FAISS)**  
   Embeddings are stored in a FAISS vector index for fast similarity search.

5. **Retrieval**  
   When a user asks a question, the most relevant chunks are retrieved.

6. **Answer Generation**  
   The LLM generates an answer **only using the retrieved context**.

7. **Source Display**  
   The app shows which articles were used to generate the answer.

---

## ✨ Key Features

- Context-grounded answers (no hallucination)  
- Source citations  
- Modern LangChain (LCEL / Runnable pipeline)  
- FAISS vector search  
- Streamlit UI  
- Cloud deployment  

---

## 🚫 Why Pickle Is NOT Used

Earlier versions of LangChain used `pickle` to store vector databases.  
This project **does not use pickle** because:

- FAISS objects contain thread locks and C++ components  
- Pickle cannot safely serialize these objects  
- It leads to runtime errors  

Instead, FAISS is stored using the official and safe approach:

```python
vectorstore.save_local("faiss_index")
FAISS.load_local("faiss_index", embeddings)
 ```


## 🧪 Tech Stack

- Python 3.11  
- Streamlit  
- LangChain 1.x  
- OpenAI API  
- FAISS  
- Unstructured  

---

## 🛠️ Installation (Local Setup)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Anshuman776/langchain.git
cd langchain/News_research_tool_project
````

### 2️⃣ Create a virtual environment
```bash
conda create -n langchain311 python=3.11
conda activate langchain311
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables
Create a .env file
```bash
OPENAI_API_KEY=your_api_key_here
```
Ensure the following exists in main.py:
```bash
from dotenv import load_dotenv
load_dotenv()
```

### 5️⃣ Run the app
```bash
streamlit run main.py
```

### 📖 How to Use

1. Open the app

2. Enter up to 3 news article URLs, for example:

https://www.moneycontrol.com/news/business/stocks/buy-tata-motors-target-of-rs-743-kr-     choksey-11080811.html

https://www.moneycontrol.com/news/business/tata-motors-launches-punch-icng-price-starts-at-rs-7-1-lakh-11098751.html

https://www.moneycontrol.com/news/business/tata-motors-mahindra-gain-certificates-for-production-linked-payouts-11281691.html

3. Ask a question related to the articles

4. View the answer and sources

### 🧠 Example Questions

“What is the price of Tata Punch”

“Summarize the key developments.”

“What are the risks mentioned?”

### 📌 Important Note

If you ask a question that is not answered in the articles, the app will respond with:

“I don’t know based on the provided context.”

This is intentional and ensures factual accuracy.

### 🚀 Future Improvements

Streaming responses

Multi-article comparison

Citation numbering

Hybrid search (BM25 + vectors)

Document preview UI

### 👨‍💻 Author

Built by Anshuman Maurya

Learning and experimenting with RAG, LangChain, and LLM applications

## 📜 License

This project is licensed under the **MIT License**.

