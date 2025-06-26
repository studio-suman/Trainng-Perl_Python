#pip install openai-whisper sentence-transformers scikit-learn transformers moviepy
import os
import subprocess
import numpy as np
# Removed unused import
import whisper
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
# Removed unused import
 
# Step 1: Transcribe the video using Whisper
def transcribe_video(video_path):
    model = whisper.load_model("base") # type: ignore
    result = model.transcribe(video_path)
    return result['segments']  # List of segments with 'start', 'end', 'text'
 
# Step 2: Embed the transcript using sentence embeddings
def embed_segments(segments):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    texts = [seg['text'] for seg in segments]
    embeddings = model.encode(texts)
    return embeddings
 
# Step 3: Apply semantic chunking based on similarity
def semantic_chunking(segments, embeddings, threshold=0.75):
    chunks = []
    current_chunk = [segments[0]]
    for i in range(1, len(segments)):
        sim = cosine_similarity(np.array([embeddings[i]]), np.array([embeddings[i-1]]))[0][0]
        if sim > threshold:
            current_chunk.append(segments[i])
        else:
            chunks.append(current_chunk)
            current_chunk = [segments[i]]
    if current_chunk:
        chunks.append(current_chunk)
    return chunks
 
# Step 4: Summarize each chunk using an LLM
def summarize_chunks(chunks):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summaries = []
    for chunk in chunks:
        text = " ".join([seg['text'] for seg in chunk])
        summary = summarizer(text, max_length=60, min_length=10, do_sample=False)
        if isinstance(summary, list) and len(summary) > 0 and 'summary_text' in summary[0]:
            summaries.append(summary[0]['summary_text'])
        else:
            summaries.append("Error: Unable to summarize chunk.")
        summaries.append(summary)
    return summaries
 
# Step 5: Extract video segments using FFmpeg
def extract_video_segments(video_path, chunks, output_dir="video_chunks"):
    os.makedirs(output_dir, exist_ok=True)
    for i, chunk in enumerate(chunks):
        start = chunk[0]['start']
        end = chunk[-1]['end']
        output_file = os.path.join(output_dir, f"chunk_{i+1}.mp4")
        subprocess.run([
            "ffmpeg", "-y", "-i", video_path,
            "-ss", str(start), "-to", str(end),
            "-c", "copy", output_file
        ])
    return output_dir
 
# Example usage
video_file = r"D:\OneDrive - Wipro\Desktop\Trainng-Perl_Python\Python_Codes\LLM_USE Cases\SemanticVideo\EF-connect-Recording.mp4"  # Replace with your video file path
segments = transcribe_video(video_file)
#embeddings = embed_segments(segments)
#chunks = semantic_chunking(segments, embeddings)
#summaries = summarize_chunks(chunks)
#output_folder = extract_video_segments(video_file, chunks)
 
# Print summaries
# for i, summary in enumerate(summaries):
#     print(f"Chunk {i+1} Summary: {summary}")