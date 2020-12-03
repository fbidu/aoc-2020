"""
Tests for an inifinite list
"""
from aoc import InfList


def test_inflist_init():
    """
    Can we create a new inflist?
    """
    inf = InfList([1, 2, 3])
    assert inf[0] == 1


def test_inflist_beyond_index():
    """
    Does an InfList loops around?
    """
    inf = InfList([1, 2, 3])
    assert inf[2] == 3
    assert inf[3] == 1
    assert inf[4] == 2
    assert inf[5] == 3
    assert inf[6] == 1
    assert inf[7] == 2
    assert inf[8] == 3
