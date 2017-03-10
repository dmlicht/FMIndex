import pytest

import fm_index
import random

END_CHAR = '$'


def split_into_reads(seq, cov=10, read_len=20, skip_size=5):
    """returns an array of simulated reads from genome sequence"""
    generated_reads = [seq[i:i + read_len] for i in range(0, len(seq) - read_len, 5) for _ in range(cov)]
    random.shuffle(generated_reads)
    return generated_reads


@pytest.fixture(scope='module')
def reads():
    with open('test_files/phiX174_genome.txt') as f:
        data = f.read()
    return split_into_reads(data, 2, 30, 10)


@pytest.fixture(scope="session")
def words():
    return ["hello", "world", "im", "david"]


@pytest.fixture
def joined_words(words):
    return END_CHAR.join(words) + END_CHAR


@pytest.fixture
def index(joined_words):
    return fm_index.FMIndex(joined_words)


def test_get_read_at_offset(words, index):
    read_starts_at = 0
    read_ends_at = -1
    for ii in range(len(words)):
        read_ends_at = read_ends_at + len(words[ii]) + 1
        rand_pos_in_read = random.randint(read_starts_at, read_ends_at)
        ith_read_from_fm = index.get_read_at_offset(rand_pos_in_read)
        assert words[ii] == ith_read_from_fm, "problem with read " + str(ii) + ":" + words[ii] + '\n' + ith_read_from_fm
        read_starts_at = read_starts_at + len(words[ii]) + 1


@pytest.skip
def test_get_nth_read(words, index):
    for ii, word in enumerate(words):
        assert index.get_nth_read(ii) == word
