from PIL import Image
import pytesseract


def process_image(image, lang_code="eng"):
    """Processes an image and returns the text in it.
    :param image: Image object
    :param lang_code: Language code for tesseract
    :return: Text in the image"""
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:/Users/sagni/AppData/Local/Programs/Tesseract-OCR/tesseract.exe"
    )
    return pytesseract.image_to_string(Image.open(image), lang=lang_code)
