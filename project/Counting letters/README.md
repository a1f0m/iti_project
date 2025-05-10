
# Counting Letters in A string

This Python script provides two functions to analyze strings: counting the number of vowels and finding the positions of the letter 'i'. It demonstrates basic string manipulation and iteration.

## Functions

### `count_vowels(s)`
Counts the number of vowels (a, e, o, u, i) in a given string.

- **Input**:
    - A string `s`.

- **Output**:
    - An integer representing the number of vowels in the string.

- **Example**:
    ```python
    count_vowels("hello world")  # Output: 3
    count_vowels("Python")       # Output: 1
    ```

---

### `find_letter_i(s)`
Finds all the positions of the letter 'i' in a given string.

- **Input**:
    - A string `s`.

- **Output**:
    - A list of integers representing the indices where the letter 'i' appears.

- **Example**:
    ```python
    find_letter_i("mississippi")  # Output: [1, 4, 7, 10]
    find_letter_i("Python")       # Output: []
    ```

---

## Usage

Call the functions directly in a script:

```python
from string_analysis import count_vowels, find_letter_i

vowel_count = count_vowels("example string")
print(f"Number of vowels: {vowel_count}")

i_locations = find_letter_i("example string")
print(f"Positions of 'i': {i_locations}")
```

