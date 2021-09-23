x = float(input("Enter the first number: "))
y = input("Enter the operator: ")
z = float(input("Enter the second number: "))
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x / z)
else:
    print("Invalid operator")
