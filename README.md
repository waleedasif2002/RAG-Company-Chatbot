# 🧠 RAG-Based Company Chatbot 🚀

This project is a **Retrieval-Augmented Generation (RAG) chatbot** that answers company-related queries using **FastAPI, Pinecone, OpenAI, and Streamlit**.

---

## 🔥 Features
✅ **Retrieves relevant company documents using Pinecone**  
✅ **Generates intelligent responses using OpenAI GPT-4 Turbo**  
✅ **Deploys a FastAPI backend for querying**  
✅ **User-friendly Streamlit frontend**  

---

## ⚙️ Project Structure
```
📂 RAG-Company-Chatbot
│── 📄 app.py             # FastAPI backend for query processing
│── 📄 main.py            # Streamlit frontend for user interaction
│── 📄 Data.docx          # Company document data
│── 📄 RAG_Week2.ipynb    # Jupyter Notebook for development
│── 📄 README.md          # Project documentation
│── 📄 .gitignore         # Prevents sensitive files from being pushed
```

---

## 🚀 Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/RAG-Company-Chatbot.git
cd RAG-Company-Chatbot
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
---

## **⚙️ Configuration**
### **3️⃣ Set Up API Keys**
1. **Create a `.env` file** in the project root and add:
```
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```

2. **Ensure your `.env` file is listed in `.gitignore`** to prevent pushing secrets.

---

## **🔧 Running the Application**
### **4️⃣ Run FastAPI Backend**
```bash
python app.py
```
FastAPI will be available at 👉 **`http://127.0.0.1:8080/docs`**.

### **5️⃣ Run Streamlit Frontend**
```bash
streamlit run main.py
```
Access the UI at 👉 **`http://localhost:8501/`**.

---

## **🛠 Troubleshooting**
- **Port Already in Use?**  
  - Change the port in `app.py`:
    ```python
    uvicorn.run(app, host="0.0.0.0", port=8081)
    ```
- **Pinecone Index Not Found?**  
  - Ensure you **created the index** before running the app.
---

## **🔗 Connect with Me**
📩 **GitHub:** [Your GitHub Profile](https://github.com/waleedasif2002)  
