
# sorting_lists

This Python script allows the user to input a list of integers and displays the sorted list in both ascending and descending order. It demonstrates basic list manipulation, user input, and sorting functionality.

## Function

### `sort_list_elements()`
Prompts the user to enter a number of elements, then reads the elements and prints them sorted in both ascending and descending order.

- **Input**:
  - The number of elements in the list.
  - Each element (entered individually).

- **Output**:
  - The list sorted in ascending order.
  - The list sorted in descending order.

- **Example**:
  ```
  Enter the number of elements: 5
  Enter the elements:
  Element 1: 12
  Element 2: 4
  Element 3: 19
  Element 4: 7
  Element 5: 2
  Ascending order: [2, 4, 7, 12, 19]
  Descending order: [19, 12, 7, 4, 2]
  ```

---

## Usage

Call the function directly in a script:

```python
from sorting_lists import sort_list_elements

sort_list_elements()
```

