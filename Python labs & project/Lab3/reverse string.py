def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()

    # Reverse the order of words
    reversed_words = words[::-1]

    # Join the reversed words back into a string
    reversed_string = " ".join(reversed_words)

    return reversed_string

# Given string
String = "Deeptech Python Training"

# Reverse the words in the string
reversed_string = reverse_words(String)

# Print the reversed string
print("Original String:")
print(String)
print("\nReversed String:")
print(reversed_string)
