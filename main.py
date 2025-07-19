
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info


def main():
    arguments = sys.argv
    print(f"{len(arguments)} number arguments provided")
    verbose = False
    query = ""

    system_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories

        All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
        """
    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
    )

    if len(arguments) < 2:
        print("ERROR: no prompt provided...\nUSAGE: main.py \"YOUR PROMPT HERE\" [--OPTION]")
        exit(1)
    elif len(arguments) > 2:
        if arguments[2] == "--verbose":
            verbose = True
            query = arguments[1]
        if arguments[1] == "--verbose":
            verbose = True
            query = arguments[2]
    elif len(arguments) == 2:
        query = arguments[1]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
    types.Content(role="user", parts=[types.Part(text=query)]),
    ]
    message = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages, 
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
        )
    
    if verbose:
        print("+++++++++++++++++++++ VERBOSE OUTPUT +++++++++++++++++++++")
        print(f"User prompt: {arguments[1]}")
        print(f"Prompt tokens: {message.usage_metadata.prompt_token_count}\nResponse tokens: {message.usage_metadata.candidates_token_count}")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    if not message.function_calls:
        return message.text
    
    for function_call_part in message.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        


if __name__ == "__main__":
    main()
