import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    # Match exactly four(4) numeric parts
    if not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip):
        return False

    for part in ip.split("."):
        #reject leading zeros --- except "0"
        if len(part)> 1 and part.startswith("0"):
            return False

        if int(part) < 0 or int(part)> 255:
            return False
    return True

if __name__ == "__main__":
    main()
