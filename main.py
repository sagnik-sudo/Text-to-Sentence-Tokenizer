from fastapi import FastAPI, Form, UploadFile
from src.save_temporary_file import remove_temp_directory, save_temp
import src.sentence_tokenizer as st
import src.filetype_checker as fc
import src.tesseract as tess

description = """
This is a simple tool for splitting a document into sentences.

For suggestions and contributions, please visit [here](https://github.com/sagnik-sudo/Text-to-Sentence-Tokenizer/issues)

If you like my work, please star it on [here](https://github.com/sagnik-sudo/Text-to-Sentence-Tokenizer)
"""
app = FastAPI(
    title="Text to Sentence Tokenizer",
    description=description,
    version="Beta",
    docs_url="/tokenizer",
    redoc_url="/tokenizer/redoc",
    contact={
        "name": "Developer - Sagnik Das",
        "email": "sagnikdas2305@gmail.com",
    },
)


@app.post("/tokenize/text", tags=["Tokenizer"], summary="Tokenize text into sentences.")
async def tokenize_from_text(sentence: str = Form(...)):
    tokens = st.sent_tokenize(sentence)
    return {"Length": len(tokens), "Tokens": tokens}


@app.post(
    "/tokenize/file",
    tags=["Tokenizer"],
    summary="Tokenize text or image file into sentences.",
)
async def tokenize_from_file(fileinput: UploadFile):
    if fc.check_file_type(fileinput.filename).startswith("image"):
        location = save_temp(fileinput)
        text = tess.process_image(location)
    elif fc.check_file_type(fileinput.filename).startswith("text"):
        text = fileinput.file.read().decode("utf-8")
    else:
        return {"Error": "File type not supported."}

    remove_temp_directory()
    tokens = st.sent_tokenize(text)
    return {"Length": len(tokens), "Tokens": tokens}
