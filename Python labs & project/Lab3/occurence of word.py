def count_word_occurrences(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create an empty dictionary to store word occurrences
    word_count = {}

    # Iterate through each word in the sentence
    for word in words:
        # Remove punctuation marks if any
        word = word.strip(",.!?'\"")

        # Convert the word to lowercase to avoid case sensitivity
        word = word.lower()

        # If the word is already in the dictionary, increment its count
        if word in word_count:
            word_count[word] += 1
        else:
            # If the word is not in the dictionary, add it with count 1
            word_count[word] = 1

    return word_count

# Given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Count occurrences of each word
word_occurrences = count_word_occurrences(sentence)

# Print the word occurrences
for word, count in word_occurrences.items():
    print(f"'{word}': {count}")
