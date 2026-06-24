
# simple and easy calculator 
print("=== simple calculator ===")

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

print("Choose operation: * - + /")
operator = input("Enter operator: ")

if operator == "+":
    print("Result:", num1 + num2)

elif operator == "-":
    print("Result:", num1 - num2)

elif operator == "*":
    print("Result:", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero not allowed")

else:
    print("Invalid operator")