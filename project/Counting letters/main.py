import counting_letters

text = input("Enter a string: ")

# Use the count_vowels function
vowel_count = counting_letters.count_vowels(text)
print(f"Number of vowels: {vowel_count}")

# Use the find_letter_i function
i_locations = counting_letters.find_letter_i(text)
print(f"Positions of 'i': {i_locations}")