# test tokenizer module

import sys
from pathlib import Path


from core.tokenizer import tokenize


def test_basic_tokenization():
    tokens = tokenize("Hello World")
    words = [w for _, w in tokens]
    assert "hello" in words or "world" in words


def test_stopword_removal():
    tokens = tokenize("the cat is on the mat")
    words = [w for _, w in tokens]
    assert "the" not in words
    assert "is" not in words
    assert "on" not in words


def test_stemming():
    tokens = tokenize("running runs")
    words = [w for _, w in tokens]
    # both should stem to "run"
    assert all(w == "run" for w in words)


def test_positions_preserved():
    tokens = tokenize("cat dog bird")
    positions = [p for p, _ in tokens]
    assert positions == [0, 1, 2]


def test_positions_with_stopwords():
    # stopwords still count for position
    tokens = tokenize("the quick brown fox")
    # "the" is stopword at pos 0
    # "quick" at pos 1, "brown" at pos 2, "fox" at pos 3
    pos_word = {p: w for p, w in tokens}
    assert 0 not in pos_word  # "the" removed
    assert 1 in pos_word  # "quick"
    assert 3 in pos_word  # "fox"


def test_punctuation_removed():
    tokens = tokenize("hello, world! how's it?")
    words = [w for _, w in tokens]
    assert "hello" in words
    assert "world" in words


def test_empty_input():
    tokens = tokenize("")
    assert tokens == []


def test_only_stopwords():
    tokens = tokenize("the a an is")
    assert tokens == []


if __name__ == "__main__":
    test_basic_tokenization()
    test_stopword_removal()
    test_stemming()
    test_positions_preserved()
    test_positions_with_stopwords()
    test_punctuation_removed()
    test_empty_input()
    test_only_stopwords()
    print("✅ All tokenizer tests passed!")
