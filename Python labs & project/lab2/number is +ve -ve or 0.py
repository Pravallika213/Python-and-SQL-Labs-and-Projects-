def check_number():
    # Take user input
    number = float(input("Enter a number: "))  
    #control statements
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

check_number()
