from fastapi import UploadFile


def save_temp(fileinput: UploadFile):
    temp_directory()
    file_path = "./temp_files/" + fileinput.filename
    with open(file_path, "wb") as f:
        f.write(fileinput.file.read())
    return file_path


def temp_directory():
    import os
    import shutil

    if not os.path.exists("./temp_files"):
        os.makedirs("./temp_files")
    else:
        shutil.rmtree("./temp_files")
        os.makedirs("./temp_files")


def remove_temp_directory():
    import os
    import shutil

    if os.path.exists("./temp_files"):
        shutil.rmtree("./temp_files")
