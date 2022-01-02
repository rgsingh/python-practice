import pytest
from src import prob84


def test_unhappy_string():
    results = prob84.seek_the_unhappy("abcdefeghhehxyzdgd")

    assert results[0][0] == 11
    assert results[0][1] == 'h'
    assert results[1][0] == 17
    assert results[1][1] == 'd'
