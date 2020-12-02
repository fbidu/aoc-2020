"""
Day 02

- Given a list of passwords like
    ```
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    .
    .
    .
    x-y char: password
    ```
- Returns how many of them are valid

A valid password is:
- Has `char` a minimum of `x` and up to `y` times
"""
import click


def parse(line):
    """
    Given a line like `1-3 a: abcde` returns the password
    rule and the line separated

    >>> parse("1-3 a: abcde")
    ['1-3 a', 'abcde']
    """
    return line.split(": ")


def brute_force(lines):
    """
    Given a list of lines as defined by the problem, returns
    a count of how many of them are valid.

    >>> brute_force(["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"])
    2
    """

    def matches(line):
        """
        Given a line like "1-3 a: abcde", does a brute force
        search to check if the pattern `1-3 a` matches.
        That is, if the letter `a` occurs 1, 2 or 3 times
        inside `abcde`.
        """
        pattern, line = parse(line)
        min_max, target_char = pattern.split()
        min_, max_ = [int(x) for x in min_max.split("-")]

        counter = 0
        for letter in line:
            if letter == target_char:
                counter += 1

        return min_ <= counter <= max_

    return sum(matches(line) for line in lines)


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Does all the cool things
    """
    with open(filename) as f:
        number_list = f.read()
        number_list = number_list.split("\n")

    print(brute_force(number_list))


if __name__ == "__main__":
    main(None)
