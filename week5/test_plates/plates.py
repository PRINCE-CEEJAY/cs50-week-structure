def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Length must be between 2 and 6
    if not (1 <= len(s) <= 6):
        return False

    # Rule 2: First two characters must be letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Rule 3: No punctuation, spaces, periods
    if not s.isalnum():
        return False

    # Rule 4 & 5: Numbers can ONLY be at the end,
    # and the first number cannot be '0'.
    number_started = False

    for char in s:
        if char.isdigit():
            if not number_started:
                # This is the FIRST digit, check for leading zero
                if char == "0":
                    return False
                number_started = True
        else:
            if number_started:
                # Letter appearing after numbers:  invalid
                return False
    return True

if __name__ == "__main__":
    main()
