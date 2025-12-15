# test proximity module

import sys
from pathlib import Path


from core.proximity import min_distance, proximity_score


def test_min_distance_basic():
    result = min_distance([10, 40, 90], [12, 43, 95])
    assert result == 2  # |10-12| = 2


def test_min_distance_exact_match():
    result = min_distance([5, 10, 15], [10, 20, 30])
    assert result == 0  # both have 10


def test_min_distance_far_apart():
    result = min_distance([1, 2, 3], [100, 200, 300])
    assert result == 97  # |3-100| = 97


def test_min_distance_single_elements():
    result = min_distance([5], [10])
    assert result == 5


def test_proximity_score_adjacent():
    # terms at positions 10, 11, 12 -> very close
    result = proximity_score([[10], [11], [12]])
    assert result == 2  # (11-10) + (12-11) = 2


def test_proximity_score_far():
    result = proximity_score([[10], [50], [100]])
    assert result == 90  # (50-10) + (100-50) = 90


def test_proximity_score_single_term():
    result = proximity_score([[10, 20, 30]])
    assert result == 0  # only one term


def test_proximity_score_empty():
    result = proximity_score([])
    assert result == 0


def test_proximity_score_two_terms():
    result = proximity_score([[5, 15], [8, 20]])
    assert result == 3  # min(|5-8|, |15-8|, |5-20|, |15-20|) = 3


if __name__ == "__main__":
    test_min_distance_basic()
    test_min_distance_exact_match()
    test_min_distance_far_apart()
    test_min_distance_single_elements()
    test_proximity_score_adjacent()
    test_proximity_score_far()
    test_proximity_score_single_term()
    test_proximity_score_empty()
    test_proximity_score_two_terms()
    print("✅ All proximity tests passed!")
