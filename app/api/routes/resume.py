from fastapi import APIRouter,UploadFile,File,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeOut
from app.services.parser import parse_resume_text

router=APIRouter()

@router.post('/upload',response_model=ResumeOut)
async def upload_resume(
    file: UploadFile=File(...),
    db:AsyncSession=Depends(get_db)
):
    content=await file.read()
    text=parse_resume_text(content)

    resume=Resume(content=text)
    db.add(resume)
    await db.commit()
    await db.refresh(resume)

    return resume