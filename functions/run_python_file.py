import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_path = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        print(f"FILE PATH: {file_path.split(".")[-1]}")

        if not valid_path:
           return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if file_path.split(".")[-1] != "py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python3", target_file]
        if args:
            command.extend(args)

        process = subprocess.run(command, text=True, timeout=30, capture_output=True)
        output_string = ""

        if process.returncode != 0:
            output_string += f"Process exited with code {process.returncode}"

        if not process.stdout and not process.stderr:
            output_string += f"No output produced"
        else:
            output_string += f"STDOUT:\n{process.stdout}STDERR:\n{process.stderr}"

        return output_string

    except Exception as e:
        return f"Error: executing pythin file: {e}"



print(run_python_file(".", "get_files_info.py"))

