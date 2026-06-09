from backend.config import get_model
from backend.ai_fallbacks import (
    interview_fallback,
    safe_generate_text
)


def generate_interview_questions(
    resume_text,
    job_description
):

    prompt = f"""
    Generate interview questions based on the resume and job description.

    Create:

    1. HR Questions (5)
    2. Technical Questions (10)
    3. Project Questions (5)

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    return safe_generate_text(
        get_model,
        prompt,
        interview_fallback()
    )
