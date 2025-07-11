from pydantic import BaseModel
from datetime import datetime

class JobCreate(BaseModel):
    title:str
    description:str

class JobOut(BaseModel):
    id:int
    title:str
    description:str
    created_at:datetime

    class Config:
        orm_mode=True