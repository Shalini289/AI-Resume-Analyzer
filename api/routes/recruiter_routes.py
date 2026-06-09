from fastapi import APIRouter

router = APIRouter()


@router.get("/dashboard")
def recruiter_dashboard():

    return {
        "message":
        "Recruiter Dashboard"
    }


@router.get("/top-candidates")
def top_candidates():

    return {
        "candidates": [
            {
                "name":
                "Candidate A",
                "ats_score":
                91
            },
            {
                "name":
                "Candidate B",
                "ats_score":
                88
            }
        ]
    }