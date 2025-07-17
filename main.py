
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    arguments = sys.argv
    if len(arguments) < 1:
        print("ERROR: no prompt provided...\nUSAGE: main.py \"YOUR PROMPT HERE\"")
        exit(1)
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
    types.Content(role="user", parts=[types.Part(text=arguments[1])]),
    ]
    message = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print(f"You asked: \"{arguments[1]}\"\n")
    print(message.text)
    print(f"Prompt tokens: {message.usage_metadata.prompt_token_count}\nResponse tokens: {message.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
