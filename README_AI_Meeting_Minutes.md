
# 🤖 AI Meeting Minutes Generator & Action Tracker

Automatically transcribe, summarize, and extract action items from meeting audio, video, or transcripts using GPT-4, Whisper, and LangChain.

---

## 🚀 Demo

Upload an `.mp3`, `.mp4`, or `.txt` transcript and get:
- 🧠 GPT-4-generated summary
- 📌 Action items, decisions, and open points
- ❓ Ask context-aware questions using RAG
- 📤 Downloadable output (PDF export coming soon)

---

## 🛠️ Tech Stack

| Tool          | Purpose                              |
|---------------|--------------------------------------|
| Python        | Backend logic                        |
| Streamlit     | Frontend UI                          |
| OpenAI GPT-4  | Summarization & Q&A                  |
| Whisper       | Speech-to-text transcription         |
| LangChain     | RAG pipeline + prompt orchestration  |
| FAISS         | Vector DB for semantic retrieval     |
| PyMuPDF       | (Optional) PDF output generation     |
| Docker        | Containerized deployment             |

---

## 📦 Features

- 🎙️ **Upload audio/video/text** meeting files
- 🔊 **Transcribe with Whisper** (offline support)
- 🧠 **Summarize** meetings with GPT-4:
  - TL;DR
  - Action Items (Who, What, By When)
  - Decisions
  - Unresolved Questions
- 🔍 **Ask custom questions** (RAG search)
- 📄 View all results in a simple **Streamlit dashboard**
- 💡 Built for real-world use in **corporate/business meetings**

---

## 💻 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/samruddhi-08/ai-meeting-minutes.git
cd ai-meeting-minutes
```

### 2. Create and activate virtual environment (Python 3.10+)

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install requirements

```bash
pip install -r requirements.txt
pip install git+https://github.com/openai/whisper.git
pip install -U langchain-community
```

### 4. Set OpenAI API key

Create a `.env` file in the root:

```
OPENAI_API_KEY=your-api-key-here
```

Or set in terminal:

```bash
$env:OPENAI_API_KEY="your-api-key-here"
```

### 5. Add FFmpeg (for Whisper)

- Download FFmpeg: https://www.gyan.dev/ffmpeg/builds/
- Extract to: `C:\ffmpeg\bin`
- Add `C:\ffmpeg\bin` to your system `PATH`
- Restart your terminal
- Test with: `ffmpeg -version`

---

## 🧪 Run the App

```bash
streamlit run app/ui_app.py
```

Open your browser to [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```
ai-meeting-minutes/
│
├── app/
│   ├── ui_app.py            # Streamlit frontend
│   ├── transcribe.py        # Whisper transcription
│   ├── summarizer.py        # GPT-4 summarizer
│   ├── chunking.py          # Text chunk splitter
│   ├── embedding.py         # FAISS vector DB creation
│   ├── qa_rag.py            # RAG-based Q&A
├── data/
│   └── uploads/             # Audio/video/text files
├── models/
│   └── faiss_index/         # Stored FAISS vector DB
├── .env                     # API keys
├── requirements.txt
├── README.md
```
