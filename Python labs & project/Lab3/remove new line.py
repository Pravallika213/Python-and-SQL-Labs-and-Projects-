def remove_newlines(input_string):
    # Replace newline characters with an empty string
    cleaned_string = input_string.replace("\n", "")
    return cleaned_string

# Given string
Python_String = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove newline characters
cleaned_string = remove_newlines(Python_String)

# Print the cleaned string
print("Original String:")
print(Python_String)
print("\nCleaned String:")
print(cleaned_string)
