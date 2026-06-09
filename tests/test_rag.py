from backend.rag import (
    build_resume_context,
    split_resume
)


def test_chunk_creation():

    text = (
        "Python " * 1000
    )

    chunks = split_resume(
        text
    )

    assert len(chunks) > 0


def test_resume_context_prioritizes_question_terms():

    resume = """
    Python developer with backend API experience.

    Built dashboards with React.

    Managed hiring and recruiting operations.
    """

    context = build_resume_context(
        "What backend API experience is listed?",
        resume
    )

    assert "backend API experience" in context
