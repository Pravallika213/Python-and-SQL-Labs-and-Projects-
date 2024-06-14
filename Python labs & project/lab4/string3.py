def count_cases(input_string):
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    special_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            special_count += 1

    return uppercase_count, lowercase_count, digit_count, special_count

input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
upper, lower, digits, special = count_cases(input_string)
print("UpperCase :", upper)
print("LowerCase :", lower)
print("NumberCase :", digits)
print("SpecialCase :", special)
