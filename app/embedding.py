import os
import faiss
import pickle
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def create_faiss_index(chunks: list, save_path: str = "models/faiss_index"):
    """
    Embeds transcript chunks and saves FAISS index locally.
    """
    print("🔄 Generating embeddings...")
    embeddings = OpenAIEmbeddings()  # Uses OPENAI_API_KEY from env
    vector_store = FAISS.from_texts(chunks, embedding=embeddings)

    # Save index and metadata
    vector_store.save_local(save_path)
    print(f"✅ FAISS index saved to: {save_path}")

    return vector_store


def load_faiss_index(load_path: str = "models/faiss_index"):
    """
    Loads previously saved FAISS vector store.
    """
    print(f"📂 Loading FAISS index from: {load_path}")
    return FAISS.load_local(
        load_path,
        OpenAIEmbeddings(),
        allow_dangerous_deserialization=True  # ✅ ADD THIS LINE
    )