
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    arguments = sys.argv
    print(f"{len(arguments)} number arguments provided")
    verbose = False
    query = ""

    if len(arguments) < 2:
        print("ERROR: no prompt provided...\nUSAGE: main.py \"YOUR PROMPT HERE\" [--OPTION]")
        exit(1)
    elif len(arguments) == 3:
        if arguments[2] == "--verbose":
            verbose = True
            query = arguments[1]
        if arguments[1] == "--verbose":
            verbose = True
            query = arguments[2]
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
    types.Content(role="user", parts=[types.Part(text=query)]),
    ]
    message = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    if verbose:
        print("+++++++++++++++++++++ VERBOSE OUTPUT +++++++++++++++++++++")
        print(f"User prompt: {arguments[1]}")
        print(f"Prompt tokens: {message.usage_metadata.prompt_token_count}\nResponse tokens: {message.usage_metadata.candidates_token_count}")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print(message.text)
        


if __name__ == "__main__":
    main()
