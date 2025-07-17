# 🚀 Electronix AI – Microservice Sentiment Analysis

A scalable and lightweight microservice for **sentiment analysis**, built from scratch without using any pretrained models. This microservice is part of the **Electronix AI** initiative to provide modular, containerized AI services for real-world applications.

---

## 🧠 Features

- Custom-trained sentiment classifier (no pretrained models)
- Flask REST API for predictions
- JSON-based request and response
- Dockerized deployment
- Dataset generator and training scripts included

---

## 🗂️ Project Structure

electronix_ai/
├── app/
│ ├── main.py # Flask API entrypoint
│ ├── routes/predict.py # Prediction logic
│ └── model/ # Trained model and vectorizer
├── dataset/
│ └── sentiment_dataset.jsonl # Sample/generated dataset
├── train/
│ ├── generate_dataset.py # Script to generate synthetic labeled data
│ └── train_model.py # Script to train sentiment model
├── Dockerfile
├── requirements.txt
├── LICENSE
└── README.md

yaml
Copy
Edit

---

## 🔧 Setup & Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/electronix_ai.git
cd electronix_ai
2. (Optional) Create virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Generate dataset (optional)
bash
Copy
Edit
python train/generate_dataset.py --count 5000
5. Train the model
bash
Copy
Edit
python train/train_model.py
6. Run the Flask app
bash
Copy
Edit
python app/main.py
Visit http://localhost:5000 to access the API.

📦 Docker Instructions
Build and Run the Docker Container
bash
Copy
Edit
docker build -t electronix-sentiment .
docker run -p 5000:5000 electronix-sentiment
📤 API Usage
Endpoint: /predict
Method: POST
Payload:

json
Copy
Edit
{
  "text": "I love this product!"
}
Response:

json
Copy
Edit
{
  "sentiment": "positive"
}
🛠 Tech Stack
Python

Flask

scikit-learn

NLTK

Docker

