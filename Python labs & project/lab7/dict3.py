# Input dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

print("Keys:")
for key in dict_num:
    print(key)

print("\nValues:")
for value in dict_num.values():
    print(value)

print("\nItems:")
for key, value in dict_num.items():
    print(f"Key: {key}, Value: {value}")
