import os


def update_init_file():
    """Get the current directory"""
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Define the path to the utils directory
    utils_directory = os.path.join(current_directory, "utils")

    # Get a list of Python files in the utils directory
    python_files = [
        f
        for f in os.listdir(utils_directory)
        if f.endswith(".py") and f != "__init__.py"
    ]

    # Generate the import statements for each Python file
    import_statements = [
        f"from .{filename[:-3]} import {filename[:-3].capitalize()}"
        for filename in python_files
    ]

    # Construct the content to write to the __init__.py file
    init_content = "\n".join(import_statements)

    # Write the content to the __init__.py file
    with open(
        os.path.join(utils_directory, "__init__.py"), "w", encoding="utf-8"
    ) as init_file:
        init_file.write(init_content)


# Call the function to update the __init__.py file
update_init_file()
