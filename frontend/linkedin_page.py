import streamlit as st
from backend.linkedin_optimizer import (
    optimize_linkedin
)

def linkedin_page():

    st.header(
        "LinkedIn Optimizer"
    )

    content = st.text_area(
        "Paste LinkedIn About Section"
    )

    if st.button(
        "Optimize"
    ):

        result = optimize_linkedin(
            content
        )

        st.markdown(
            result
        )