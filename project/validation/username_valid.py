def validate_name(name):
    if name == "":
        return False
    for char in name:
        if char.isdigit():
            return False
    return True

def email_validation(email):
    print("Validating email...      (Note: using if conditions)")
    at = False
    dot = False
    for char in email:
        if char == "@":
            at = True
        elif char == ".":
            dot = True
    if email == "":
        return False
    elif at and dot:
        if email[0] not in ['@', '.'] and email[-1] not in ['@', '.'] and "@." not in email and ".@" not in email and "@@" not in email and ".." not in email:
            return True
        else:
            return False
    else:
        return False
    
def valid_email(email):
    print("Validating email... (Note: using nested try-except-else)")
    at = False
    dot = False
    for char in email:
        if char == "@":
            at = True
        elif char == ".":
            dot = True
    try:
        if email == "":
            raise ValueError("Email is empty")
    except ValueError as e:
        print(str(e))
        return False
    try:
        if not (at and dot):
            raise ValueError("Email must contain '@' and '.'")
    except ValueError as e:
        print(str(e))
        return False
    try:
        if email[0] in ['@', '.'] or email[-1] in ['@', '.']:
            raise ValueError("Email cannot start or end with '@' or '.'")
    except ValueError as e:
        print(str(e))
        return False
    try:
        if "@." in email or ".@" in email or "@@" in email or ".." in email:
            raise ValueError("Invalid sequences in email (e.g., '@.', '.@', '@@', '..')")
    except ValueError as e:
        print(str(e))
        return False

    # 5. All checks passed
    else:
        print("Email is valid")
        return True
