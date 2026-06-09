from backend.resume_insights import (
    analyze_resume_insights
)


def test_resume_insights_detects_core_signals():

    resume = """
    Jane Doe
    jane@example.com
    linkedin.com/in/janedoe
    github.com/janedoe

    Summary:
    Python developer focused on data analysis.

    Skills:
    Python, SQL, React, FastAPI, Docker

    Experience:
    - Built an analytics dashboard used by 500 users.

    Projects:
    - Created an AI resume analyzer.

    Education:
    B.Tech Computer Science
    """

    result = analyze_resume_insights(
        resume
    )

    assert result["overall_score"] >= 80
    assert result["contact_signals"]["email"]
    assert result["contact_signals"]["linkedin"]
    assert "skills" in result["detected_sections"]
    assert "python" in result["detected_skills"]
    assert result["quantified_bullets"] == 1


def test_resume_insights_recommends_missing_sections():

    result = analyze_resume_insights(
        "Python developer"
    )

    assert result["missing_sections"]
    assert result["recommendations"]
