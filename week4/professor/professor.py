import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        answer = x + y

        # Give user up to Three attempts
        for _ in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))

            except ValueError:
                print("EEE")
                continue

            if guess == answer:
                score += 1
                break
            else:
                print("EEE")
        else:
            # aafter 3 wrong tries, show answer
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")


def get_level():
        # only return value if level is between 1 and 3 else keep prompting
    while True:
        level = input("Level: ").strip()
        if level.isdigit() and 1 <= int(level) <= 3:
            return int(level)


def generate_integer(level):
    # Generate random digit values based on the level
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

# ensure program is run directly
if __name__ == "__main__":
    main()
