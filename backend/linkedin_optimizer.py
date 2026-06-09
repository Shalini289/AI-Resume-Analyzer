from backend.config import get_model
from backend.ai_fallbacks import (
    linkedin_fallback,
    safe_generate_text
)


def optimize_linkedin(
    linkedin_content
):

    prompt = f"""
    Analyze and improve this LinkedIn profile content.

    Return:

    1. Improved Headline
    2. Improved About Section
    3. Skill Recommendations
    4. Networking Suggestions

    LinkedIn Content:

    {linkedin_content}
    """

    return safe_generate_text(
        get_model,
        prompt,
        linkedin_fallback()
    )
