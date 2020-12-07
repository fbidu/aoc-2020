"""
General tests for an AOC `Day`
"""


from aoc import Day


class DayX(Day):
    @strategy  # <== brute_force vai ser adicionado à self.strategies
    def brute_force(self):
        return "potato"
