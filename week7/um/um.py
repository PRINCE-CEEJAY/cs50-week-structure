# import re

# def main():
#     print(count(input("Text: ")))


# def count(s):
#     count = 0
#     parts = s.split(" ")
#     for word in parts:
#         if word[0:2].lower() == "um":
#             count += 1
#     return count


# if __name__ == "__main__":
#     main()

import re

def main():
    print(count(input("Text: ")))

def count(s):

    matches = re.findall(r'\bum\b', s, flags=re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()
