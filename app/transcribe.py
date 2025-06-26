import whisper
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube

# Load Whisper model (base is fast and accurate for most uses)
model = whisper.load_model("base")

def transcribe_audio(file_path: str) -> str:
    """
    Transcribes audio or video file using Whisper.
    Supports .mp3, .mp4, .wav, etc.
    """
    print(f"Transcribing: {file_path}")
    result = model.transcribe(file_path)
    return result["text"]

def get_youtube_transcript(video_url: str) -> str:
    """
    Fetch transcript from a YouTube video using its ID.
    Only works if the video has captions enabled.
    """
    try:
        video_id = video_url.split("v=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item["text"] for item in transcript])
    except Exception as e:
        return f"Failed to fetch transcript: {str(e)}"
