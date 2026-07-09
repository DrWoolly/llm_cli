import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY_BOOT")
MODEL = "openrouter/free"

def main():
    if not api_key:
        raise Exception("Key not found")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()


    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {
            "role": "user",
            "content": args.user_prompt
        }
    ]

    response = client.chat.completions.create(model=MODEL, messages=messages)

    if not response.usage:
        raise RuntimeError("Failed API Request")

    if args.verbose:
        prompt_tokens = response.usage.prompt_tokens
        response_tokens = response.usage.completion_tokens
        total_tokens = response.usage.total_tokens

        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
        print(f"Total tokens: {total_tokens}")

    print(f"Response: {response.choices[0].message.content}")

if __name__ == "__main__":
    main()
