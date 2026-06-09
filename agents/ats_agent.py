from agents.base_agent import BaseAgent


class ATSAgent(BaseAgent):

    def analyze(
        self,
        resume,
        jd
    ):

        prompt = f"""
        Analyze resume against job description.

        Return:

        1. ATS Score
        2. Matching Skills
        3. Missing Skills
        4. Suggestions

        Resume:
        {resume}

        Job Description:
        {jd}
        """

        return self.run(prompt)