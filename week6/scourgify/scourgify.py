import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.endswith(".csv") or not output_file.endswith(".csv"):
        sys.exit("Not a CSV file")

    scourgify(input_file, output_file)


def scourgify(input_file, output_file):
    students = []

    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]

                students.append({
                    "first": first,
                    "last": last,
                    "house": house
                })

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    with open(output_file, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["first", "last", "house"]
        )
        writer.writeheader()

        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()
