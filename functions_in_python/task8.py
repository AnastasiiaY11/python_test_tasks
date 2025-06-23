# Input data
words = ["apple", "banana", "cherry", "apricot", "blueberry"]
target_letter = "a"

# Using filter with lambda to get words starting with target letter
filtered_words = list(filter(lambda word: word.startswith(target_letter), words))

# Print the results
print(f"Original words: {words}")
print(f"Words starting with '{target_letter}': {filtered_words}")

# Additional tests with different letters and words
test_words = ["python", "programming", "practice", "code", "project"]
test_letters = ["p", "c"]

for letter in test_letters:
    result = list(filter(lambda word: word.startswith(letter), test_words))
    print(f"\nWords starting with '{letter}': {result}")
