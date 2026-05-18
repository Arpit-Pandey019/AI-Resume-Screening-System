# 🚀 AI Resume Screening System

🔗 **Live Demo:** https://ai-resume-screening-system-4.onrender.com

---

## 📌 Overview

The **AI Resume Screening System** is a machine learning-based web application that automatically analyzes resumes and classifies them as **GOOD or BAD** based on skills, keywords, and content relevance.

It uses **Natural Language Processing (NLP)** and a **supervised machine learning model** to evaluate resumes efficiently.

---

## ⚙️ Features

- 🤖 AI-based resume classification
- 📄 Resume text analysis
- 🧹 NLP-based text preprocessing
- 📊 TF-IDF feature extraction
- 🧠 Machine Learning model (Naive Bayes)
- 🌐 Flask web application
- ☁️ Deployed on Render

---

## 🏗️ System Architecture

User Input (Resume Text)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Flask Backend (app.py)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Text Cleaning (utils.py)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
TF-IDF Vectorization  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Machine Learning Model  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Prediction (GOOD / BAD)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Web UI Response  

---

## 🧠 Machine Learning Model

- **Algorithm:** Multinomial Naive Bayes  
- **Type:** Supervised Learning  
- **Task:** Binary Classification  
- **Input:** Resume text  
- **Output:** GOOD or BAD resume  

The model learns patterns from labeled resume data and predicts the suitability of new resumes.

---

## 🧹 NLP Techniques Used

- Lowercasing text  
- Removing stopwords  
- Removing special characters  
- Tokenization  
- TF-IDF Vectorization  

---

## 🛠️ Tech Stack

- Python 🐍  
- Flask 🌐  
- Scikit-learn 🤖  
- Pandas 📊  
- NLTK 🧹  
- HTML5 + CSS3 🎨  
- Render ☁️  

---

## 📁 Project Structure
