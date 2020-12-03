"""
Day 03 - pt2

- Now we have the same problem as part 1 but with five different slopes:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

- Return the product of all the hits of each slope


"""
import click

from aoc.inf_list import InfList


def inf_list_counter(
    lines,
    right_step=3,
    down_step=1,
):
    """
    Uses an InfList to count the hits
    """
    map_ = [InfList(line) for line in lines]

    hits = 0
    for line_no, line in enumerate(map_[::down_step]):
        if line[line_no * right_step] == "#":
            hits += 1

    return hits


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Does all the cool things
    """
    with open(filename) as f:
        map_lines = f.read()
        map_lines = map_lines.split("\n")

    one_one = inf_list_counter(map_lines, 1, 1)
    three_one = inf_list_counter(map_lines, 3, 1)
    five_one = inf_list_counter(map_lines, 5, 1)
    seven_one = inf_list_counter(map_lines, 7, 1)
    one_two = inf_list_counter(map_lines, 1, 2)
    print(one_one * three_one * five_one * seven_one * one_two)


if __name__ == "__main__":
    main(None)
