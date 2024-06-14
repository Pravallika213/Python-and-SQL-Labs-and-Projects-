def find_duplicates(input_list):
    count_dict = {}
    duplicates = []
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    for item, count in count_dict.items():
        if count > 1:
            duplicates.append(item)

    return duplicates
sample_list = [1, 2, 3, 4, 2, 3, 5, 6, 4, 7, 8, 8, 9]

print("Duplicate values:", find_duplicates(sample_list))
