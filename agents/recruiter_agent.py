from agents.base_agent import BaseAgent


class RecruiterAgent(
    BaseAgent
):

    def evaluate(
        self,
        resume
    ):

        prompt = f"""
        Act as a recruiter.

        Evaluate this candidate.

        Return:

        1. Hire / No Hire
        2. Strengths
        3. Concerns
        4. Suggested Role

        Resume:
        {resume}
        """

        return self.run(prompt)