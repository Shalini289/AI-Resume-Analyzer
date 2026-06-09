from fastapi import FastAPI

from api.routes.auth_routes import router as auth_router
from api.routes.resume_routes import router as resume_router
from api.routes.interview_routes import router as interview_router
from api.routes.recruiter_routes import router as recruiter_router

app = FastAPI(
    title="AI Resume Analyzer API",
    version="1.0.0"
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)

app.include_router(
    interview_router,
    prefix="/interview",
    tags=["Interview"]
)

app.include_router(
    recruiter_router,
    prefix="/recruiter",
    tags=["Recruiter"]
)


@app.get("/")
def home():

    return {
        "message":
        "AI Resume Analyzer API Running"
    }