import os

from groq import Groq
from config import GROQ_API_KEY
from rag.rag_pipeline import build_prompt

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
You are MediAssist AI, an AI-powered healthcare assistant.

Rules:
1. Explain health topics in clear, simple language.
2. Never diagnose diseases.
3. Never prescribe medicines or dosages.
4. Encourage users to consult healthcare professionals.
5. If emergency symptoms are detected, advise immediate medical attention.
6. Use retrieved medical knowledge whenever available.
7. If the information is not available in the knowledge base, clearly state that.
8. Always end every response with the following disclaimer:

⚠️ Medical Disclaimer:
This chatbot provides educational information only and is not a substitute for professional medical advice.
"""


def get_ai_response(user_question, chat_history):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(chat_history)

    rag_prompt, sources = build_prompt(user_question)

    messages.append(
        {
            "role": "user",
            "content": rag_prompt
        }
    )

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.2,
            max_tokens=700
        )

        answer = completion.choices[0].message.content

        answer += "\n\n━━━━━━━━━━━━━━━━━━━━━━\n"

        answer += "\n📚 **References**\n"

        for source in sources:
            filename = os.path.basename(source)

            if filename == "healthcare_knowledge.txt":
                filename = "Healthcare Knowledge Base"

            answer += f"\n• {filename}"

        answer += """

━━━━━━━━━━━━━━━━━━━━━━

⚠️ **Medical Disclaimer**

This chatbot provides educational information only.

It is not intended to diagnose diseases,
prescribe medicines,
or replace professional medical advice.
"""

        return answer

    except Exception as e:
        return f"Error: {e}"
