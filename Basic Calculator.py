def calculator():
    print("Simple Calculator")
    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if operation == 'q':
            print("Exiting Calculator...")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero.")
                    continue
                result = num1 / num2
            
            print(f"Result: {result}")
        except ValueError:
            print("Error: Please enter valid numbers.")

calculator()
