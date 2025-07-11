from fastapi import FastAPI
from app.api.routes import resume,job,match
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

#Allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
                   )

#Include routers
app.include_router(resume.router,prefix="/api/resume")
app.include_router(job.router,prefix="/api/jobs")
app.include_router(match.router,prefix="/api/match")