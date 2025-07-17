import os

from . import config

def get_file_content(working_directory, file_path):

    filepath = os.path.abspath(os.path.join(working_directory, file_path))

    if not filepath.startswith(os.path.abspath(working_directory)):
        err_message = f'Error: Cannot list "{filepath}" as it is outside the permitted working directory'
        return err_message
    if not os.path.isfile(filepath):
        err_message = f'Error: "{filepath}" is not a regular file'
        return err_message
    
    try:
        with open(filepath, "r") as f:
            file_content_string = f.read(config.MAX_CHARS)
            if len(file_content_string) == config.MAX_CHARS:
                return f"{file_content_string}\n[...File\"{filepath}\" truncated at {config.MAX_CHARS} characters]"
            return file_content_string
    except Exception as e:
        return f"ERROR could not read file: {e}"
