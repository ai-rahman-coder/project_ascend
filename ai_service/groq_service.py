import logging

from groq import Groq
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

    logger.info("Sending request to Groq API")

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=groq_messages,
        max_completion_tokens=200
    )
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
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=groq_messages,
        max_completion_tokens=200,
        stream=True
    )
    logger.info("Received streaming response from Groq API")

    for chunk in response:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

    logger.info("Streaming response completed from Groq API")

# if __name__ == "__main__":
#     for chunk in ask_groq_stream([{"role": "user", "parts": [{"text": "Hello, how are you?"}]}]):
#         print("chunk", chunk, end="\n", flush=True)

    # print("response model dump", response.model_dump_json(),"\n")
    # print("response dir",dir(response),"\n")

    # print("response whole", response)
    # print("response text",response.output_text)
    
    # print("response model",response.model)