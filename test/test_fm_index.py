from collections import Counter

import pytest

import fmindex
from fmindex import n_less_than, FMIndex
from util import find_all_overlapping


@pytest.fixture
def example_string():
    return "Tomorrow_and_tomorrow_and_tomorrow"


@pytest.fixture
def example_text():
    with open('test/ipsum.txt') as f:
        return f.read()


@pytest.fixture
def index(example_string):
    return FMIndex(example_string)


def test_create_suffix_array_naive():
    example = "abacad"
    suffix_array = fmindex.create_suffix_array_naive(example)
    expected = [0, 2, 4, 1, 3, 5]
    assert expected == suffix_array


def test_n_less_than(example_string):
    counter = Counter(example_string)
    occ_lex_lower = n_less_than(example_string)
    sorted_counts = sorted(counter.items())
    for i in range(len(sorted_counts) - 1):
        current_letter = sorted_counts[i][0]
        next_letter = sorted_counts[i + 1][0]
        current_letter_count = sorted_counts[i][1]
        diff = occ_lex_lower[next_letter] - occ_lex_lower[current_letter]
        assert current_letter_count == diff


def test_naive_find_all():
    assert len(list(find_all_overlapping("ababa", "aba"))) == 2


def test_find(example_string):
    index = FMIndex("Tomorrow_and_tomorrow_and_tomorrow")
    assert len(index.find("tomorrow")) == 2


def test_find_on_ipsum(example_text):
    index = FMIndex(example_text)
    words = example_text.split()
    distinct_words = set(words)

    naive_occurrences = {word: len(list(find_all_overlapping(example_text, word))) for word in distinct_words}
    fm_occurrences = {word: len(index.find(word)) for word in distinct_words}
    assert fm_occurrences == naive_occurrences
