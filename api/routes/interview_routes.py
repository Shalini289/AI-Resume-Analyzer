from fastapi import APIRouter
from pydantic import BaseModel

from backend.interview_generator import (
    generate_interview_questions
)

router = APIRouter()


class InterviewRequest(
    BaseModel
):

    resume_text: str
    job_description: str


@router.post("/generate")
def generate_questions(
    data: InterviewRequest
):

    questions = generate_interview_questions(
        data.resume_text,
        data.job_description
    )

    return {
        "questions":
        questions
    }