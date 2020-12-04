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

    return None, None


@strategy
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

    return None, None


@strategy
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

    return None, None


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Handles input and benchmarks all the strategies
    """
    with open(filename) as f:
        number_list = f.read()
        number_list = number_list[:-1].split("\n")

    result = hashed_search(number_list)
    print(result[0] * result[1])

    for fun in strategies:
        cprofiler(fun, number_list)


if __name__ == "__main__":
    main(None)
