from agents.base_agent import BaseAgent


class CareerAgent(
    BaseAgent
):

    def roadmap(
        self,
        resume,
        target_role
    ):

        prompt = f"""
        Create a career roadmap.

        Resume:
        {resume}

        Target Role:
        {target_role}

        Return:

        - Missing Skills
        - Learning Plan
        - Certifications
        - Projects
        """

        return self.run(prompt)