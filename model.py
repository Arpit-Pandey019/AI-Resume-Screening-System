import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from utils import clean_text

# sample dataset (replace with real dataset later)
data = pd.read_csv("data/resumes_dataset.csv")

data['clean'] = data['resume'].apply(clean_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['clean'])
y = data['label']

model = MultinomialNB()
model.fit(X, y)

joblib.dump(model, "ml_model/resume_model.pkl")
joblib.dump(vectorizer, "ml_model/vectorizer.pkl")

print("Model trained successfully")