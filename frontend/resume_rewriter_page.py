import streamlit as st
from backend.resume_rewriter import (
    rewrite_resume
)

def resume_rewriter_page():

    st.header(
        "Resume Rewriter"
    )

    text = st.text_area(
        "Paste Resume Bullet"
    )

    if st.button(
        "Rewrite"
    ):

        rewritten = rewrite_resume(
            text
        )

        st.markdown(
            rewritten
        )