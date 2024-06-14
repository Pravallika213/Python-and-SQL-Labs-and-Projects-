def count_and_display_vowels(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    vowel_list = []

    # Iterate through each character in the text
    for char in text:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1
            vowel_list.append(char)

    # Print the count of vowels and the list of vowels
    print("Number of vowels:", vowel_count)
    print("Vowels in the text:", ", ".join(vowel_list))

# Given text
text = "Welcome to python Training"

# Count and display vowels
count_and_display_vowels(text)
