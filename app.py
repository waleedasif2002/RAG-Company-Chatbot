import uvicorn
import pinecone
import openai
import numpy as np
import os
from fastapi import FastAPI, HTTPException
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INDEX_NAME = "company-docs-index"

pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)

existing_indexes = [index.name for index in pc.list_indexes()]
if INDEX_NAME not in existing_indexes:
    raise ValueError(f"Pinecone index '{INDEX_NAME}' does not exist. Please create it first.")

index = pc.Index(INDEX_NAME)

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def query_pinecone(question, top_k=3, threshold=0.3):
    query_embedding = model.encode(question, convert_to_numpy=True).astype(np.float32).tolist()
    results = index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
    
    relevant_responses = [match["metadata"]["text"] for match in results["matches"] if match["score"] >= threshold]
    
    return relevant_responses if relevant_responses else ["This information is not available in the given source."]

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(query, context):
    prompt = f"Use the following information to answer the query:\n\n{context}\n\nQuery: {query}\nAnswer:"
    
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant that provides company-related answers based on provided documents."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    
    return response.choices[0].message.content

@app.get("/query/")
def get_answer(question: str):
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    retrieved_texts = query_pinecone(question, top_k=5)
    final_response = generate_answer(question, retrieved_texts)
    
    return {"question": question, "answer": final_response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)  
