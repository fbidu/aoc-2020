"""
Day 05

# Part 02

- Given a list of seat IDs
- Find the gap of exactly 1 unit
- That is, the ID that:
    - Is NOT in the list
    - But both of its imemediate neighbors are in the list
"""

import cProfile
import click

strategies = []


def strategy(func):
    """
    A decorator that will register a function in a list of strategies
    """
    strategies.append(func)
    return func


def cprofiler(fun, *args, **kwargs):
    """
    Profiles a function `fun` through `cProfile`,
    passing `*args` and `**kwargs` to `fun`
    """
    print(f"Profiling {fun.__name__}")
    with cProfile.Profile() as pr:
        fun(*args, **kwargs)
    pr.print_stats()


def simple(passes):
    """
    A very naïve and inneficient approach that will literally allocate
    lists of 128 and 8 consecutive numbers for each row and column,
    repectively, and will use array slicing to perform the binary
    partitioning.

    The result will be the seats' IDs

    >>> simple(["FBFBBFFRLR", "BFFFBBFRRR"])
    [357, 567]
    """

    def find_seat(pass_coordinates):
        row_coordinates, column_coordinates = pass_coordinates[:7], pass_coordinates[7:]
        rows = list(range(128))

        for coordinate in row_coordinates:
            if coordinate == "F":
                rows = rows[: len(rows) // 2]
            else:
                rows = rows[len(rows) // 2 :]

        columns = list(range(8))
        for coordinate in column_coordinates:
            if coordinate == "L":
                columns = columns[: len(columns) // 2]
            else:
                columns = columns[len(columns) // 2 :]

        return rows[0], columns[0]

    seats = [find_seat(pass_) for pass_ in passes]
    return [s[0] * 8 + s[1] for s in seats]

@strategy
def brute_force(seats):
    """
    Brute-force approach to find the missing seat
    """
    for seat in seats:
        if seat + 1 not in seats and seat + 2 in seats:
            return seat + 1

    return None

@strategy
def brute_force_hashed(seats):
    """
    A hashed brute-force approach to find the missing seat
    """
    seats = set(seats)
    for seat in seats:
        if seat + 1 not in seats and seat + 2 in seats:
            return seat + 1

    return None

@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Handles input and benchmarks all the strategies
    """
    with open(filename) as f:
        passes = f.read()
        passes = passes.split("\n")

    seats = simple(passes)
    seat = brute_force(seats)
    print(seat)

    for fun in strategies:
        cprofiler(fun, seats)


if __name__ == "__main__":
    main(None)
