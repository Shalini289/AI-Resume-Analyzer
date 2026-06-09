import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

_model = None


def get_model():
    global _model

    if _model is None:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GEMINI_API_KEY is not configured."
            )

        genai.configure(
            api_key=api_key
        )

        _model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    return _model
