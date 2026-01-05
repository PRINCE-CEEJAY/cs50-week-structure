expression = input("Enter basic math: ")

left_num, operator, right_num = expression.split()
left_num = int(left_num)
right_num = int(right_num)

match(operator):
    case "+":
        result = left_num + right_num
    case "-":
        result = left_num - right_num
    case "*":
        result = left_num * right_num
    case "/":
        result = left_num / right_num
    case _:
        result = ""

print(f"{result:.1f}")
