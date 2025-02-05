import streamlit as st
import requests

FASTAPI_URL = "http://127.0.0.1:8000/query/"

st.set_page_config(page_title="Company Chatbot", layout="centered")

st.title("💬 Company Chatbot")
st.markdown("Ask questions about the company, and the AI will answer using company documents.")

question = st.text_input("Enter your question:")

if st.button("Get Answer") and question.strip():
    with st.spinner("Retrieving information..."):
        try:
            response = requests.get(FASTAPI_URL, params={"question": question})
            
            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                st.success("✅ Answer Retrieved:")
                st.write(answer)
            else:
                st.error(f"⚠️ Error {response.status_code}: {response.text}")
        
        except requests.exceptions.RequestException as e:
            st.error(f"❌ Connection Error: {e}")

st.markdown("---")
