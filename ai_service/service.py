import logging

from ai_service.gemini_service import ask_gemini, ask_gemini_stream
from ai_service.groq_service import ask_groq, ask_groq_stream

from google.genai.errors import ClientError

logger = logging.getLogger(__name__)

def ask_ai(messages):
    try:
        logger.info("Using Gemini Provider for AI response")
        return ask_gemini(messages)
    except ClientError as e:
        if e.code == 429:
            logger.info("Gemini API rate limit exceeded. Falling back to Groq API.")
            return ask_groq(messages)
        raise


def ask_ai_stream(messages):
    try:
        logger.info("Using Gemini Provider for AI streaming response")
        yield from ask_gemini_stream(messages)
    except ClientError as e:
        if e.code == 429:
            logger.info("Gemini API rate limit exceeded. Falling back to Groq API for streaming.")
            yield from ask_groq_stream(messages)
        else:
            raise