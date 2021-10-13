import os


def read_file(file_path):
    """Read file content on file_path."""
    fd = open(file_path, 'r')
    content = fd.read()
    fd.close()

    return content


def read_files(folder):
    """List all files from selected folder."""
    filenames = next(
        os.walk(folder),
        (None, None, []))[2]
    return filenames
