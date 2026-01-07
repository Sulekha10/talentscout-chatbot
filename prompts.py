# Greeting
GREETING_MESSAGE = (
    "Hello! I am the **TalentScout Hiring Assistant**. "
    "I will collect some basic information and ask a few technical questions "
    "based on your skills for initial screening."
)

# End Message
END_MESSAGE = (
    "✅ Thank you for your time! Your responses have been recorded.\n\n"
    "Our recruitment team will review your profile and contact you if your skills match our requirements.\n"
    "We wish you the best of luck! 🚀"
)

# Fallback
FALLBACK_MESSAGE = (
    "I'm here to assist with the hiring process only. "
    "Could you please provide the requested information related to your profile?"
)

# Technical Question Prompt
TECH_QUESTION_PROMPT = """
You are an AI technical interviewer.

The candidate has declared the following tech stack:
{tech_stack}

Task:
- Generate 3 to 5 interview questions for EACH technology.
- Keep them relevant to real-world development.
- Ensure questions test both theoretical and practical understanding.
- Format clearly as a numbered list.
"""
