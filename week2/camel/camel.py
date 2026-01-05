camelCase = input("type in a camel case variable name ").strip()
snake_case = ""
for char in camelCase:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
print(snake_case)
