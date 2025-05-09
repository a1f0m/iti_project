
# Multiplication Table Generator

This project provides two functions to generate multiplication tables in Python using nested loops and nested lists. It demonstrates basic looping constructs and list manipulation.

---

## Functions

### 1. `print_multiplication_table()`
Prints a formatted multiplication table using nested `for` loops. The output is displayed directly in the terminal.

#### Description:
- Prompts the user for a number `n`.
- Prints a triangular multiplication table up to `n × n`.
- Uses formatted strings to align the output with tab spacing.

#### Example Output (for n = 3):
```
1x1=1
2x1=2	2x2=4
3x1=3	3x2=6	3x3=9
```

---

### 2. `list_multiplication_table()`
Generates a triangular multiplication table using nested lists and prints the resulting 2D list structure.

#### Description:
- Prompts the user for a number `n`.
- Constructs a list of lists where each inner list contains the results of the multiplication row.
- Useful for data storage or manipulation in code, unlike `print_multiplication_table()` which is purely for display.

#### Example Output (for n = 3):
```
[[1], [2, 4], [3, 6, 9]]
```

---

## Purpose

This script helps beginners:
- Understand how nested loops work.
- Learn to format terminal output.
- Use and manipulate nested lists in Python.


