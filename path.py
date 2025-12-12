import os

def print_directory_contents(path='.'):
    """
    Print all entries (files + sub-directories) in the given directory path.
    Default is the current directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: Permission denied accessing '{path}'.")
        return

    print(f"Contents of directory '{path}':")
    for name in entries:
        print(name)

if __name__ == '__main__':
    # Example usage: you can change the path as needed
    directory_path = input("Enter directory path (leave blank for current): ").strip() or '.'
    print_directory_contents(directory_path)
