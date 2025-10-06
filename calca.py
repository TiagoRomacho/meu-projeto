def calculator():
    print("Simple Calculator - Addition and Subtraction")
    num1 = float(input("Enter first number: "))
    operation = input("Enter operation (+ or -): ")
    num2 = float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    else:
        print("Invalid operation. Please use + or -.")

calculator()
