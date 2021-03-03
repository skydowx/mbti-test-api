from sqlalchemy.orm import Session

import models, schemas

def get_result(db: Session, result_id: int):
    return db.query(models.Result).filter(models.Result.id == result_id).first()

def get_result_by_personality_type(db: Session, personality_type: str):
    return db.query(models.Result).filter(models.Result.personality_type == personality_type).first()

def create_result(db: Session, result: schemas.ResultCreate):
    db_result = models.Result(input_text=result.input_text, personality_type=result.personality_type)
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result