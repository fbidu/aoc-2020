"""
Day 07

# Part 01

- Given a list of bag rules such as

```
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
```

- Count how many different outer bag colors can hold a `shiny gold` bag

- In this example there are 4 possibilities:

    - A bright white bag, which can hold your shiny gold bag directly.
    - A muted yellow bag, which can hold your shiny gold bag directly,
      plus some other bags.
    - A dark orange bag, which can hold bright white and muted yellow bags,
      either of which could then hold your shiny gold bag.
    - A light red bag, which can hold bright white and muted yellow bags,
      either of which could then hold your shiny gold bag.
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


def linear_search(rules):
    """
    Simple two-step linear search:

        1. Loops through all the rules and checks if the bag can
           directly hold a `shiny gold`
        2. For every color that can hold a `shiny gold`, count how
           many bags can hold them.
    """

    def find_holders(rules, target_color):
        """
        Returns a list of every unique bag color that can hold
        a `target_color` colored bag inside it.
        """
        holders = set()

        for line in rules:
            color, rule = line.split(" bags ")
            if target_color in rule:
                holders.add(color)

        return holders

    direct_holders = find_holders(rules, "shiny gold")
    indirect_holders = set()

    for holder in direct_holders:
        indirect_holders.update(find_holders(rules, holder))

    return len(direct_holders | indirect_holders)


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Handles input and benchmarks all the strategies
    """
    with open(filename) as f:
        rules = f.readlines()

    print(linear_search(rules))

    for fun in strategies:
        cprofiler(fun, rules)


if __name__ == "__main__":
    main(None)
