def remove_duplicates(input_string):
    unique_chars = set()
    result = ""
    for char in input_string:
        if char not in unique_chars:
        
            unique_chars.add(char)
    
            result += char

    return result

input_string = "String and String Function"
output_string = remove_duplicates(input_string)
print("Output:", output_string)
