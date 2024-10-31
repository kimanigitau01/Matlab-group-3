num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sign = input("Enter the operand: ")
answer = 0

if sign == "+":
    answer = num1 + num2
elif sign == "-":
    answer = num1 - num2
elif sign == "/":
    answer = float(num1 /num2)
elif sign == "%":
    answer = num1 % num2
elif sign == "*":
    answer = num1 * num2


print(num1, sign, num2, "=", answer)