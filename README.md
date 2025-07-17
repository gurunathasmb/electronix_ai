# 🚀 Electronix AI – Microservice Sentiment Analysis

A lightweight and efficient **Sentiment Analysis Microservice** built from scratch by **Gurunatha Gouda**. This microservice is a part of the **Electronix AI** project, designed for modular AI-based services that are easy to integrate and deploy.

This project does **not** use any pretrained models – the sentiment classifier is trained from the ground up using custom-generated datasets and basic NLP techniques.

---

## 🔍 Overview

- 🔤 Classifies text into **Positive**, **Negative**, or **Neutral**
- 🧠 Trained using a custom NLP pipeline (TfidfVectorizer + LogisticRegression)
- 📦 Exposes a REST API using **Flask**
- 🐳 Fully Dockerized
- 📁 Dataset generation and training scripts included

---

## 🗂️ Folder Structure

```
electronix_ai/
│
├── app/
│   ├── main.py               # Flask API
│   ├── routes/predict.py     # Inference logic
│   └── model/                # Trained model & vectorizer
│
├── dataset/
│   └── sentiment_dataset.jsonl  # Labeled dataset
│
├── train/
│   ├── generate_dataset.py   # Generate synthetic data
│   └── train_model.py        # Train sentiment model
│
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone this repository

```bash
git clone https://github.com/gurunatha/electronix_ai.git
cd electronix_ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Generate custom dataset

```bash
python train/generate_dataset.py --count 5000
```

### 5. Train the model

```bash
python train/train_model.py
```

### 6. Start the microservice

```bash
python app/main.py
```

Runs on: `http://localhost:5000`

---

## 🔁 Sample API Call

### Endpoint:
```
POST /predict
```

### Request:
```json
{
  "text": "I really enjoy using this!"
}
```

### Response:
```json
{
  "sentiment": "positive"
}
```

---

## 🐳 Run with Docker

```bash
docker build -t electronix-sentiment .
docker run -p 5000:5000 electronix-sentiment
```

---

## 📦 Dependencies

Inside `requirements.txt`:
```
flask
scikit-learn
nltk
joblib
```

Also run once in Python:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---
