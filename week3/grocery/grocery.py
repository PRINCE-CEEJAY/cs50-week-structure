def main():
    # dictionary to store user inputs
    dict = {}

    # loop to prompt and store user inputs
    while True:
        try:
            # get user input and convert to capital letters
            userInput = input("").strip()
            userInput = userInput.upper()

            # get the items and count from dictionary
            dict[userInput] = dict.get(userInput, 0) + 1

        # halt and print the results when user presses control-D
        except EOFError:
            for item in sorted(dict):
                print(dict[item], item)
            break

# ensure the file is run directly and not from an imported file
if __name__ == "__main__":
    main()
