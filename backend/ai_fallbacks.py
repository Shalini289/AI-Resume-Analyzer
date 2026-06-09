def format_ai_unavailable(reason):

    return (
        "AI generation is temporarily unavailable. "
        f"{reason} "
        "You can retry after the quota resets, or use the draft below."
    )


def is_quota_error(error):

    message = str(error).lower()

    return (
        "resourceexhausted" in message
        or "429" in message
        or "quota" in message
        or "rate-limit" in message
        or "rate limit" in message
    )


def get_error_message(error):

    if is_quota_error(error):
        return "Gemini API quota or rate limit was reached."

    return "The AI provider returned an error."


def safe_generate_text(
    get_model,
    prompt,
    fallback
):

    try:
        response = get_model().generate_content(
            prompt
        )

        return response.text

    except Exception as error:
        return (
            f"{format_ai_unavailable(get_error_message(error))}\n\n"
            f"{fallback}"
        )


def interview_fallback():

    return """
### HR Questions
1. Tell me about yourself and your career goals.
2. Why are you interested in this role?
3. What strengths would you bring to this team?
4. Describe a challenge you handled in a project or internship.
5. Where do you want to grow next?

### Technical Questions
1. Walk through the most relevant project on your resume.
2. What tools, languages, or frameworks did you use most?
3. How would you debug a production issue?
4. How do you design an API or feature from requirements?
5. How do you test your work before delivery?
6. Explain a technical decision you made and its tradeoffs.
7. How do you optimize performance in an application?
8. How do you handle data validation and errors?
9. What would you improve in your recent project?
10. How do you learn a new technology quickly?

### Project Questions
1. What problem did your strongest project solve?
2. What was your individual contribution?
3. What was the hardest technical part?
4. How did you measure success?
5. What would you build next?
"""


def cover_letter_fallback():

    return """
Dear Hiring Manager,

I am excited to apply for this role. My resume reflects hands-on experience building projects, solving technical problems, and learning quickly across modern tools and workflows. I am especially interested in contributing to a team where I can apply my skills, strengthen product outcomes, and keep growing through practical challenges.

In my recent work, I have focused on creating useful, well-structured solutions and communicating technical ideas clearly. I bring curiosity, ownership, and a practical approach to improving systems and user experiences.

Thank you for considering my application. I would welcome the opportunity to discuss how my background aligns with your team’s needs.

Sincerely,
Candidate
"""


def rewrite_fallback(bullet_point):

    bullet = bullet_point.strip() or "Completed assigned project work."

    return (
        "Improved resume bullet:\n\n"
        f"- Delivered {bullet[0].lower() + bullet[1:]} with a focus on measurable impact, "
        "clear execution, and business value."
    )


def skill_gap_fallback():

    return """
### Current Skill Review
- Identify the strongest tools, languages, frameworks, and projects already present in the resume.
- Prioritize skills that appear directly in the target role.

### Missing Skills
- Add role-specific tools mentioned repeatedly in job descriptions.
- Strengthen project proof for the top 3 required skills.

### Learning Roadmap
1. Review 5-8 job descriptions for the target role.
2. List recurring technical and soft skills.
3. Build one focused project that demonstrates the biggest missing skill.
4. Add quantified outcomes to the resume.
5. Re-run ATS analysis against a real job description.

### Recommended Projects
- Role-specific dashboard, API, automation, or case study.
- Portfolio project with a clear problem, tools used, and measurable result.

### Certifications
- Choose certifications only when they match the target role and strengthen credibility.
"""


def linkedin_fallback():

    return """
### Improved Headline
Aspiring professional | Project-focused learner | Building practical, user-centered solutions

### About Section Direction
Open with your target role, strongest skills, and the types of problems you enjoy solving. Add 2-3 proof points from projects, internships, or measurable outcomes.

### Skill Recommendations
- Add role-specific technical skills.
- Pin your strongest project or portfolio link.
- Keep your top skills aligned with the jobs you are applying for.

### Networking Suggestions
- Connect with recruiters and professionals in your target role.
- Comment thoughtfully on posts related to your industry.
- Share short project updates that show your learning and execution.
"""
