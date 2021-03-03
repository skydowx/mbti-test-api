from typing import List, Optional

from pydantic import BaseModel

class ResultBase(BaseModel):
    input_text: str

class ResultCreate(ResultBase):
    personality_type: str

class Result(ResultBase):
    id: int
    personality_type: str

    class Config:
        orm_mode = True