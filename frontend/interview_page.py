import streamlit as st
from backend.interview_generator import (
    generate_interview_questions
)

def interview_page():

    st.header(
        "Interview Generator"
    )

    jd = st.text_area(
        "Job Description"
    )

    if st.button(
        "Generate Questions"
    ):

        questions = generate_interview_questions(
            jd
        )

        st.markdown(
            questions
        )