from pydantic import BaseModel
from typing import List, Optional

class MatchRequest(BaseModel):
    resume_id: int  # or the resume content if you want direct matching from text

class JobMatch(BaseModel):
    job_id: int
    title: str
    description: str
    score: Optional[float]  # if you calculate a match score

class MatchResponse(BaseModel):
    matches: List[JobMatch]
