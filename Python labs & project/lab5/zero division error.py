def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

divide_numbers(numerator, denominator)
