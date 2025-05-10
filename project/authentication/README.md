
# username_authentication

This Python script provides basic user authentication functionality. It uses a list of dictionaries to store usernames and passwords and includes two validation functions: one for usernames and one for passwords.

## Data Structure

The script uses a list of dictionaries named `userd` to store user credentials. Each dictionary contains:
- `"name"`: the username
- `"pass"`: the corresponding password

```python
userd = [
    {"name": "fekry", "pass": "1234"},
    {"name": "abdullah", "pass": "4321"},
    {"name": "ziad", "pass": "5678"},
    {"name": "ahmed", "pass": "8765"}
]
```

## Functions

### 1. `validate_user(user)`
Checks whether the provided username exists in the `userd` list.

- **Parameters**:
  - `user` (str): The username to validate.

- **Returns**:
  - `True` if the username exists, `False` otherwise.

- **Example**:
  ```python
  validate_user("ziad")  # Returns: True
  validate_user("omar")  # Returns: False
  ```

---

### 2. `validate_pass(passw)`
Checks whether the provided password exists in the `userd` list.

- **Parameters**:
  - `passw` (str): The password to validate.

- **Returns**:
  - `True` if the password exists, `False` otherwise.

- **Example**:
  ```python
  validate_pass("1234")  # Returns: True
  validate_pass("0000")  # Returns: False
  ```

---

## Usage

Import the functions and call them with the appropriate parameters:

```python
from username_authentication import validate_user, validate_pass

if validate_user("fekry") and validate_pass("1234"):
    print("Login successful")
else:
    print("Invalid credentials")
```


