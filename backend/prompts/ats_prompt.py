ATS_PROMPT = """
You are an expert Applicant Tracking System (ATS).

Analyze the resume against the job description.

Return ONLY valid JSON.

{
    "ats_score": 0,
    "matching_skills": [],
    "missing_skills": [],
    "strengths": [],
    "suggestions": []
}

Evaluation Criteria:

1. Skill Match
2. Relevant Experience
3. Project Relevance
4. Education
5. ATS Keywords

Resume:
{resume}

Job Description:
{jd}
"""