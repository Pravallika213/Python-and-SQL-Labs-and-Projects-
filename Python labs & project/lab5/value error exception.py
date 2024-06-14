def get_integer_input():
    while True:
        try:
            user_input = input("Please enter an integer: ")
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")
try:
    user_integer = get_integer_input()
    print("You entered:", user_integer)
except ValueError as ve:
    print("An error occurred:", ve)
