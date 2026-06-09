import os


def validate_pdf(filename):

    return filename.lower().endswith(".pdf")


def validate_resume_text(text):

    if not text:
        return False

    if not text.strip():
        return False

    return True


def validate_job_description(jd):

    if not jd:
        return False

    if not jd.strip():
        return False

    return True


def validate_target_role(role):

    if not role:
        return False

    return True


def validate_linkedin_content(content):

    if not content:
        return False

    return len(content.strip()) > 30
