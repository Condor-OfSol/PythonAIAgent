from . import get_file_contents, get_files_info, write_file, run_python
from google.genai import types


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_contents = types.FunctionDeclaration(
    name="get_file_contents",
    description="Reads the contents of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the file to read, relative to the working directory.",
            )
        },
    ),
)

schema_run_python = types.FunctionDeclaration(
    name="run_python_file",
    description="runs the python file passed as an argument, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
           "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to read files from, relative to the working directory.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to run, relative to the working directory.",
            ),           
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, creating it if it doesn't exist, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to write files to, relative to the working directory.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)