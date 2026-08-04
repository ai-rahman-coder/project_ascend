from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(prompt: list):
   
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
    )
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

    response = client.models.generate_content_stream(
        model="gemini-3.6-flash",
        contents=messages
        )

    for chunk in response:
        if chunk.text:
            yield chunk.text



# if __name__ == "__main__":
#     for chunk in ask_gemini_stream(["Hello, how are you?"]):
#         print("chunk", chunk, end="\n", flush=True)