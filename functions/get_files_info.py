import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_path, directory))

        valid_target_dir = os.path.commonpath([abs_working_path, target_dir]) == abs_working_path

        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        results = []
        listing = os.listdir(target_dir)
        for item in listing:
            p = "/".join([target_dir, item])
            results.append(f"- {item}: file_size={os.path.getsize(p)}, is_dir={os.path.isdir(p)}")
    
        return "\n".join(results)
    
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
