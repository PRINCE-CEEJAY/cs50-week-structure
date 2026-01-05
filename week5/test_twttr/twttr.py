def main():
    text = input("Enter text: ").strip()
    print(shorten(text))

def shorten(text):
    return "".join(char for char in text if char.upper() not in {"A", "E", "I", "O"})

if __name__ == "__main__":
    main()
