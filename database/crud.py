from database.models import (
    User,
    Resume,
    Analysis
)


def create_user(
    db,
    name,
    email,
    password_hash
):

    user = User(
        name=name,
        email=email,
        password_hash=password_hash
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def get_user_by_email(
    db,
    email
):

    return db.query(User)\
        .filter(
            User.email == email
        )\
        .first()


def get_user_by_id(
    db,
    user_id
):

    return db.query(User)\
        .filter(
            User.id == user_id
        )\
        .first()


def save_resume(
    db,
    user_id,
    file_name,
    resume_text
):

    resume = Resume(
        user_id=user_id,
        file_name=file_name,
        resume_text=resume_text
    )

    db.add(resume)

    db.commit()

    db.refresh(resume)

    return resume


def save_analysis(
    db,
    resume_id,
    ats_score,
    strengths,
    weaknesses,
    suggestions
):

    analysis = Analysis(
        resume_id=resume_id,
        ats_score=ats_score,
        strengths=strengths,
        weaknesses=weaknesses,
        suggestions=suggestions
    )

    db.add(analysis)

    db.commit()

    db.refresh(analysis)

    return analysis
