ATS_PROMPT = """
Analyze the resume against the job description.

Return ONLY valid JSON.

{
    "ats_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "strengths": [],
    "suggestions": []
}

Resume:
{resume}

Job Description:
{jd}
"""