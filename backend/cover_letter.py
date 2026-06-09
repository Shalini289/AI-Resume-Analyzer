from backend.config import get_model
from backend.ai_fallbacks import (
    cover_letter_fallback,
    safe_generate_text
)


def generate_cover_letter(
    resume_text,
    job_description
):

    prompt = f"""
    Create a professional cover letter.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Requirements:
    - Professional tone
    - Highlight relevant skills
    - Mention projects
    - Keep under 400 words
    """

    return safe_generate_text(
        get_model,
        prompt,
        cover_letter_fallback()
    )
