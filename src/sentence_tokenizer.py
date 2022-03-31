# NLTK Sentence Tokenizer

from array import array
from nltk.tokenize import sent_tokenize


def tokenize(text):
    """
    Tokenize text into sentences.
    :param text:
    :return: list of sentences"""
    tokenized_array: array = sent_tokenize(text)
    return tokenized_array
