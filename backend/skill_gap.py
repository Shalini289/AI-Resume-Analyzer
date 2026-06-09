from backend.config import get_model
from backend.ai_fallbacks import (
    safe_generate_text,
    skill_gap_fallback
)


def analyze_skill_gap(
    resume_text,
    target_role
):

    prompt = f"""
    Analyze the resume and compare it to the target role.

    Return:

    1. Current Skills
    2. Missing Skills
    3. Learning Roadmap
    4. Recommended Projects
    5. Certifications

    Resume:
    {resume_text}

    Target Role:
    {target_role}
    """

    return safe_generate_text(
        get_model,
        prompt,
        skill_gap_fallback()
    )
