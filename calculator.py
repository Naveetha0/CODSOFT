def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt user for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Prompt user for operation
    operation = input("Choose operation (+, -, *, /): ")

    # Perform calculation
    if operation == '+':
        a = num1 + num2
        print(f"a = {num1} + {num2} = {a}")
    elif operation == '-':
        b = num1 - num2
        print(f"b = {num1} - {num2} = {b}")
    elif operation == '*':
        c = num1 * num2
        print(f"c = {num1} * {num2} = {c}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is undefined.")
        else:
            d = num1 / num2
            print(f"d = {num1} / {num2} = {d}")
    else:
        print("Invalid operation choice. Please select +, -, *, or /.")

if __name__ == "__main__":
    calculator()
