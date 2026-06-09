INTERVIEW_PROMPT = """
Generate interview questions based on the resume and job description.

Return:

1. HR Questions (5)
2. Technical Questions (10)
3. Project Questions (5)

Questions should increase in difficulty.

Resume:
{resume}

Job Description:
{jd}
"""