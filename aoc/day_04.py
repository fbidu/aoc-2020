"""
Day 0


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
def brute_force(lines):
    """
    This strategy will loop through all the lines, saving them to a list.
    Once a blank line is found, it will group the current saved lines
    in a new string and check if all of the required fields are
    present on the passport using Python's `in` operator.
    """

    def is_valid_passport(passport_lines):
        passport = " ".join(passport_lines)

        return (
            "byr" in passport
            and "iyr" in passport
            and "eyr" in passport
            and "hgt" in passport
            and "hcl" in passport
            and "ecl" in passport
            and "pid" in passport
        )

    current_passport = []
    valid_passports = 0
    for line in lines:
        if line == "\n":
            valid_passports += is_valid_passport(current_passport)
            current_passport = []

        current_passport.append(line)

    if current_passport:
        valid_passports += is_valid_passport(current_passport)

    return valid_passports


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    """
    Handles input and benchmarks all the strategies
    """
    with open(filename) as f:
        lines = f.readlines()

    result = brute_force(lines)
    print(result)

    for fun in strategies:
        cprofiler(fun, lines)


if __name__ == "__main__":
    main(None)
