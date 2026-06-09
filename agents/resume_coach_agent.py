from agents.base_agent import BaseAgent


class ResumeCoachAgent(
    BaseAgent
):

    def coach(
        self,
        resume
    ):

        prompt = f"""
        Act as a FAANG recruiter.

        Review the resume.

        Provide:

        1. Weaknesses
        2. Improvements
        3. Better Project Descriptions
        4. ATS Recommendations

        Resume:
        {resume}
        """

        return self.run(prompt)