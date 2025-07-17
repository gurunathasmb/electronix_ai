from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load sentiment model
sentiment_pipeline = pipeline("sentiment-analysis")

# Input model
class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict_sentiment(data: TextInput):
    result = sentiment_pipeline(data.text)[0]
    label = result['label']  # POSITIVE or NEGATIVE
    return {"sentiment": label}
