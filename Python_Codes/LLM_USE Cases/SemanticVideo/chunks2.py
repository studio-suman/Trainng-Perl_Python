import os
import subprocess
import numpy as np
import whisper
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline
from multiprocessing import Pool, cpu_count

os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"
subprocess.run(["ffmpeg", "-version"])

# Step 1: Transcribe the video using Whisper
def transcribe_video(video_path):
    model = whisper.load_model("base")  # type: ignore
    result = model.transcribe(video_path)
    return result['segments']  # List of segments with 'start', 'end', 'text'

# Step 2: Embed the transcript using sentence embeddings with multiprocessing
def embed_text(text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(text)

def embed_segments_parallel(segments):
    texts = [seg['text'] for seg in segments]
    try:
        with Pool(processes=cpu_count()) as pool:
            embeddings = pool.map(embed_text, texts)
    except Exception as e:
        print(f"Multiprocessing failed for embedding: {e}")
        model = SentenceTransformer('all-MiniLM-L6-v2')
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

# Step 4: Summarize each chunk using an LLM with multiprocessing
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=60, min_length=10, do_sample=False)
    if isinstance(summary, list) and len(summary) > 0 and 'summary_text' in summary[0]:
        return summary[0]['summary_text']
    else:
        return "Error: Unable to summarize chunk."

def summarize_chunks_parallel(chunks):
    texts = [" ".join([seg['text'] for seg in chunk]) for chunk in chunks]
    try:
        with Pool(processes=cpu_count()) as pool:
            summaries = pool.map(summarize_text, texts)
    except Exception as e:
        print(f"Multiprocessing failed for summarization: {e}")
        summaries = [summarize_text(text) for text in texts]
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
video_file = r"D:\OneDrive - Wipro\Desktop\EF-connect-Recording.mp4"  # Replace with your video file path
segments = transcribe_video(video_file)
print(segments)
#embeddings = embed_segments_parallel(segments)
#chunks = semantic_chunking(segments, embeddings)
#summaries = summarize_chunks_parallel(chunks)
#output_folder = extract_video_segments(video_file, chunks)

# Print summaries
#for i, summary in enumerate(summaries):
#    print(f"Chunk {i+1} Summary: {summary}")

