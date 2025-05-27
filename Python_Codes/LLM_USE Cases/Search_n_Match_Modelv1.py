import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Sample dataset with job descriptions, resumes, and match labels
data = {
    'Job_Description': [
        "Job description for .Net MVC Developer",
        "Job description for Data Scientist",
        "Job description for Frontend Developer",
        "Job description for Backend Developer",
        "Job description for Project Manager"
    ],
    'Resume': [
        "Resume for .Net MVC Developer",
        "Resume for Data Scientist",
        "Resume for Frontend Developer",
        "Resume for Backend Developer",
        "Resume for Project Manager"
    ],
    'Match': [1, 1, 1, 1, 1]
}

# Add non-matching examples
data['Job_Description'].extend([
    "Job description for .Net MVC Developer",
    "Job description for Data Scientist",
    "Job description for Frontend Developer",
    "Job description for Backend Developer",
    "Job description for Project Manager"
])
data['Resume'].extend([
    "Resume for Data Scientist",
    "Resume for Frontend Developer",
    "Resume for Backend Developer",
    "Resume for Project Manager",
    "Resume for .Net MVC Developer"
])
data['Match'].extend([0, 0, 0, 0, 0])

# Create DataFrame
df = pd.DataFrame(data)

# Combine job descriptions and resumes into a single dataset
documents = df['Job_Description'] + " " + df['Resume']

# Vectorize the documents using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Calculate the cosine similarity between job descriptions and resumes
cosine_sim = [cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix[i+1:i+2])[0][0] for i in range(0, len(documents), 2)] # type: ignore

# Prepare the dataset for training a machine learning model
X = tfidf_matrix.toarray() # type: ignore
y = df['Match'].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict the match quality on the test set
y_pred = model.predict(X_test)

# Calculate evaluation metrics
precision = precision_score(y_test, y_pred, zero_division=1)
recall = recall_score(y_test, y_pred, zero_division=1)
f1 = f1_score(y_test, y_pred, zero_division=1)
accuracy = accuracy_score(y_test, y_pred)

# Print the results
print(f"Cosine Similarity: {cosine_sim}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")
print(f"Accuracy: {accuracy}")

