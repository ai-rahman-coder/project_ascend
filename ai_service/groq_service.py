from openai import OpenAI
from config import GROQ_API_KEY

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
    )

def ask_groq(prompt: list):
    try:
        groq_messages = []
        for msg in prompt:
            role = msg["role"]
            if role == "model":
                role = "assistant"

            groq_messages.append({
                "role": role,
                "content": msg["parts"][0]["text"]
            })

        response = client.responses.create(
            model="openai/gpt-oss-20b",
            input=groq_messages,
            max_output_tokens=200
        )

        return {
            "text": response.output_text,
            "model": response.model,
            "usage": {
                "promptTokenCount": response.usage.input_tokens,
                "candidatesTokenCount": response.usage.output_tokens,
                "totalTokenCount": response.usage.total_tokens
            },
        }
    except Exception as e:
        print("Type Error:", type(e))
        print("Error:", e)
        return {
            "text": "Sorry, something went wrong. Please try again later.",
            "model": None,
            "usage": None,
        }



# if __name__ == "__main__":
#     print("response model dump", response.model_dump_json(),"\n")

#     print("response", response)
#     print("response text",response.output_text)
#     print("response dir",dir(response))
#     print("response model",response.model)