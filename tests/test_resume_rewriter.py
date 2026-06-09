from backend.resume_rewriter import (
    rewrite_resume
)


def test_rewriter_function_exists():

    assert callable(
        rewrite_resume
    )