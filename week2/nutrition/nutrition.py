# build the fruit dictionary
fruits_dict = { 'Apple': 130,
               'Avocado': 50,
               'Banana': 110,
               'Cantaloupe': 50,
               'Grapefruit': 60,
               'Grapes': 90,
               'Honeydew Melon': 50,
               'Kiwifruit': 90,
               'Lemon': 15,
               'Lime': 20,
               'Nectarine': 60,
               'Peach': 60,
               'Pear': 100,
               'Pineapple': 50,
               'Plums': 70,
               'Strawberries': 50,
               'Sweet Cherries': 100,
               'Tangerine': 50,
               'Watermelon': 80
               }
# get user's choice of fruit
fruit_input = input('Enter Fruit: ').strip()

# go through the dictionary and print the value of whatever if the key matches users input formatted
for fruit in fruits_dict:
    if fruit.title() == fruit_input.title():
        print(f"Calories: {fruits_dict[fruit]}")



