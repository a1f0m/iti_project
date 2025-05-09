
# Input Validation Utility

This project provides simple Python utility functions to validate user input, particularly names and email addresses. It demonstrates basic input validation through conditional checks and structured exception handling.

---

## Functions

### 1. `validate_name(name)`
Validates a name to ensure it's not empty and does not contain any digits.

#### Parameters:
- `name` (str): The input name to validate.

#### Returns:
- `True` if valid (non-empty, no digits).
- `False` if invalid.

#### Example:
```python
validate_name("John")       # True
validate_name("John123")    # False
validate_name("")           # False
```

---

### 2. `email_validation(email)`
Validates an email address using simple `if` conditions without regular expressions. It checks for the presence and placement of `"@"` and `"."` and ensures there are no invalid sequences.

#### Parameters:
- `email` (str): The email address to validate.

#### Returns:
- `True` if the email format is valid.
- `False` if not.

#### Rules Checked:
- Email must not be empty.
- Must contain both `"@"` and `"."`.
- Cannot start or end with `"@"` or `"."`.
- Cannot contain invalid sequences like `"@."`, `".@"`, `"@@"`, or `".."`.

#### Example:
```python
email_validation("user@example.com")    # True
email_validation("user@@example.com")   # False
```

---

### 3. `valid_email(email)`
Validates an email address using **nested `try-except-else`** blocks for better error handling and readability. Each validation rule raises a specific error message if the check fails.

#### Parameters:
- `email` (str): The email address to validate.

#### Returns:
- `True` if valid.
- `False` if invalid (with printed error messages).

#### Example:
```python
valid_email("test@domain.com")      # True
valid_email("test@@domain..com")    # False, prints reason
```

---

## Purpose

This script is useful for:
- Demonstrating how to structure simple input validation functions.
- Comparing validation using `if-else` logic versus exception-based design.
- Teaching beginner programmers the use of control flow and error handling in Python.

---

## License

This code is free to use for educational and personal projects.
