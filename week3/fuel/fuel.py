# making my own custom exception for invalid division
class InvalidDivision(Exception):
     pass

while True:
    try:
        # prompt user for input
        guage_fraction = input("What's the fraction of the guage? ").strip()

        # split and convert to integer
        dividend, divisor = guage_fraction.split("/")
        dividend = int(dividend)
        divisor =  int(divisor)

        # raise an exception error when user types incorrect fraction
        if dividend > divisor  or divisor == 0 or int(guage_fraction[0:1]) < 0:
            raise InvalidDivision

        # convert to percentage
        percentage = (dividend / divisor) * 100

        # round it up to nearest whole number
        percentage = (percentage)

        # check what to print
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        elif 1 < percentage < 99:
            print(f"{percentage:.0f}%")
        break

    # catch the exceptions and notify user of the error
    except InvalidDivision:
         print("Invalid division")

    except ValueError:
        print("Invalid input. Use format X/Y with integers. Try again.")
