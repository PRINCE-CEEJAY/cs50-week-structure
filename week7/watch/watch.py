import re

def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    pattern = r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'

    match = re.search(pattern, s)
    #return the reformatted string if matched from the match group

    if match:
       return f"https://youtu.be/{match.group(1)}"

    return None




if __name__ == "__main__":
    main()
