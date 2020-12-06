"""
Day 06

# Part 01

- Given a group of letters separated by a blank line such as

```
abc

a
b
c

ab
ac

a
a
a
a

b
```

- Count how many unique letters are there in each group
- Return the sum of each group's count

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
def simple(groups):
    """
    The simple - and inefficient - approach here is to loop through every
    letter, adding the new letters to a list and then counting them.

    >>> simple(["abc", "a\\nb\\nc", "ab\\nac"])
    9
    """
    result = 0
    for group in groups:
        letters = [letter for letter in group if letter != "\n"]
        unique_letters = []

        for letter in letters:
            if letter not in unique_letters:
                unique_letters.append(letter)

        result += len(unique_letters)

    return result


@strategy
def hashed(groups):
    """
    Using a set is a small change with a relevant performance impact

    >>> simple(["abc", "a\\nb\\nc", "ab\\nac"])
    9
    """
    result = 0
    for group in groups:
        letters = set(letter for letter in group if letter != "\n")
        result += len(letters)

    return result


@strategy
def hashed_list_exp(groups):
    """
    Using a set with list comprehension enhances the performance impact
    but with a memory cost.

    The only difference from this approach and `hashed`'s approach
    is that a full list is built before being fed to the dict

    >>> simple(["abc", "a\\nb\\nc", "ab\\nac"])
    9
    """
    result = 0
    for group in groups:
        letters = set([letter for letter in group if letter != "\n"])
        result += len(letters)

    return result


@strategy
def hashed_set_comprehension(groups):
    """
    Using a set with list comprehension enhances the performance impact
    but with a memory cost.

    The only difference from this approach and `hashed`'s approach
    is that a full list is built before being fed to the dict

    >>> simple(["abc", "a\\nb\\nc", "ab\\nac"])
    9
    """
    result = 0
    for group in groups:
        letters = {letter for letter in group if letter != "\n"}
        result += len(letters)

    return result


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Handles input and benchmarks all the strategies
    """
    with open(filename) as f:
        groups = f.read()
        groups = groups.split("\n\n")

    print("simple", simple(groups))
    print("hashed", hashed(groups))
    print("hashed_list_exp", hashed_list_exp(groups))

    for fun in strategies:
        cprofiler(fun, groups)


if __name__ == "__main__":
    main(None)
