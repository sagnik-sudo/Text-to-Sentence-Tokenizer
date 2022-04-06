from fastapi import FastAPI, Header, Query, Response, UploadFile, status
from src.find_frequency_of_tokens import frequency_of_tokens
from src.save_temporary_file import remove_temp_directory, save_temp
import src.sentence_tokenizer as st
import src.filetype_checker as fc
import src.tesseract as tess
import nltk
from src.word_level_tokenizer import tokenize_at_word_level

nltk.download("punkt")

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


@app.post(
    "/tokenize",
    tags=["Sentence Tokenizer App"],
    summary="Tokenize text or image file into sentences or words.",
)
async def tokenize_from_file(
    fileinput: UploadFile,
    tokenize_level: str = Query("Tokenize at level", enum=["sentence", "words"]),
    need_frequency: bool | None = Header("Need Frequency of Words/Sentences"),
    response: Response = Response,
):
    """
    Tokenize text or image file into sentences or words.

    :param fileinput: File to be tokenized

    :param tokenize_level: Tokenize at level

    :param need_frequency: Need Frequency of Words/Sentences?
    """
    try:
        if fc.check_file_type(fileinput.filename).startswith("image"):
            location = save_temp(fileinput)
            text = tess.process_image(location)
            remove_temp_directory()
        elif fc.check_file_type(fileinput.filename).startswith("text"):
            text = fileinput.file.read().decode("utf-8")
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"Error": "File type not supported."}

        match tokenize_level:
            case "sentence":
                tokens = st.sent_tokenize(text)
            case "words":
                tokens = tokenize_at_word_level(text)
        if need_frequency:
            tokens = frequency_of_tokens(tokens, tokenize_level)
        return {"Length": len(tokens), "Tokens": tokens}
    except:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"Error": "Something went wrong!"}
