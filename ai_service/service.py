import logging

from ai_service.gemini_service import ask_gemini, ask_gemini_stream
from ai_service.groq_service import ask_groq, ask_groq_stream

from exceptions.ai_exceptions import RateLimitExceededError, ProviderUnavailableError, InvalidProviderResponseError, UnauthorizedAccessError

logger = logging.getLogger(__name__)

def ask_ai(messages):
    try:
        logger.info("Using Gemini Provider")
        return ask_gemini(messages)
    except RateLimitExceededError:
        logger.info("Gemini rate limit exceeded. Falling back to Groq.")
        return ask_groq(messages)
    except ProviderUnavailableError:
        logger.info("Gemini provider is unavailable. Falling back to Groq.")
        return ask_groq(messages)
    except InvalidProviderResponseError:
        logger.info("Gemini returned an invalid response. Falling back to Groq.")
        return ask_groq(messages)
    except UnauthorizedAccessError:
        logger.error("Gemini API authentication failed. Check your API key. Falling back to Groq.")
        return ask_groq(messages)


def ask_ai_stream(messages):
    try:
        logger.info("Using Gemini Provider for streaming")
        yield from ask_gemini_stream(messages)
    except RateLimitExceededError:
        logger.info("Gemini API rate limit exceeded. Falling back to Groq streaming.")
        yield from ask_groq_stream(messages)
    except ProviderUnavailableError:
        logger.info("Gemini provider is unavailable. Falling back to Groq streaming.")
        yield from ask_groq_stream(messages)
    except InvalidProviderResponseError:
        logger.info("Gemini returned an invalid streaming response. Falling back to Groq streaming.")
        yield from ask_groq_stream(messages)
    except UnauthorizedAccessError:
        logger.error("Gemini API authentication failed. Check your API key. Falling back to Groq streaming.")
        yield from ask_groq_stream(messages)