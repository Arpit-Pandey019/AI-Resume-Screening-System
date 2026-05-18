from flask import Flask, render_template, request
import joblib
from utils import clean_text

app = Flask(__name__)

model = joblib.load("ml_model/resume_model.pkl")
vectorizer = joblib.load("ml_model/vectorizer.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    resume_text = request.form['resume']
    
    cleaned = clean_text(resume_text)
    vector = vectorizer.transform([cleaned])
    result = model.predict(vector)[0]

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)