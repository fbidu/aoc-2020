"""
Day 05

# Part 01

- Given a list of boarding passes like `FBFBBFFRLR`
- Find your seat inside a plane
- The plane is divided into rows and columns
- The boarding pass is a binary space partition

- The first 7 characters define the rows
- Starting with [0, ..., 127]
- `F` instructs you to go to the lower half, [0, ..., 63]
- `B` instructs you to go to the upper half, [32, ..., 63]
- `F` instructs you to go to the lower half, [32, ..., 47]
- `B` instructs you to go to the upper half, [40, ..., 47]
- `B` instructs you to go to the upper half, [44, ..., 47]
- `F` instructs you to go to the lower half, [44, 45]
- `F` instructs you to go to the lower half, [44], which is the row.

- The last 3 characters will be the columns
- Starting with [0, ..., 7]
- `R` instructs you to take the upper half, [4, ..., 7]
- `L` instructs you to take the lower half, [4, 5]
- `R` instructs you to take the upper half, [5], which is the line

- Finally, we have the seat's ID
    - Given by the product of the row number by 8
    - Plus the column number
- For the given example, the ID is 44 * 8 + 5 = 357
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


@strategy
def simple(passes):
    """
    A very naïve and inneficient approach that will literally allocate
    lists of 128 and 8 consecutive numbers for each row and column,
    repectively, and will use array slicing to perform the binary
    partitioning.

    The result will be the seat with maximum ID

    >>> simple(["FBFBBFFRLR", "BFFFBBFRRR"])
    567
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
    return max(s[0] * 8 + s[1] for s in seats)


@strategy
def int_pointers(passes):
    """
    This solution implements a more optimized find_seat using
    simple integers to keep track of the list's boundaries.

    The result will be the seat with maximum ID

    >>> simple(["FBFBBFFRLR", "BFFFBBFRRR"])
    567
    """

    def binary_finder(max_, instructions, min_=0, go_low="F"):
        for instruction in instructions:
            if instruction == go_low:
                max_ -= ((max_ - min_) // 2) + 1
            else:
                min_ += ((max_ - min_) // 2) + 1

        return min_

    def find_seat(pass_coordinates):
        row_coordinates, column_coordinates = pass_coordinates[:7], pass_coordinates[7:]
        row = binary_finder(127, row_coordinates)
        column = binary_finder(7, column_coordinates, go_low="L")

        return row, column

    seats = [find_seat(pass_) for pass_ in passes]
    return max(s[0] * 8 + s[1] for s in seats)

@strategy
def int_pointers_max_comprehension(passes):
    """
    This solution implements a more optimized find_seat using
    simple integers to keep track of the list's boundaries.

    The result will be the seat with maximum ID, but in this case
    I'll feed the max function the list's expression, without
    saving it to memory.

    >>> simple(["FBFBBFFRLR", "BFFFBBFRRR"])
    567
    """

    def binary_finder(max_, instructions, min_=0, go_low="F"):
        for instruction in instructions:
            if instruction == go_low:
                max_ -= ((max_ - min_) // 2) + 1
            else:
                min_ += ((max_ - min_) // 2) + 1

        return min_

    def find_seat(pass_coordinates):
        row_coordinates, column_coordinates = pass_coordinates[:7], pass_coordinates[7:]
        row = binary_finder(127, row_coordinates)
        column = binary_finder(7, column_coordinates, go_low="L")

        return row, column

    return max(seat[0] * 8 + seat[1] for s in seats)

@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Handles input and benchmarks all the strategies
    """
    with open(filename) as f:
        passes = f.read()
        passes = passes.split("\n")

    print("simple", simple(passes))
    print("int pointers", int_pointers(passes))

    for fun in strategies:
        cprofiler(fun, passes)


if __name__ == "__main__":
    main(None)
