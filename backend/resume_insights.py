import re
from collections import Counter


SECTION_KEYWORDS = {
    "summary": [
        "summary",
        "profile",
        "objective"
    ],
    "skills": [
        "skills",
        "technical skills",
        "technologies"
    ],
    "experience": [
        "experience",
        "work experience",
        "employment"
    ],
    "projects": [
        "projects",
        "portfolio"
    ],
    "education": [
        "education",
        "academics"
    ],
    "certifications": [
        "certifications",
        "certificates"
    ]
}

SKILL_KEYWORDS = [
    "python",
    "java",
    "javascript",
    "typescript",
    "react",
    "node",
    "sql",
    "mongodb",
    "postgresql",
    "fastapi",
    "django",
    "flask",
    "streamlit",
    "aws",
    "azure",
    "docker",
    "kubernetes",
    "git",
    "machine learning",
    "data analysis",
    "excel",
    "power bi",
    "tableau",
    "nlp",
    "api",
    "rest"
]

ACTION_VERBS = [
    "built",
    "created",
    "developed",
    "designed",
    "implemented",
    "improved",
    "optimized",
    "automated",
    "analyzed",
    "launched",
    "managed",
    "led",
    "delivered",
    "reduced",
    "increased"
]

STOP_WORDS = {
    "the",
    "and",
    "for",
    "with",
    "from",
    "that",
    "this",
    "are",
    "was",
    "were",
    "you",
    "your",
    "resume",
    "project",
    "using",
    "work",
    "skills",
    "experience"
}


def normalize_text(text):
    return re.sub(
        r"\s+",
        " ",
        text or ""
    ).strip()


def has_section(text, aliases):
    lower_text = text.lower()

    return any(
        re.search(
            rf"(^|\n)\s*{re.escape(alias)}\s*:?",
            lower_text
        )
        for alias in aliases
    )


def extract_keywords(text, limit=12):
    words = re.findall(
        r"[a-zA-Z][a-zA-Z+#.-]{2,}",
        text.lower()
    )

    counts = Counter(
        word
        for word in words
        if word not in STOP_WORDS
    )

    return [
        word
        for word, _ in counts.most_common(limit)
    ]


def analyze_resume_insights(resume_text):
    normalized = normalize_text(resume_text)
    lower_text = normalized.lower()
    words = re.findall(
        r"\b\w+\b",
        normalized
    )
    bullet_count = len(
        re.findall(
            r"(^|\n)\s*[-*•]",
            resume_text or ""
        )
    )
    quantified_bullets = len(
        re.findall(
            r"(^|\n)\s*[-*•].*\d",
            resume_text or ""
        )
    )
    detected_sections = [
        section
        for section, aliases in SECTION_KEYWORDS.items()
        if has_section(
            resume_text or "",
            aliases
        )
    ]
    missing_sections = [
        section
        for section in [
            "summary",
            "skills",
            "experience",
            "projects",
            "education"
        ]
        if section not in detected_sections
    ]
    detected_skills = [
        skill
        for skill in SKILL_KEYWORDS
        if re.search(
            rf"\b{re.escape(skill)}\b",
            lower_text
        )
    ]
    contact_signals = {
        "email": bool(
            re.search(
                r"[\w.+-]+@[\w-]+\.[\w.-]+",
                normalized
            )
        ),
        "phone": bool(
            re.search(
                r"(\+?\d[\d\s().-]{8,}\d)",
                normalized
            )
        ),
        "linkedin": "linkedin.com" in lower_text,
        "github": "github.com" in lower_text
    }
    action_verb_hits = [
        verb
        for verb in ACTION_VERBS
        if re.search(
            rf"\b{verb}\b",
            lower_text
        )
    ]

    score = 40
    score += min(
        len(detected_sections) * 6,
        30
    )
    score += min(
        len(detected_skills) * 2,
        16
    )
    score += min(
        sum(contact_signals.values()) * 3,
        12
    )
    score += 6 if quantified_bullets else 0
    score += 6 if action_verb_hits else 0
    score = min(
        score,
        100
    )

    recommendations = []

    if missing_sections:
        recommendations.append(
            "Add missing core sections: "
            + ", ".join(missing_sections)
            + "."
        )

    if not quantified_bullets:
        recommendations.append(
            "Add numbers to impact bullets, such as users, revenue, time saved, or accuracy gained."
        )

    if len(detected_skills) < 6:
        recommendations.append(
            "Add a clearer skills section with tools, languages, frameworks, and platforms."
        )

    if not contact_signals["linkedin"]:
        recommendations.append(
            "Include a LinkedIn profile link near your contact details."
        )

    if not action_verb_hits:
        recommendations.append(
            "Start more bullets with strong action verbs like built, improved, automated, or led."
        )

    if len(words) < 250:
        recommendations.append(
            "The resume looks short; add more detail around achievements, projects, and responsibilities."
        )

    if not recommendations:
        recommendations.append(
            "The resume has a solid foundation. Fine-tune it against each job description before applying."
        )

    return {
        "overall_score": score,
        "word_count": len(words),
        "bullet_count": bullet_count,
        "quantified_bullets": quantified_bullets,
        "detected_sections": detected_sections,
        "missing_sections": missing_sections,
        "detected_skills": detected_skills,
        "contact_signals": contact_signals,
        "top_keywords": extract_keywords(
            normalized
        ),
        "recommendations": recommendations
    }
