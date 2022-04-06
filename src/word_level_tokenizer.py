import nltk
from nltk.tokenize import TweetTokenizer

from src.sentence_tokenizer import tokenize

nltk.download("averaged_perceptron_tagger")


def tokenize_at_word_level(input_text):
    tokenizer_words = TweetTokenizer()
    tokens_sentences = [tokenizer_words.tokenize(t) for t in tokenize(input_text)]
    return tokens_sentences
