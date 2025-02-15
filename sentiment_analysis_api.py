from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize the FastAPI app
app = FastAPI()

# Load a pre-trained sentiment analysis model from Hugging Face
# Using a small model (distilbert) for faster response times
sentiment_model = pipeline("sentiment-analysis")

class SentimentRequest(BaseModel):
    text: str #everytime the user sends a request to the api, this class will enfornce type validation bc it is expecting the text whose sentiment we want to analyze

class SentimentResponse(BaseModel):
    label: str #This field holds the sentiment label returned by the model, e.g., "POSITIVE" or "NEGATIVE".
    score: float #This field holds the confidence score (a floating-point number between 0 and 1) that the model assigns to the sentiment label. For example, the score might be 0.99 for a high confidence in the "POSITIVE" label.


@app.post("/analyze_sentiment", response_model=SentimentResponse)
async def analyze_sentiment(request: SentimentRequest):
    """
    Endpoint to analyze sentiment of a given text.
    """
    # Get the sentiment analysis results
    sentiment = sentiment_model(request.text)[0]

    # Extract the label and score
    label = sentiment['label']
    score = sentiment['score']

    # Return the response
    return SentimentResponse(label=label, score=score)