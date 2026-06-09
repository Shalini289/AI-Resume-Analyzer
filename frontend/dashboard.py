import streamlit as st
from ats_page import ats_page
from resume_chat import resume_chat_page
from interview_page import interview_page
from cover_letter_page import cover_letter_page
from skill_gap_page import skill_gap_page
from resume_rewriter_page import resume_rewriter_page
from linkedin_page import linkedin_page

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.sidebar.title("AI Resume Analyzer")

page = st.sidebar.selectbox(
    "Choose Feature",
    [
        "ATS Analyzer",
        "Resume Chat",
        "Interview Generator",
        "Cover Letter",
        "Skill Gap Analysis",
        "Resume Rewriter",
        "LinkedIn Optimizer"
    ]
)

if page == "ATS Analyzer":
    ats_page()

elif page == "Resume Chat":
    resume_chat_page()

elif page == "Interview Generator":
    interview_page()

elif page == "Cover Letter":
    cover_letter_page()

elif page == "Skill Gap Analysis":
    skill_gap_page()

elif page == "Resume Rewriter":
    resume_rewriter_page()

elif page == "LinkedIn Optimizer":
    linkedin_page()