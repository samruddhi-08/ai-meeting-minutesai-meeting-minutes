from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings


def load_qa_pipeline(index_path="models/faiss_index"):
    """
    Load FAISS vector store and create a RetrievalQA pipeline using GPT-4.
    """
    print(f"📥 Loading FAISS index from: {index_path}")
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.load_local(index_path, embeddings)

    llm = ChatOpenAI(model="gpt-4", temperature=0.2)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(),
        return_source_documents=True
    )
    return qa

def answer_question(qa_pipeline, question: str):
    """
    Ask a question and get an answer based on transcript chunks in FAISS.
    """
    print(f"❓ Q: {question}")
    result = qa_pipeline({"query": question})
    return result["result"]
