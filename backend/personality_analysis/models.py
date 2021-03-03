from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from database import Base


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    input_text = Column(String)
    personality_type = Column(String)