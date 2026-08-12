import logging

from google import genai
from google.genai.errors import ClientError, ServerError

from config import GEMINI_API_KEY

from exceptions.ai_exceptions import RateLimitExceededError, ProviderUnavailableError, InvalidProviderResponseError, UnauthorizedAccessError

logger = logging.getLogger(__name__)

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(prompt: list):
    logger.info("Sending request to Gemini API")
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )
        
    except ClientError as e:
        if e.code == 429:
            raise RateLimitExceededError("Gemini API rate limit exceeded") from e
        if e.code == 401:
            raise UnauthorizedAccessError() from e
        raise
    except ServerError as e:
        raise ProviderUnavailableError("Gemini API is unavailable") from e
    if not response or response.text is None or response.model_version is None or response.usage_metadata is None:
        raise InvalidProviderResponseError("Gemini API returned an invalid response")

    logger.info("Received response from Gemini API")
    return {
                    "text": response.text,
                    "model": response.model_version,
                    "usage": {
                        "promptTokenCount": response.usage_metadata.prompt_token_count,
                        "candidatesTokenCount": response.usage_metadata.candidates_token_count,
                        "totalTokenCount": response.usage_metadata.total_token_count
                    },
                }


def ask_gemini_stream(messages: list):
    logger.info("Sending streaming request to Gemini API")
    try:
        response = client.models.generate_content_stream(
            model="gemini-3.6-flash",
            contents=messages
            )
        logger.info("Streaming response started from Gemini API")
        received_text = False
        for chunk in response:
            if chunk.text:
                received_text = True
                yield chunk.text

    except ClientError as e:
        if e.code == 429:
            raise RateLimitExceededError("Gemini API rate limit exceeded") from e
        if e.code == 401:
            raise UnauthorizedAccessError("Gemini API authentication failed. Check your API key.") from e
        raise
    except ServerError as e:
        raise ProviderUnavailableError("Gemini API is unavailable") from e

    if not received_text:
        raise InvalidProviderResponseError("Gemini API returned an empty streaming response")
    logger.info("Streaming response completed from Gemini API")