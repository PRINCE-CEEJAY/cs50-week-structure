import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if " to " not in s:
        raise ValueError

    start, end = s.split(" to ")

    start_time = convert_one(start)
    end_time = convert_one(end)

    return f"{start_time} to {end_time}"

# Helpaer function
def convert_one(t):
    parts = t.split()

    if len(parts) != 2:
        raise ValueError

    time, period = parts

    if period not in ["AM", "PM"]:
        raise ValueError

    if ":" in time:
        hour, minute = time.split(":")

        # minute must be exactly two digits
        if len(minute) != 2:
            raise ValueError
    else:
        hour = time
        minute = "00"

    # hour must be digits only
    if not hour.isdigit() or not minute.isdigit():
        raise ValueError

    # reject leadin zero hour like "09"
    if len(hour) == 2 and hour.startswith("0"):
        raise ValueError

    hour = int(hour)
    minute = int(minute)

    if hour < 1 or hour > 12:
        raise ValueError

    if minute < 0 or minute > 59:
        raise ValueError

    #Convert to 24hour format
    if period == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
