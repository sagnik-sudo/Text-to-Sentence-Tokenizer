# Text to Sentence Tokenizer

## Description

This is a simple tool for splitting a document into sentences.

## Steps to start

1. Enable Virtual Environment

    ``` virtualenv venv ```

    ``` source venv/bin/activate ```

2. Install dependencies

    ``` pip install -r requirements.txt ```

3. Run the tool

    ``` uvicorn main:app --reload --port 8080 ```

4. Open the browser and go to <http://localhost:8080/tokenizer>

_You are good to go!_

## Prerequisites

1. If you are using Windows
    - Install Tesseract OCR from <https://github.com/UB-Mannheim/tesseract/wiki>
    - Install Python `3.10.4` or above from <https://www.python.org/downloads/>

2. If you are using Linux
    - Install Python `3.10.4` or above from <https://www.python.org/downloads/>
    - Modify tesseract install location inside `./src/tesseract.py`

## Maintainer

Name: [Sagnik Das](https://github.com/sagnik-sudo)

Email: [sagnikdas2305@gmail.com](sagnikdas2305@gmail.com)

## Suggestions are welcome

For suggestions and contributions, please visit [here](https://github.com/sagnik-sudo/Text-to-Sentence-Tokenizer/issues)

If you like my work, please star it on [here](https://github.com/sagnik-sudo/Text-to-Sentence-Tokenizer)
