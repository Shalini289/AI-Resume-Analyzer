import streamlit as st
from backend.skill_gap import (
    analyze_skill_gap
)

def skill_gap_page():

    st.header(
        "Skill Gap Analyzer"
    )

    role = st.text_input(
        "Target Role"
    )

    if st.button(
        "Analyze"
    ):

        result = analyze_skill_gap(
            role
        )

        st.markdown(
            result
        )