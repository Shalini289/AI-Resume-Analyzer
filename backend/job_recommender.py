from backend.config import get_model


def recommend_jobs(
    resume_text
):

    prompt = f"""
    Analyze the resume.

    Recommend:

    1. Top 10 Suitable Job Roles
    2. Match Percentage
    3. Why the role fits
    4. Expected Salary Range
    5. Skills to improve

    Resume:

    {resume_text}
    """

    response = get_model().generate_content(
        prompt
    )

    return response.text
