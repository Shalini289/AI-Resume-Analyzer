from backend.utils.validators import (
    validate_job_description,
    validate_resume_text
)


def test_resume_validation():

    assert validate_resume_text(
        "Python Developer Resume"
    )


def test_jd_validation():

    assert validate_job_description(
        "Need Python Developer"
    )