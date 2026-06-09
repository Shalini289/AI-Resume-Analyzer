import json
import re

from backend.config import get_model
from backend.ai_fallbacks import (
    get_error_message
)

ATS_PROMPT = """
You are an expert ATS Resume Analyzer.

Analyze the resume against the job description.

Return ONLY valid JSON.

{{
  "ats_score": 0,
  "matching_skills": [],
  "missing_skills": [],
  "strengths": [],
  "suggestions": []
}}

Resume:
{resume}

Job Description:
{jd}
"""


def build_ats_prompt(
    resume_text,
    job_description
):

    return ATS_PROMPT.format(
        resume=resume_text,
        jd=job_description
    )


def clean_json(response_text):

    response_text = re.sub(
        r"```json|```",
        "",
        response_text
    ).strip()

    try:
        return json.loads(response_text)

    except Exception:

        return {
            "ats_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "strengths": [],
            "suggestions": [
                "Could not parse AI response."
            ]
        }


def analyze_resume(
    resume_text,
    job_description
):

    prompt = build_ats_prompt(
        resume_text,
        job_description
    )

    try:
        response = get_model().generate_content(
            prompt
        )

        return clean_json(
            response.text
        )

    except Exception as error:
        return {
            "ats_score": 0,
            "matching_skills": [],
            "missing_skills": [],
            "strengths": [],
            "suggestions": [
                get_error_message(error),
                "Retry after the quota resets, or use Resume Insights for an offline resume audit."
            ]
        }
