"""
Day 0


"""
import cProfile
import click

import re

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

    def parse_fields(passport):
        pattern = r"([a-z]{3}):([#|\w]*)"

        passport = dict(re.findall(pattern, passport))

        try:
            passport["byr"] = int(passport["byr"])
            passport["iyr"] = int(passport["iyr"])
            passport["eyr"] = int(passport["eyr"])
        except (KeyError, ValueError):
            return {}

        return passport

    def valid_numeric(passport, field, min_, max_):
        return min_ <= passport[field] <= max_

    def valid_height(passport):
        pattern = r"(\d+)(cm|in)"

        try:
            value, unit = re.findall(pattern, passport["hgt"])[0]
            value = int(value)
        except (IndexError, ValueError):
            return False

        if unit not in {"cm", "in"}:
            return False

        if unit == "cm":
            return 150 <= value <= 193

        return 59 <= value <= 76

    def valid_hair_color(passport):
        pattern = r"^#[a-f0-9]{6}$"
        return bool(re.match(pattern, passport["hcl"]))

    def valid_pid(passport):
        pattern = r"^[0-9]{9}$"
        return bool(re.match(pattern, passport["pid"]))

    def valid_eye_color(passport):
        return passport["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def is_valid_passport(passport_lines):
        passport = " ".join(passport_lines)

        fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

        if not all(field in passport for field in fields):
            return False

        passport = parse_fields(passport)

        return (
            valid_numeric(passport, "byr", 1920, 2002)
            and valid_numeric(passport, "iyr", 2010, 2020)
            and valid_numeric(passport, "eyr", 2020, 2030)
            and valid_height(passport)
            and valid_hair_color(passport)
            and valid_eye_color(passport)
            and valid_pid(passport)
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
