from pydantic import BaseModel


class UserCreate(BaseModel):

    name: str

    email: str

    password: str


class UserResponse(BaseModel):

    id: int

    name: str

    email: str

    class Config:
        from_attributes = True


class ResumeCreate(BaseModel):

    file_name: str

    resume_text: str


class AnalysisResponse(BaseModel):

    ats_score: int

    strengths: str

    weaknesses: str

    suggestions: str

    class Config:
        from_attributes = True