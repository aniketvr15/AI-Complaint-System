from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load AI Models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
categorizer = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

# Request Schema
class ComplaintRequest(BaseModel):
    complaint: str

# Summarization Endpoint
@app.post("/summarize")
def summarize_complaint(request: ComplaintRequest):
    summary = summarizer(request.complaint, max_length=50, min_length=10, do_sample=False)
    return {"summary": summary[0]['summary_text']}

# Categorization Endpoint
@app.post("/categorize")
def categorize_complaint(request: ComplaintRequest):
    category = categorizer(request.complaint)
    return {"category": category[0]['label']}

# Combined Processing Endpoint
@app.post("/process")
def process_complaint(request: ComplaintRequest):
    summary = summarizer(request.complaint, max_length=50, min_length=10, do_sample=False)
    category = categorizer(request.complaint)
    return {"summary": summary[0]['summary_text'], "category": category[0]['label']}
