from backend.config import model


class BaseAgent:

    def __init__(self):
        self.model = model

    def run(self, prompt):

        response = self.model.generate_content(
            prompt
        )

        return response.text