import random

# Get level
while True:
    level = input("Level: ").strip()
    if level.isdigit() and int(level) > 0:
        level = int(level)
        break

# generate random number
random_number = random.randint(1, level)

# get guesses
while True:
    guess = input("Guess: ").strip()
    if guess.isdigit() and int(guess) > 0:
        guess = int(guess)
    else:
        continue

    if guess < random_number:
        print("Too small!")
    elif guess > random_number:
        print("Too large!")
    else:
        print("Just right!")
        break
