"""
Day 08

# Part 01

- Given a list of asm-like instructions such as

```
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
```

- Detect an infinite loop, that is, an instruction that would be visited
  twice
- Return the value in the acumulator right `before` the loop
- The jumps are relative

- In the given example, the instructions would be visited in the following order

```
nop +0  | 1
acc +1  | 2, 8(!)
jmp +4  | 3
acc +3  | 6
jmp -3  | 7
acc -99 |
acc +1  | 4
jmp -4  | 5
acc +6  |
```

- The result right befor the 8th instruction - a repeated `acc +1` is five

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


def solve(steps):
    """
    Given a set of instructions, follows them and returns the accumulated
    value right before an infinite loop.
    """

    accumulator = 0
    visited = set()
    program_counter = 0

    while program_counter < len(steps):
        instruction = steps[program_counter]
        visited.add(program_counter)

        op, arg = instruction.split(" ")
        arg = int(arg)

        if op == "acc":
            accumulator += arg
            program_counter += 1
        elif op == "jmp":
            program_counter += arg
        else:
            program_counter += 1

        if program_counter in visited:
            # Found a jump that should be nop
            if op == "jmp":
                program_counter -= arg - 1
            # Found a nop that should be jump
            else:
                program_counter += arg

    return accumulator


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Handles input and benchmarks all the strategies
    """
    with open(filename) as f:
        steps = f.readlines()

    print(solve(steps))

    for fun in strategies:
        cprofiler(fun, steps)


if __name__ == "__main__":
    main(None)
