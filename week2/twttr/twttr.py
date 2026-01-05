# def main():
#     words = input("type in string of texts ").strip()
#     print(shorten(words))

# def shorten(words):
#     str = ""
#     for char in words:cd
#         if char not in ["A", "O", "E", "I", "U", "a", "o", "e", "i", "u"]:
#             str += char
#     return str

# if __name__ == "__main__":
#     main()

def main():
    text = input("Enter text: ").strip()
    print(shorten(text))

def shorten(text):
    return "".join(char for char in text if char.upper() not in {"A", "E", "I", "O", "U"})

if __name__ == "__main__":
    main()
