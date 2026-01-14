# Simple Calculator

# Taking inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("select operation (+, -, *, /): ")

# Performing operation 
if choice == '+':
    result = num1 + num2
    print("num1 + num2 = ", result)

elif choice == '-':
    result = num1 - num2
    print(" num1 - num2 = ", result)

elif choice == '*':
    result = num1 * num2
    print(" num1 * num2 = ", result)

elif choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("num1 / num2 = ", result)
    else:
        print("Division by zero is not allowed")

else:
    print("Invalid operation selected")
