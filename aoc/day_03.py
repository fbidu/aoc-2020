"""
Day 03

- Given a list of free and occupied spaces such as
    ```
    ..##.......
    #...#...#..
    .#....#..#.
    ..#.#...#.#
    .#...##..#.
    ..#.##.....
    .#.#.#....#
    .#........#
    #.##...#...
    #...##....#
    .#..#...#.#
    ```
- And a slope of "3 right and 1 down"
- Count how many "#" are in the path
- Each line repeats to the right as much as needed

- In the given example we have

    ```
    ..##.........##.........##.........##.........##.........##.......  --->
    #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
    .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
    ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
    .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
    ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
    .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
    .#........#.#........X.#........#.#........#.#........#.#........#
    #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
    #...##....##...##....##...#X....##...##....##...##....##...##....#
    .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#
    ```
- So we have 7 hits

"""
import click

from aoc.inf_list import InfList


def inf_list_counter(lines):
    """
    Uses an InfList to count the hits
    """
    map_ = [InfList(line) for line in lines]

    hits = 0
    for line_no, line in enumerate(map_):
        if line[line_no * 3] == "#":
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

    print(inf_list_counter(map_lines))


if __name__ == "__main__":
    main(None)
