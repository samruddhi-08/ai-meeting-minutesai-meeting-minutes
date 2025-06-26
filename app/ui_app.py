import streamlit as st
import os

from transcribe import transcribe_audio, get_youtube_transcript
from chunking import chunk_transcript
from embedding import create_faiss_index, load_faiss_index
from summarizer import generate_meeting_summary
from qa_rag import load_qa_pipeline, answer_question

st.set_page_config(page_title="AI Meeting Minutes Generator", layout="wide")
st.title("🤖 AI Meeting Minutes Generator & Action Tracker")

# Sidebar upload
st.sidebar.header("📤 Upload or Paste Meeting")
uploaded_file = st.sidebar.file_uploader("Upload Audio/Video (.mp3/.mp4) or Transcript (.txt)", type=["mp3", "mp4", "txt"])
youtube_url = st.sidebar.text_input("Or enter YouTube video URL")

if uploaded_file:
    file_path = f"data/uploads/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if file_path.endswith(".txt"):
        transcript_text = uploaded_file.read().decode("utf-8")
    else:
        transcript_text = transcribe_audio(file_path)

elif youtube_url:
    transcript_text = get_youtube_transcript(youtube_url)

else:
    st.info("Please upload a file or enter a YouTube URL.")
    st.stop()

# Show transcript preview
with st.expander("📝 Transcript Preview"):
    st.write(transcript_text[:3000])

# Summarize & Extract
if st.button("🧠 Generate Summary & Action Points"):
    st.info("Chunking transcript...")
    chunks = chunk_transcript(transcript_text)

    st.info("Creating FAISS vector index...")
    create_faiss_index(chunks)

    st.success("✅ Summary ready:")
    summary = generate_meeting_summary(transcript_text)
    st.markdown(summary)

# RAG-based Q&A
st.subheader("❓ Ask a Question about the Meeting")
query = st.text_input("What would you like to know?")
if query:
    qa_pipeline = load_qa_pipeline()
    answer = answer_question(qa_pipeline, query)
    st.markdown(f"**Answer:** {answer}")
