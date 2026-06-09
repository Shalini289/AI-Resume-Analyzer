from backend.analyzer import (
    build_ats_prompt,
    clean_json
)


def test_json_parser():

    response = """
    {
        "ats_score": 80,
        "matching_skills": [],
        "missing_skills": [],
        "strengths": [],
        "suggestions": []
    }
    """

    result = clean_json(
        response
    )

    assert result[
        "ats_score"
    ] == 80


def test_ats_prompt_formats_json_schema():

    prompt = build_ats_prompt(
        "Python resume",
        "Python role"
    )

    assert '"ats_score": 0' in prompt
    assert "Python resume" in prompt
    assert "Python role" in prompt
