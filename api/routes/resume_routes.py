from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Form
)

from backend.parser import extract_text
from backend.analyzer import analyze_resume

router = APIRouter()


@router.post("/analyze")
async def analyze_resume_api(
    file: UploadFile = File(...),
    jd: str = Form(...)
):

    resume_text = extract_text(
        file.file
    )

    result = analyze_resume(
        resume_text,
        jd
    )

    return result