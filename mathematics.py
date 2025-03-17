def calculator():
    # Ask user for the first number
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Ask user for the operation
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation. Please enter +, -, * or /.")

    # Ask user for the second number
    while True:
        try:
            num2 = float(input("Enter the second number: "))
            if operation == '/' and num2 == 0:
                print("Cannot divide by zero. Please enter another number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Perform the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")

# Run the calculator function
calculator()

