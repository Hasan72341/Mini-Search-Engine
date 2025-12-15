# test intersection module

import sys
from pathlib import Path


from core.intersection import intersect_two_lists, intersect_many_lists


def test_two_lists_basic():
    result = intersect_two_lists([1, 3, 5, 7], [3, 4, 5, 8])
    assert result == [3, 5]


def test_two_lists_no_overlap():
    result = intersect_two_lists([1, 2, 3], [4, 5, 6])
    assert result == []


def test_two_lists_full_overlap():
    result = intersect_two_lists([1, 2, 3], [1, 2, 3])
    assert result == [1, 2, 3]


def test_two_lists_empty():
    result = intersect_two_lists([], [1, 2, 3])
    assert result == []


def test_many_lists_basic():
    result = intersect_many_lists([[1, 2, 3, 4], [2, 3], [3, 4, 5]])
    assert result == [3]


def test_many_lists_no_common():
    result = intersect_many_lists([[1, 2], [3, 4], [5, 6]])
    assert result == []


def test_many_lists_single():
    result = intersect_many_lists([[1, 2, 3]])
    assert result == [1, 2, 3]


def test_many_lists_empty():
    result = intersect_many_lists([])
    assert result == []


def test_many_lists_all_common():
    result = intersect_many_lists([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    assert result == [1, 2, 3]


if __name__ == "__main__":
    test_two_lists_basic()
    test_two_lists_no_overlap()
    test_two_lists_full_overlap()
    test_two_lists_empty()
    test_many_lists_basic()
    test_many_lists_no_common()
    test_many_lists_single()
    test_many_lists_empty()
    test_many_lists_all_common()
    print("✅ All intersection tests passed!")
