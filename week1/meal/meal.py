def main():
    # prompting user for the time
    time_str = input("What time is it? ")
    hours = convert(time_str)

    # check what time it is
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    # formatting and converting time to fraction of an hour
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()
