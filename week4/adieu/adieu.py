import inflect

# initialize name list and inflect engine
name_list = []
engine = inflect.engine()

# continuously prompt for name until user pressess control-d
while True:
    try:
        user_input = input("").strip()
        name_list.append(user_input)

# handle controll-d press
    except EOFError:
        print(f"Adieu, adieu, to {engine.join(name_list)}")
        break
