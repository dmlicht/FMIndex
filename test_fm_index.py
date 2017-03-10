import pytest

import fm_index
from collections import Counter

from fm_index import calculate_n_occuring_lower_letters, FMIndex


@pytest.fixture
def example_string():
    return "Tomorrow_and_tomorrow_and_tomorrow"


@pytest.fixture
def example_text():
    with open('test_files/ipsum.txt') as f:
        return f.read()


@pytest.fixture
def index(text):
    return FMIndex(text)


def test_create_suffix_array_naive():
    example = "abacad"
    suffix_array = fm_index.create_suffix_array_naive(example)
    expected = [0, 2, 4, 1, 3, 5]
    assert expected == suffix_array


def test_calculate_occ_lex_lower(example_string):
    counter = Counter(example_string)
    occ_lex_lower = calculate_n_occuring_lower_letters(example_string)
    sorted_counts = sorted(counter.items())
    for i in range(len(sorted_counts) - 1):
        current_letter = sorted_counts[i][0]
        next_letter = sorted_counts[i + 1][0]
        current_letter_count = sorted_counts[i][1]
        diff = occ_lex_lower[next_letter] - occ_lex_lower[current_letter]
        assert current_letter_count == diff


def test_counts_from_get_occurrences(example_text):
    # read in data
    return

    index = fm_index.FMIndex(example_text)

    distinct_words = set(example_text.split())
    # count the words the old fashioned way
    counter = Counter()
    for word in distinct_words:
        i = 0
        while i < len(example_text):
            i = example_text.find(word, i)
            if i == -1:
                break
            counter[word] += 1
            i += 1

    # count the words using fm index
    fm_occurence_counts = {}
    for word in distinct_words:
        fm_occurence_counts[word] = len(index.occurrences(word))

    # compare!
    print(counter)
    for word in distinct_words:
        print(word)
        assert fm_occurence_counts[word] == counter[word]
