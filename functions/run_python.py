import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    print(f"file: {abs_file_path} exists: {os.path.exists(abs_file_path)}")
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    result_message = ""
    try:
        
        completed_process = subprocess.run(
            ['python3', abs_file_path] + args,
            capture_output=True,
            text=True,
            cwd=abs_working_dir,
            timeout=30,
        )

        if completed_process.stdout != "":
            result_message = "STDOUT:\n" + completed_process.stdout.strip()

        if completed_process.stderr != "":
            result_message += "\nSTDERR:\n" + completed_process.stderr.strip()

        if completed_process.returncode != 0:
            result_message += f"\nError: Process exited with code {completed_process.returncode}"

        if result_message == "":
            result_message = "No output produced."

        return result_message
    except Exception as e:
        return f"Error: executing Python file: {e}"