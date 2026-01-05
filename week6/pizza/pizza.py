import sys
import csv
from tabulate import tabulate


def main():
    arg = sys.argv
    validate_arg(arg)


def validate_arg(arg):
    if len(arg) < 2:
        sys.exit("Too few command line arguments")
    elif len(arg) > 2:
        sys.exit("Too many command line arguments")
    else:
        valid_arg = arg[1]
        if valid_arg.endswith(".csv"):
            proceed_to_action(valid_arg)
        else:
            sys.exit("Not a valid CSV file")

def proceed_to_action(valid_arg):
    try:
        with open(valid_arg) as origin:
            origin_data = csv.reader(origin)
            formatted = tabulate(origin_data, headers = "firstrow", tablefmt="grid")
            print(formatted)

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
