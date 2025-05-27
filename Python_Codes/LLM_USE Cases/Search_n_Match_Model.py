# For SSL Certificate Error - python -m pip install pip-system-certs --use-feature=truststore

import docx
import pdfplumber
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
from sentence_transformers import SentenceTransformer

# Function to extract text from a .docx file
def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

# Function to extract text from a .pdf file
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        return "\n".join([page.extract_text() for page in pdf.pages])

# Function to calculate similarity using TF-IDF
def calculate_tfidf_similarity(docs):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    return cosine_similarity(tfidf_matrix)

# Function to calculate similarity using Sentence Transformers
def calculate_embedding_similarity(docs):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(docs)
    return cosine_similarity(embeddings)

# Function to evaluate the model
def evaluate_model(y_true, y_pred):
    precision = precision_score(y_true, y_pred, average='binary')
    recall = recall_score(y_true, y_pred, average='binary')
    f1 = f1_score(y_true, y_pred, average='binary')
    accuracy = accuracy_score(y_true, y_pred)
    return precision, recall, f1, accuracy

# Paths to the job description and resume files
jd_path = r"D:\OneDrive - Wipro\Desktop\.Net MVC Developer JD.docx"
resume_path = r"D:\OneDrive - Wipro\Desktop\Temp2\Resume\Chandan Karmakar Resume.pdf"

# Extract text from the files
jd_text = extract_text_from_docx(jd_path)
resume_text = extract_text_from_pdf(resume_path)

# Combine texts for similarity calculation
documents = [jd_text, resume_text]

# Calculate TF-IDF similarity
tfidf_similarity = calculate_tfidf_similarity(documents)

# Calculate Sentence Transformer similarity
embedding_similarity = calculate_embedding_similarity(documents)

# Assuming labeled data for evaluation (1 for match, 0 for no match)
y_true = [1]  # Example label
y_pred_tfidf = [1 if tfidf_similarity[0][1] > 0.5 else 0]
y_pred_embedding = [1 if embedding_similarity[0][1] > 0.5 else 0]

# Evaluate TF-IDF model
precision_tfidf, recall_tfidf, f1_tfidf, accuracy_tfidf = evaluate_model(y_true, y_pred_tfidf)

# Evaluate Embedding model
precision_embedding, recall_embedding, f1_embedding, accuracy_embedding = evaluate_model(y_true, y_pred_embedding)

# Print evaluation results
print("TF-IDF Model Evaluation:")
print(f"Precision: {precision_tfidf}, Recall: {recall_tfidf}, F1-Score: {f1_tfidf}, Accuracy: {accuracy_tfidf}")

print("Embedding Model Evaluation:")
print(f"Precision: {precision_embedding}, Recall: {recall_embedding}, F1-Score: {f1_embedding}, Accuracy: {accuracy_embedding}")

