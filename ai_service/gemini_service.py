import logging

from google import genai
from config import GEMINI_API_KEY

logger = logging.getLogger(__name__)

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(prompt: list):
    logger.info("Sending request to Gemini API")
   
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )

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
    response = client.models.generate_content_stream(
        model="gemini-3.6-flash",
        contents=messages
        )
    logger.info("Streaming response started from Gemini API")
    for chunk in response:
        if chunk.text:
            yield chunk.text

    logger.info("Streaming response completed from Gemini API")



# if __name__ == "__main__":
#     for chunk in ask_gemini_stream(["Hello, how are you?"]):
#         print("chunk", chunk, end="\n", flush=True)