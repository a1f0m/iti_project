def count_vowels(s):
    count = 0
    for char in s:
        if char.lower() in "aeoui":
            count += 1
    return count

def find_letter_i(s):
    locations = []
    for i in range(len(s)):
        if s[i] == 'i':
            locations.append(i)
    return locations