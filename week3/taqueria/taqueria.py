# dictionary of food items and prices
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# variable to track running total
total = 0

while True:
    try:
        # prompt user for input
        item = input("item: ").strip()

        # track when item is found
        found = False

        for edible in menu:
            if item.title() == edible.title():
                total += menu[edible]
                print(f"Total: ${total:.2f}", end="\n")
                found = True
                break;

        # if item not in the list, just skip
        if not found:
            print("Item: ")
            break

    except EOFError:
        # Handle the end of input condition
        print(f"\nFinal Total: ${total:.2f}")
         # Exit the while loop
        break

    except ValueError:
        # Handle other potential input errors if needed
        continue
