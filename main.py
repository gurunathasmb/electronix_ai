from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


sentiment_pipeline = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.post("/predict")
async def predict_sentiment(data: TextInput):
    result = sentiment_pipeline(data.text)[0]
    label = result['label']  
    return {"sentiment": label}
