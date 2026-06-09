from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey
)

from datetime import datetime

from database.postgres import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String(100))

    email = Column(
        String(150),
        unique=True
    )

    password_hash = Column(
        String(255)
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Resume(Base):

    __tablename__ = "resumes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    file_name = Column(
        String(255)
    )

    resume_text = Column(
        Text
    )

    uploaded_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Analysis(Base):

    __tablename__ = "analysis"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id")
    )

    ats_score = Column(
        Integer
    )

    strengths = Column(
        Text
    )

    weaknesses = Column(
        Text
    )

    suggestions = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class InterviewHistory(Base):

    __tablename__ = "interview_history"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    score = Column(
        Integer
    )

    feedback = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )