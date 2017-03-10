import t_rank
from collections import Counter
import pytest


@pytest.fixture()
def text_blob():
    text_blob = None
    with open('tests/ipsum.txt') as f:
        text_blob = f.read()
    return text_blob.replace(' ', '_')


@pytest.fixture()
def ranks(text_blob):
    letter_counts = Counter(text_blob)
    letters = letter_counts.keys()
    return t_rank.TRank(text_blob, letters)


def test_lookup_with_no_occurences(ranks):
    assert ranks.rank_at_row('X', 10) == -1


def test_lookup_before_first_occurence(ranks):
    assert ranks.rank_at_row('s', 1) == -1


def test_lookup_at_first_occurence(ranks):
    assert ranks.rank_at_row('o', 1) == 0


def test_lookup_directly_after_first_occurence(ranks):
    assert ranks.rank_at_row('o', 2) == 0


def test_lookup_before_checkpoint(ranks):
    assert ranks.rank_at_row('m', 3) == -1


def test_lookup_at_checkpoint(ranks):
    assert ranks.rank_at_row('m', 4) == 0


def test_lookup_after_checkpoint(ranks):
    assert ranks.rank_at_row('m', 5) == 0


def test_lookup_sanity_check(ranks, text_blob):
    for i in range(1, len(text_blob)):
        c = text_blob[i]
        assert ranks.rank_at_row(c, i) == 1 + ranks.rank_at_row(c, i - 1)
