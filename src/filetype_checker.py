# Checks file types and returns the mime

import mimetypes

from fastapi import File


def check_file_type(filename):
    """Checks the file type of the file and returns the mime type."""
    mime = mimetypes.guess_type(filename)
    return mime[0]
