from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_transcript(transcript_text: str, chunk_size=500, chunk_overlap=100):
    """
    Splits a long transcript into overlapping chunks for RAG.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_text(transcript_text)


# Example usage for testing
if __name__ == "__main__":
    with open("data/uploads/sample_transcript.txt", "r", encoding="utf-8") as f:
        text = f.read()
    chunks = chunk_transcript(text)

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i + 1} ---\n{chunk}")
