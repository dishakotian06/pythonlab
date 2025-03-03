a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
operation = input("Choose operation(+,-,*,/):")

if operation == "+":
    print("Result:",a+b)
elif operation == "-":
    print("Result:",a-b)
elif operation == "*":
    print("Result:",a*b)
elif operation == "/":
    print("Result:",a/b if b!=0 else "cannot divide by zero")
else:
    print("Invalid operator")
