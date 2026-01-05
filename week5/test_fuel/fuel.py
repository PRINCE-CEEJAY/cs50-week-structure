def main():
    while True:
        try:
            fraction = input("What's the fraction of the gauge? ").strip()
            percentage = convert(fraction)
            print(gauge(percentage))
            break

        except ValueError:
            print("Invalid input. Try again.")

        except ZeroDivisionError:
            print("Division by zero. Try again.")

def convert(fraction):
    # Get X/Y FORMAT
    x, y = fraction.split("/")

    # convert x, y to integes
    x = int(x)
    y = int(y)

    #if  Y == 0 then raise ZeroDivisionError explicitly
    if y == 0:
        raise ZeroDivisionError

    # X > Y or negative values then ValueError
    if x > y or x < 0 or y < 0:
        raise ValueError

    # convertng to percentage
    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}"


if __name__ == "__main__":
    main()
