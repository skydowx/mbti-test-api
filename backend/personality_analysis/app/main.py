import uvicorn
from typing import List

from fastapi import Depends, FastAPI, HTTPException, Form
from sqlalchemy.orm import Session

# from app.predict_types import predict_text
import crud, models, schemas #ERROR
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post('/checkPersonality')
# async def get_personality(text: str = Form(...)):
#     personality = predict_text(text)
#     return {"personality": personality}

@app.post('/checkPersonality', response_model=schemas.Result)
def get_personality(result: schemas.ResultCreate, db: Session = Depends(get_db)):
    # personality = predict_text(result.input_text)
    
    return crud.create_result(db=db, result=result)