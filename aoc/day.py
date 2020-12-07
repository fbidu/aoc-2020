"""
Module for helpers regarding a general AOC day
"""


class Day:
    """
    A general AOC Day, comprised of inputs
    and solution strategies.
    """

    strategies = []

    def strategy(self, fun):
        self.strategies.append(fun)
        return fun
