import streamlit as st
from backend.cover_letter import (
    generate_cover_letter
)

def cover_letter_page():

    st.header(
        "Cover Letter Generator"
    )

    jd = st.text_area(
        "Job Description"
    )

    if st.button(
        "Generate Cover Letter"
    ):

        letter = generate_cover_letter(
            jd
        )

        st.markdown(letter)