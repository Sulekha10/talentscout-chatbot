import os
from groq import Groq
from prompts import TECH_QUESTION_PROMPT

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_questions(tech_stack):
    prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack)

    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a professional technical interviewer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=400
        )

        output = chat_completion.choices[0].message.content
        questions = [q.strip() for q in output.split("\n") if q.strip()]
        return questions

    except Exception as e:
        return [f"⚠️ Groq API Error: {str(e)}"]
