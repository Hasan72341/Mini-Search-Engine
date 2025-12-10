# tokenize text into (position, stemmed_word)

import re
from nltk.stem import PorterStemmer


STOP_WORDS = {
    "the", "is", "a", "an", "and", "or", "of", "to", "in", "on", "for", "with"
}

stemmer = PorterStemmer()


def tokenize(text):
    # normalize and stem words

    text = text.lower()
    words = re.findall(r"[a-z0-9]+", text)

    tokens = []
    position = 0

    for word in words:
        if word in STOP_WORDS:
            position += 1
            continue

        stemmed = stemmer.stem(word)
        tokens.append((position, stemmed))
        position += 1

    return tokens
