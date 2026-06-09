import streamlit as st
from backend.rag import ask_resume_question

def resume_chat_page():

    st.header(
        "Chat With Resume"
    )

    question = st.text_input(
        "Ask about your resume"
    )

    if st.button(
        "Ask"
    ):

        answer = ask_resume_question(
            question
        )

        st.markdown(answer)