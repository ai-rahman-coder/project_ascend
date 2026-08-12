import logging

from groq import Groq
from groq import RateLimitError, InternalServerError, AuthenticationError

from exceptions.ai_exceptions import RateLimitExceededError, ProviderUnavailableError, InvalidProviderResponseError, UnauthorizedAccessError

from config import GROQ_API_KEY

logger = logging.getLogger(__name__)

client = Groq(api_key=GROQ_API_KEY)

def ask_groq(prompt: list):
    groq_messages = []
    for msg in prompt:
        role = msg["role"]
        if role == "model":
            role = "assistant"

        groq_messages.append({
            "role": role,
            "content": msg["parts"][0]["text"]
        })
    try:
        logger.info("Sending request to Groq API")
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=groq_messages,
            max_completion_tokens=200
        )
    except RateLimitError as e:
        raise RateLimitExceededError("Groq API rate limit exceeded") from e
    except InternalServerError as e:
        raise ProviderUnavailableError("Groq API is unavailable") from e
    except AuthenticationError as e:
        raise UnauthorizedAccessError("Groq API authentication failed. Check your API key.") from e
    if not response or response.choices[0].message.content is None or response.model is None or response.usage is None:
        raise InvalidProviderResponseError("Groq API returned an invalid response")

    logger.info("Received response from Groq API")

    return {
        "text": response.choices[0].message.content,
        "model": response.model,
        "usage": {
            "promptTokenCount": response.usage.prompt_tokens,
            "candidatesTokenCount": response.usage.completion_tokens,
            "totalTokenCount": response.usage.total_tokens
        },
    }


def ask_groq_stream(messages: list):
    groq_messages = []
    for msg in messages:
        role = msg["role"]
        if role == "model":
            role = "assistant"

        groq_messages.append({
            "role": role,
            "content": msg["parts"][0]["text"]
        })
    logger.info("Streaming response started from Groq API")
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=groq_messages,
            max_completion_tokens=200,
            stream=True
        )
    except RateLimitError as e:
        raise RateLimitExceededError("Groq API rate limit exceeded") from e
    except InternalServerError as e:
        raise ProviderUnavailableError("Groq API is unavailable") from e
    logger.info("Received streaming response from Groq API")
    received_text = False
    for chunk in response:
        if chunk.choices[0].delta.content:
            received_text = True
            yield chunk.choices[0].delta.content

    if not received_text:
        raise InvalidProviderResponseError("Groq API returned an empty streaming response")

    logger.info("Streaming response completed from Groq API")