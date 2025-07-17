import os


def get_files_info(working_directory, directory="."):
    directory_path = os.path.abspath(os.path.join(working_directory, directory))
    if not directory_path.startswith(os.path.abspath(working_directory)):
        err_message = f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        return err_message
    if not os.path.isdir(directory_path):
        err_message = f'Error: "{directory_path}" is not a directory'
        return err_message
    
    files = os.listdir(directory_path)
    result = []
    try:
        for file in files:
            message = f"- {file}: file_size = {os.path.getsize(os.path.join(directory_path,file))}, is_dir={os.path.isdir(os.path.join(directory_path,file))}"
            result.append(message)
        return "\n".join(result)
    except Exception as e:
        return f"ERROR: could not enumerate {directory_path}... {e}"
    
