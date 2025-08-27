# Simple calculator program
operand = input(f"Enter your operator(+, -, *, /): ")

num1 = float(input(f"Enter your first number: "))
num2 = float(input(f"Enter your second number: "))


if operand == "+":
    ans = round(num1 + num2, 2)
    print(f"{num1} + {num2} = {ans}")
elif operand == "-":
    ans = num1 - num2
    print(f"{num1} - {num2} = {ans}")
elif operand == "*":
    ans = round(num1 * num2, 2)
    print(f"{num1} * {num2} = {ans}")
elif operand == "/":
    ans = round(num1 / num2, 2)
    print(f"{num1} / {num2} = {ans}")
else:
    print(f"{operand} is invalid!!\n")
    operand = input(f"Enter your operator(+, -, *, /): ")

