from backend.analyzer import (
    analyze_resume
)
from backend.interview_generator import (
    generate_interview_questions
)


class FailingModel:

    def generate_content(
        self,
        prompt
    ):

        raise RuntimeError(
            "ResourceExhausted: 429 quota exceeded"
        )


def test_interview_generator_returns_fallback_on_quota_error(
    monkeypatch
):

    monkeypatch.setattr(
        "backend.interview_generator.get_model",
        lambda: FailingModel()
    )

    result = generate_interview_questions(
        "Python resume",
        "Python role"
    )

    assert "AI generation is temporarily unavailable" in result
    assert "HR Questions" in result


def test_analyzer_returns_json_fallback_on_quota_error(
    monkeypatch
):

    monkeypatch.setattr(
        "backend.analyzer.get_model",
        lambda: FailingModel()
    )

    result = analyze_resume(
        "Python resume",
        "Python role"
    )

    assert result["ats_score"] == 0
    assert result["suggestions"]
