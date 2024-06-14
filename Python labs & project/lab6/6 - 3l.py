def split_list(original_list, length_first_part):
    first_part = original_list[:length_first_part]
    second_part = original_list[length_first_part:]

    return first_part, second_part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_first_part = 3

# Split the list into two parts
first_part, second_part = split_list(original_list, length_first_part)

# Output 
print("Original list:", original_list)
print("Length of the first part of the list:", length_first_part)
print("Splitted the said list into two parts:", (first_part, second_part))
