![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)
![Database](https://img.shields.io/badge/Database-MySQL-blue)

# 👕 Anshuman T-Shirts Store (AI-Powered SQL Q&A)

🔗 **Live App:**  
https://langchain-tsygppei8hykpdiaq9so9r.streamlit.app/

---

## 📌 Overview

<img width="1920" height="1080" alt="Screenshot 2025-12-27 150012" src="https://github.com/user-attachments/assets/961db1d6-96a0-459a-95d3-ef6e8aa9ffe1" />

**Anshuman T-Shirts Store** is an **AI-powered SQL Question Answering application** that allows users to:

- Ask natural-language questions about a T-shirts inventory  
- Automatically generate SQL queries  
- Execute queries on a live MySQL database  
- Receive **accurate, database-grounded answers**


Unlike a normal chatbot, this application **does NOT hallucinate**.  
All answers are strictly derived from the **actual SQL database**.

---

## 🧠 What is SQL-RAG?

**SQL-RAG (SQL-based Retrieval-Augmented Generation)** combines:

- **Retrieval** – Fetch information from a structured SQL database  
- **Generation** – Use an LLM to generate SQL and interpret results  

This makes the system:

- Accurate  
- Deterministic  
- Suitable for analytics and reporting  

---

## 🔍 How the Application Works

1. **User Question Input**  
   Users ask questions such as:
   - *How many Nike t-shirts are left?*
   - *Total stock of Levi t-shirts*
   - *Which brand has the most inventory?*

2. **SQL Generation**  
   LangChain converts the natural-language question into a valid MySQL query.

3. **Database Execution**  
   The query is executed against a **live MySQL database hosted on Railway**.

4. **Result Extraction**  
   Raw SQL output (e.g. `[(Decimal('98'),)]`) is safely cleaned.

5. **Answer Display**  
   The final answer is displayed to the user via Streamlit.

---

## ✨ Key Features

- Natural language → SQL conversion  
- Live database querying  
- No hallucination (DB-grounded answers only)  
- OpenAI GPT-3.5 integration  
- MySQL (Railway-hosted)  
- Streamlit UI  
- Cloud deployment  

---

## 🚫 Why Vector RAG Is NOT Used

This project does **not use FAISS or document embeddings** because:

- Data is structured (tables and columns)
- SQL queries are deterministic
- Vector search is unnecessary for relational data

Instead, the application uses **LangChain’s SQLDatabaseChain**, which is the correct tool for structured databases.

---

## 🧪 Tech Stack

- Python 3.10  
- Streamlit  
- LangChain (SQLDatabaseChain)  
- OpenAI API  
- MySQL  
- Railway  
- PyMySQL  

---

## 🛠️ Installation (Local Setup)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Anshuman776/langchain.git
cd langchain/Anshuman_t_shirts_store
```

### 2️⃣ Create a virtual environment
```bash
conda create -n tshirts python=3.10
conda activate tshirts
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables

Create a .env file:
```bash

OPENAI_API_KEY=your_openai_api_key

DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=your_railway_host
DB_PORT=your_railway_port
DB_NAME=railway
```

Ensure the following exists in code:

from dotenv import load_dotenv
load_dotenv()

### 🛢️ Connecting MySQL Using Railway

The MySQL database is hosted on Railway.

Connection format used:
```bash
mysql://USER:PASSWORD@HOST:PORT/DATABASE


LangChain connects using:

SQLDatabase.from_uri(
    f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
)
```

This setup works both locally and on Streamlit Cloud.

### 📖 How to Use

Open the app

Ask a question about the inventory

View the result instantly

### 🧠 Example Questions

“How many Nike t-shirts are left?”

“Total stock of Levi t-shirts”

“Which brand has the most inventory?”

### 📌 Important Note

If a question does not match the database schema or available data, the app will respond with:

“No data found.”

This ensures accuracy and prevents hallucination.

### 🚀 Future Improvements

Size and color filters

Inventory charts

Query history

Role-based access

Natural language summaries

### 👨‍💻 Author

Built by Anshuman Maurya

Learning and experimenting with SQL-RAG, LangChain, and Streamlit.

## 📜 License

This project is licensed under the **MIT License**.
