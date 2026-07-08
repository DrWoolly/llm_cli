import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY_BOOT")
MODEL = "openrouter/free"

def main():
    if not api_key:
        raise Exception("Key not found")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {
            "role": "user",
            "content": "What is the meaning of life?"
        }
    ]

    response = client.chat.completions.create(model=MODEL, messages=messages)

    if not response.usage:
        raise RuntimeError("Failed API Request")

    prompt_tokens = response.usage.prompt_tokens
    response_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens

    print(f"Prompt Tokens: {prompt_tokens}")
    print(f"Response Tokens: {response_tokens}")
    print(f"total_tokens: {total_tokens}")
    print(f"Response: {response.choices[0].message.content}")

if __name__ == "__main__":
    main()
