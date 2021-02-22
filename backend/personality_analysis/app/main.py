from fastapi import FastAPI, Form
from .predict_types import predict_text
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/checkPersonality')
async def get_personality(text: str = Form(...)):
    personality = predict_text(text)
    return {"personality": personality}