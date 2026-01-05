greeting = input("greet me ").strip().lower()
if greeting[0:5] == "hello":
    print("$0")
elif (greeting[0:1] == "h") and (greeting[0:5] != "hello"):
    print("$20")
else:
    print("$100")
print(greeting[0:1])
