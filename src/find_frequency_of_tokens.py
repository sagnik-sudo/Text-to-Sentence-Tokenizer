import itertools
from collections import Counter


def frequency_of_tokens(tokens, tokenize_level):
    if tokenize_level == "words":
        list_of_tokens = list(itertools.chain.from_iterable(tokens))
    else:
        list_of_tokens = tokens
    counts = Counter(list_of_tokens)
    return counts
