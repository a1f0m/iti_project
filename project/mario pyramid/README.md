
# printing_pyramids

This Python script provides two methods for generating and displaying a pyramid pattern using a specified height. It demonstrates two different approaches: direct printing using nested loops, and constructing a pyramid as a list of strings.

## Functions

### 1. `print_pyramid(h)`
Prints a left-aligned pyramid directly to the console using nested loops.

- **Parameters**:
  - `h` (int): The height of the pyramid.

- **Output**:
  - Prints the pyramid to the console line by line.

- **Example**:
  ```python
  print_pyramid(4)
  ```
  Output:
  ```
  printing pyramid using nested loops
     *
    **
   ***
  ****
  ```

---

### 2. `pyramid_list(h)`
Generates a left-aligned pyramid and stores each line as a string in a list.

- **Parameters**:
  - `h` (int): The height of the pyramid.

- **Returns**:
  - A list of strings, each representing a line in the pyramid.

- **Example**:
  ```python
  lines = pyramid_list(3)
  for line in lines:
      print(line)
  ```
  Output:
  ```
  printing pyramid using list
    *
   **
  ***
  ```

---

## Usage

To use this module, simply import it and call either of the functions with your desired height:

```python
from printing_pyramids import print_pyramid, pyramid_list

print_pyramid(5)
pyramid_lines = pyramid_list(5)
for line in pyramid_lines:
    print(line)
```

---

## Notes

- The pyramid is left-aligned and padded with spaces for proper formatting.