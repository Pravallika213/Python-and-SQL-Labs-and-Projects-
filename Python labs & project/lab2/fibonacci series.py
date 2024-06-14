def fibonacci_series(n):
    # Initialize variables to store the first two numbers in the series
    a, b = 0, 1
    fibonacci_list = []

    while a < n:
        # Add current Fibonacci number to the list
        fibonacci_list.append(a)
        # Update Fibonacci numbers for the next iteration
        a, b = b, a + b 

    return fibonacci_list

# Generate Fibonacci series between 0 and 50
fibonacci_numbers = fibonacci_series(50)

# Print the Fibonacci series
print("Fibonacci series between 0 and 50:")
print(fibonacci_numbers)
