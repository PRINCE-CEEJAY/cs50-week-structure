import sys

def main():
    command_list = sys.argv
    validate_arg(command_list)
    sys.exit()

def validate_arg(command_list):
    if len(command_list) < 2:
        sys.exit("Too few command line arguments")
    elif len(command_list) > 2:
        sys.exit("Too many command line arguments")
    elif command_list[1].split(".")[1] != "py":
        sys.exit("Not a Python file")
    else:
        valid_arg = command_list[1]
        handle_io(valid_arg)

def handle_io(valid_arg):
    count = 0
    try:
        with open(valid_arg) as file:
            lines = file.readlines()
            for line in lines:
                stripped = line.strip()
                if not stripped or stripped.startswith("#") or len(line.strip()) < 1:
                    continue
                else:
                    count += 1
        print(count)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
