"""
A custom, infinite list.
"""
from collections import UserList

# pylint:disable=too-many-ancestors
class InfList(UserList):
    """
    A list that loops infinitely through the same starting sequence

    >>> l = InfList(['a', 'b', 'c', 'd'])
    >>> l[0]
    'a'
    >>> l[3]
    'd'
    >>> l[4]
    'a'
    >>> l[5]
    'b'
    """

    def __init__(self, initlist=None):
        super().__init__(initlist=initlist)

    def __getitem__(self, i: int):
        return super().__getitem__(i % len(self))
