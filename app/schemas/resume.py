from pydantic import BaseModel
from datetime import datetime

class ResumeCreate(BaseModel):
    name:str | None=None
    content:str

class ResumeOut(BaseModel):
    id:int
    name:str | None
    content:str
    created_at: datetime

    class Config:
        orm_mode=True