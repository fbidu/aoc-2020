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

- Count how many unique letters occurs in EVERY LINE in each group
- Return the sum of each group's count
    Handles input and benchmarks all the strategies

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
    letter, adding the new letters to a list for every *line*.

    With those lists at hand, we check which letter
    of the first list occur in every other list.

    >>> simple(["abc", "a\\nb\\nc", "ab\\nac"])
    4
    """
    result = 0

    def process_voter(voter):
        """
        Given a voter, defined by a string such as `abca`, returns
        that voter's unique votes, in this case, ['a', 'b', 'c']
        """
        unique_letters = []

        for letter in voter:
            if letter not in unique_letters:
                unique_letters.append(letter)
        return unique_letters

    for group in groups:
        voters = group.split("\n")

        votes = []

        for voter in voters:
            votes.append(process_voter(voter))

        for letter in votes[0]:
            if all(letter in vote for vote in votes[0:]):
                result += 1

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

    for fun in strategies:
        cprofiler(fun, groups)


if __name__ == "__main__":
    main(None)
