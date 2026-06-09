SKILL_GAP_PROMPT = """
Analyze the resume against the target role.

Provide:

1. Current Skills
2. Missing Skills
3. Learning Roadmap
4. Recommended Projects
5. Certifications
6. Estimated Time To Become Job Ready

Resume:
{resume}

Target Role:
{target_role}
"""