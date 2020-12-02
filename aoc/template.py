"""
Day 0


"""
import click


@click.command()
@click.option("--filename", default="input.txt")
def main(filename):
    with open(filename) as f:
        number_list = f.read()
        number_list = number_list[:-1].split("\n")

    result = hashed_search(number_list)
    print(result[0] * result[1])


if __name__ == "__main__":
    main(None)
