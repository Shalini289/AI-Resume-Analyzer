import streamlit as st
from pathlib import Path

from backend.parser import extract_text
from backend.analyzer import analyze_resume

from backend.rag import (
    ask_resume_question
)

from backend.interview_generator import (
    generate_interview_questions
)

from backend.cover_letter import (
    generate_cover_letter
)

from backend.skill_gap import (
    analyze_skill_gap
)

from backend.resume_rewriter import (
    rewrite_resume
)

from backend.linkedin_optimizer import (
    optimize_linkedin
)

from backend.resume_insights import (
    analyze_resume_insights
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon=":page_facing_up:",
    layout="wide"
)


def load_styles():
    css_path = Path(__file__).parent / "assets" / "styles.css"

    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True
        )


load_styles()


FEATURES = {
    "Resume Insights": {
        "eyebrow": "Instant resume audit",
        "title": "Resume Insights",
        "description": "Get a fast structural audit with contact checks, section coverage, keywords, and improvement priorities.",
        "action": "Generate Insights"
    },
    "ATS Analyzer": {
        "eyebrow": "Resume scoring",
        "title": "ATS Resume Analysis",
        "description": "Compare a resume with a role description and surface match signals, gaps, and next steps.",
        "action": "Analyze Resume"
    },
    "Resume Chat": {
        "eyebrow": "Resume Q&A",
        "title": "Chat With Resume",
        "description": "Ask focused questions about the uploaded resume using the indexed resume context.",
        "action": "Ask"
    },
    "Interview Generator": {
        "eyebrow": "Interview prep",
        "title": "Interview Questions",
        "description": "Generate role-specific HR, technical, and project questions from the resume and job description.",
        "action": "Generate Questions"
    },
    "Cover Letter": {
        "eyebrow": "Application writing",
        "title": "Cover Letter Generator",
        "description": "Create a concise cover letter aligned to the resume and target role.",
        "action": "Generate Cover Letter"
    },
    "Skill Gap": {
        "eyebrow": "Career roadmap",
        "title": "Skill Gap Analyzer",
        "description": "Compare the resume with a target role and outline skills, projects, and learning priorities.",
        "action": "Analyze Skill Gap"
    },
    "Resume Rewriter": {
        "eyebrow": "Bullet polish",
        "title": "Resume Bullet Rewriter",
        "description": "Rewrite resume bullets to be sharper, action-led, and ATS friendly.",
        "action": "Rewrite"
    },
    "LinkedIn Optimizer": {
        "eyebrow": "Profile polish",
        "title": "LinkedIn Profile Optimizer",
        "description": "Improve LinkedIn headline, about copy, skills, and networking positioning.",
        "action": "Optimize"
    }
}


def render_feature_header(name):
    feature = FEATURES[name]

    st.markdown(
        f"""
        <section class="feature-header">
            <span>{feature["eyebrow"]}</span>
            <h2>{feature["title"]}</h2>
            <p>{feature["description"]}</p>
        </section>
        """,
        unsafe_allow_html=True
    )


def render_output(content):
    st.markdown(
        '<div class="result-shell">',
        unsafe_allow_html=True
    )
    st.markdown(content)
    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None

if "vector_store_ready" not in st.session_state:
    st.session_state.vector_store_ready = False

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.markdown(
    """
    <div class="sidebar-brand">
        <div class="brand-mark">AI</div>
        <div>
            <h1>AI Resume Analyzer</h1>
            <p>Resume intelligence workspace</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Workspace",
    [
        "Resume Insights",
        "ATS Analyzer",
        "Resume Chat",
        "Interview Generator",
        "Cover Letter",
        "Skill Gap",
        "Resume Rewriter",
        "LinkedIn Optimizer"
    ]
)

resume_status = (
    "Resume ready"
    if st.session_state.resume_text
    else "Upload required"
)

st.sidebar.markdown(
    f"""
    <div class="sidebar-status">
        <span>Current view</span>
        <strong>{page}</strong>
    </div>
    <div class="sidebar-status">
        <span>Resume status</span>
        <strong>{resume_status}</strong>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    """
    <section class="app-hero">
        <div>
            <span class="hero-kicker">AI-powered resume intelligence</span>
            <h1>AI Resume Analyzer</h1>
            <p>
                Analyze fit, polish content, prepare interviews, and turn a resume
                into a focused application strategy from one clean workspace.
            </p>
        </div>
        <div class="hero-panel">
            <span>Active workspace</span>
            <strong>Resume Review Suite</strong>
            <p>Upload once, then move across analysis, writing, and coaching tools.</p>
        </div>
    </section>
    """,
    unsafe_allow_html=True
)

upload_col, status_col = st.columns(
    [1.35, 0.65],
    gap="large"
)

with upload_col:
    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"],
        help="Use a PDF resume to unlock analysis, chat, and generation tools."
    )

with status_col:
    st.markdown(
        f"""
        <div class="resume-card">
            <span>Resume status</span>
            <strong>{resume_status}</strong>
            <p>Current tool: {page}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if uploaded_file:

    resume_text = extract_text(uploaded_file)

    st.session_state.resume_text = resume_text

    st.session_state.vector_store_ready = True

    st.success("Resume uploaded successfully")

# ===================================================
# RESUME INSIGHTS
# ===================================================

if page == "Resume Insights":

    render_feature_header(page)

    if not st.session_state.resume_text:
        st.info("Upload a resume PDF to generate instant insights.")

    else:
        insights = analyze_resume_insights(
            st.session_state.resume_text
        )

        score_col, words_col, bullets_col, quantified_col = st.columns(4)

        with score_col:
            st.metric(
                "Resume Health",
                f"{insights['overall_score']}/100"
            )

        with words_col:
            st.metric(
                "Words",
                insights["word_count"]
            )

        with bullets_col:
            st.metric(
                "Bullets",
                insights["bullet_count"]
            )

        with quantified_col:
            st.metric(
                "Quantified",
                insights["quantified_bullets"]
            )

        st.progress(
            insights["overall_score"]
        )

        contact_col, section_col = st.columns(2)

        with contact_col:
            st.markdown("### Contact Signals")

            for label, present in insights["contact_signals"].items():
                message = f"{label.title()}: {'Found' if present else 'Missing'}"

                if present:
                    st.success(message)
                else:
                    st.warning(message)

        with section_col:
            st.markdown("### Section Coverage")

            if insights["detected_sections"]:
                for section in insights["detected_sections"]:
                    st.success(section.title())

            if insights["missing_sections"]:
                st.markdown("Missing")

                for section in insights["missing_sections"]:
                    st.warning(section.title())

        skill_col, keyword_col = st.columns(2)

        with skill_col:
            st.markdown("### Detected Skills")

            if insights["detected_skills"]:
                st.markdown(
                    " ".join(
                        f'<span class="pill">{skill}</span>'
                        for skill in insights["detected_skills"]
                    ),
                    unsafe_allow_html=True
                )
            else:
                st.warning("No common technical skills detected yet.")

        with keyword_col:
            st.markdown("### Top Keywords")

            if insights["top_keywords"]:
                st.markdown(
                    " ".join(
                        f'<span class="pill muted-pill">{keyword}</span>'
                        for keyword in insights["top_keywords"]
                    ),
                    unsafe_allow_html=True
                )

        st.markdown("### Priority Fixes")

        for item in insights["recommendations"]:
            st.info(item)

# ===================================================
# ATS ANALYZER
# ===================================================

elif page == "ATS Analyzer":

    render_feature_header(page)

    with st.form(
        "ats_analyzer_form",
        enter_to_submit=True
    ):
        job_description = st.text_area(
            "Paste Job Description",
            height=180,
            placeholder="Paste the role description here..."
        )

        submitted = st.form_submit_button(
            FEATURES[page]["action"],
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not st.session_state.resume_text:
            st.warning("Upload resume first")

        elif not job_description:
            st.warning("Enter job description")

        else:

            result = analyze_resume(
                st.session_state.resume_text,
                job_description
            )

            st.session_state.analysis_result = result

            score = result["ats_score"]

            score = max(
                0,
                min(
                    100,
                    int(score)
                )
            )

            st.markdown("### ATS Score")

            st.metric(
                "Score",
                f"{score}/100"
            )

            st.progress(score)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("### Matching Skills")

                for skill in result["matching_skills"]:
                    st.success(skill)

                st.markdown("### Strengths")

                for item in result["strengths"]:
                    st.info(item)

            with col2:
                st.markdown("### Missing Skills")

                for skill in result["missing_skills"]:
                    st.error(skill)

                st.markdown("### Suggestions")

                for item in result["suggestions"]:
                    st.warning(item)

# ===================================================
# RESUME CHAT
# ===================================================

elif page == "Resume Chat":

    render_feature_header(page)

    with st.form(
        "resume_chat_form",
        enter_to_submit=True
    ):
        question = st.text_input(
            "Ask a Question",
            placeholder="Example: What projects best match a Python developer role?"
        )

        submitted = st.form_submit_button(
            FEATURES[page]["action"],
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not st.session_state.resume_text:
            st.warning("Upload resume first")

        elif not question:
            st.warning("Enter a question")

        else:

            answer = ask_resume_question(
                question,
                st.session_state.resume_text
            )

            render_output(answer)

# ===================================================
# INTERVIEW GENERATOR
# ===================================================

elif page == "Interview Generator":

    render_feature_header(page)

    with st.form(
        "interview_generator_form",
        enter_to_submit=True
    ):
        jd = st.text_area(
            "Paste Job Description",
            height=180,
            placeholder="Paste the job description to tailor interview questions..."
        )

        submitted = st.form_submit_button(
            FEATURES[page]["action"],
            type="primary",
            use_container_width=True
        )

    if submitted:

        questions = generate_interview_questions(
            st.session_state.resume_text,
            jd
        )

        render_output(questions)

# ===================================================
# COVER LETTER
# ===================================================

elif page == "Cover Letter":

    render_feature_header(page)

    with st.form(
        "cover_letter_form",
        enter_to_submit=True
    ):
        jd = st.text_area(
            "Paste Job Description",
            height=180,
            placeholder="Paste the role description for a tailored cover letter..."
        )

        submitted = st.form_submit_button(
            FEATURES[page]["action"],
            type="primary",
            use_container_width=True
        )

    if submitted:

        letter = generate_cover_letter(
            st.session_state.resume_text,
            jd
        )

        render_output(letter)

# ===================================================
# SKILL GAP ANALYSIS
# ===================================================

elif page == "Skill Gap":

    render_feature_header(page)

    with st.form(
        "skill_gap_form",
        enter_to_submit=True
    ):
        target_role = st.text_input(
            "Target Role",
            placeholder="Example: Data Analyst, Backend Engineer, Product Manager"
        )

        submitted = st.form_submit_button(
            FEATURES[page]["action"],
            type="primary",
            use_container_width=True
        )

    if submitted:

        result = analyze_skill_gap(
            st.session_state.resume_text,
            target_role
        )

        render_output(result)

# ===================================================
# RESUME REWRITER
# ===================================================

elif page == "Resume Rewriter":

    render_feature_header(page)

    with st.form(
        "resume_rewriter_form",
        enter_to_submit=True
    ):
        bullet = st.text_area(
            "Paste Resume Bullet",
            height=150,
            placeholder="Paste one resume bullet to rewrite..."
        )

        submitted = st.form_submit_button(
            FEATURES[page]["action"],
            type="primary",
            use_container_width=True
        )

    if submitted:

        rewritten = rewrite_resume(
            bullet
        )

        render_output(rewritten)

# ===================================================
# LINKEDIN OPTIMIZER
# ===================================================

elif page == "LinkedIn Optimizer":

    render_feature_header(page)

    with st.form(
        "linkedin_optimizer_form",
        enter_to_submit=True
    ):
        linkedin_content = st.text_area(
            "Paste LinkedIn Content",
            height=180,
            placeholder="Paste your headline, about section, or profile draft..."
        )

        submitted = st.form_submit_button(
            FEATURES[page]["action"],
            type="primary",
            use_container_width=True
        )

    if submitted:

        optimized = optimize_linkedin(
            linkedin_content
        )

        render_output(optimized)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "AI Resume Analyzer - Streamlit + Gemini + LangChain + FAISS"
)
