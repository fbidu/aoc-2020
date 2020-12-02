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
- Has `char` at EITHER position `x-1` OR `y-1`
- That is `1-3 a: abcde` is valid because `a` is in char 0 but not on 2
- `2-9 c: ccccccccc` is invalid because `c` appears at both 1 and 8
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
    1
    """

    def matches(line):
        """
        Given a line like "1-3 a: abcde", does a brute force
        search to check if the pattern `1-3 a` matches.
        That is, if the letter `a` occurs 1, 2 or 3 times
        inside `abcde`.
        """
        pattern, line = parse(line)
        x_y, target_char = pattern.split()
        x, y = [int(z) - 1 for z in x_y.split("-")]

        # Lazy man's XOR
        # If both of those lines are False, the sum will evaluate to 0
        # If both are true, the sum will be 2
        # The sum will be 1 ONLY if exactly one of those are true
        return (line[x] == target_char) + (line[y] == target_char) == 1

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
