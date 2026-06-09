from backend.config import get_model
from backend.ai_fallbacks import (
    rewrite_fallback,
    safe_generate_text
)


def rewrite_resume(
    bullet_point
):

    prompt = f"""
    Rewrite the following resume bullet point.

    Make it:
    - Professional
    - ATS Friendly
    - Quantified where possible
    - Action oriented

    Bullet:
    {bullet_point}
    """

    return safe_generate_text(
        get_model,
        prompt,
        rewrite_fallback(
            bullet_point
        )
    )
