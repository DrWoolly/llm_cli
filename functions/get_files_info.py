import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:

        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'


        results = []
        if directory == ".":
            directory_name = "current"
        else:
            directory_name = f"'{directory}'"

        results.append(f"Result for {directory_name} directory:")
        for contents in os.listdir(target_dir):
            target = os.path.join(target_dir, contents)
            results.append(f"- {contents}: file_size={os.path.getsize(target)} bytes, is_dir={os.path.isdir(target)}")

        return "\n".join(results)

    except Exception as e:
        return f"Error: {e}"

