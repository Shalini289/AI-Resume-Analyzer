from agents.ats_agent import ATSAgent

from agents.interview_agent import (
    InterviewAgent
)

from agents.resume_coach_agent import (
    ResumeCoachAgent
)

from agents.career_agent import (
    CareerAgent
)

from agents.recruiter_agent import (
    RecruiterAgent
)


class ResumeWorkflow:

    def __init__(self):

        self.ats = ATSAgent()

        self.interview = InterviewAgent()

        self.coach = ResumeCoachAgent()

        self.career = CareerAgent()

        self.recruiter = RecruiterAgent()

    def run(
        self,
        resume,
        jd,
        target_role
    ):

        return {

            "ats_analysis":
            self.ats.analyze(
                resume,
                jd
            ),

            "interview_questions":
            self.interview.generate_questions(
                resume,
                jd
            ),

            "resume_feedback":
            self.coach.coach(
                resume
            ),

            "career_roadmap":
            self.career.roadmap(
                resume,
                target_role
            ),

            "recruiter_review":
            self.recruiter.evaluate(
                resume
            )
        }