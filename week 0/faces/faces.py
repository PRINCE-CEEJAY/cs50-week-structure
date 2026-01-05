def main():
    userInput = convert(input('please type in something '))
    print(userInput)

def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

main()
