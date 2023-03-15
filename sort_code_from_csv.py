import csv
import random


def random_sort_code():
    """Return random sort code from file."""
    sort_codes = read_csv()
    return random.choice(sort_codes)[0:6]


def read_csv():
    """Read the csv file and return a list of sort codes."""
    with open("sort_codes.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row.
        return [row[0] for row in reader]
