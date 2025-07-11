from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.job import Job
from app.schemas.job import JobCreate,JobOut

router=APIRouter()

@router.post('/create',response_model=JobOut)
async def create_job(
    job:JobCreate,
    db:AsyncSession=Depends(get_db)
):
    job_obj=Job(**job.model_dump())
    db.add(job_obj)
    await db.commit()
    await db.refresh(job_obj)
    return job_obj
