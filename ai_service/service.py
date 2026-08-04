from ai_service.gemini_service import ask_gemini, ask_gemini_stream
from ai_service.groq_service import ask_groq

from google.genai.errors import ClientError

def ask_ai(messages):
    try:
        return ask_gemini(messages)
    except ClientError as e:
        if e.code == 429:
            print("Gemini API rate limit exceeded. Falling back to Groq API.")
            return ask_groq(messages)
        raise


def ask_ai_stream(messages):
    try:
        yield from ask_gemini_stream(messages)
    except ClientError as e:
        # TODO: Add Groq streaming fallback
        raise