def count_chars_digits_symbols(input_string):
    chars = 0
    digits = 0
    symbols = 0

    for char in input_string:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1

    return chars, digits, symbols

input_string = "P@#yn26at^&i5ve"
chars, digits, symbols = count_chars_digits_symbols(input_string)
print("Chars =", chars, "Digits =", digits, "Symbol =", symbols)
