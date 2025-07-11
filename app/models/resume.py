from sqlalchemy import Column, Integer, String ,Text, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Resume(Base):
    __tablename__="resumes"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=True)
    content=Column(Text,nullable=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())