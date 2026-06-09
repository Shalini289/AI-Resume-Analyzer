import streamlit as st
from backend.analyzer import analyze_resume

def ats_page():

    st.header("ATS Resume Analyzer")

    uploaded_resume = st.file_uploader(
        "Upload Resume",
        type=["pdf"]
    )

    jd = st.text_area(
        "Paste Job Description"
    )

    if st.button("Analyze"):

        result = analyze_resume(
            uploaded_resume,
            jd
        )

        score = result["ats_score"]

        st.metric(
            "ATS Score",
            score
        )

        st.progress(score)

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "Matching Skills"
            )

            for skill in result[
                "matching_skills"
            ]:
                st.success(skill)

        with col2:

            st.subheader(
                "Missing Skills"
            )

            for skill in result[
                "missing_skills"
            ]:
                st.error(skill)

        st.subheader(
            "Suggestions"
        )

        for item in result[
            "suggestions"
        ]:
            st.warning(item)