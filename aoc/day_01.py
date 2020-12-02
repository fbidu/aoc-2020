"""
Day 01

- Given a list of numbers
- Find the two entries that sum to 2020
- Multiply those two numbers together


* All the functions assume that a solution exists.
* number_list is a list of numerical strings
"""
import cProfile
import click


def bilinear_search(number_list, target=2020):
    """
    A simple bilinear search approach to this problem, for each
    number we compute what's its complement to reach the
    target and return them both if they are present
    """
    number_list = [int(x) for x in number_list]

    for idx, n in enumerate(number_list):
        complement = target - n
        for m in number_list[idx:]:
            if m == complement:
                return n, m


def linear_search(number_list, target=2020):
    """
    As in the bilinear search, it implements a very simple
    approach but uses the `in` keyword for the second
    step.
    """
    number_list = [int(x) for x in number_list]

    for n in number_list:
        complement = target - n
        if complement in number_list:
            return n, complement


def hashed_search(number_list, target=2020):
    """
    In this approach we convert the list of numbers to a set
    and use it to determine if the complement is present
    """
    number_list = set(int(x) for x in number_list)

    for n in number_list:
        complement = target - n
        if complement in number_list:
            return n, complement


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    with open(filename) as f:
        number_list = f.read()
        number_list = number_list[:-1].split("\n")

    result = hashed_search(number_list)
    print(result[0] * result[1])

    print("Profiling Hashed Search:")
    with cProfile.Profile() as pr:
        hashed_search(number_list)
    pr.print_stats()

    print("Profiling Linear Search:")
    with cProfile.Profile() as pr:
        bilinear_search(number_list)
    pr.print_stats()

    print("Profiling Bilinear Search:")
    with cProfile.Profile() as pr:
        bilinear_search(number_list)
    pr.print_stats()


if __name__ == "__main__":
    main(None)
