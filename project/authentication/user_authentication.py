userd = [
    {"name": "fekry", "pass": "1234"},
    {"name": "abdullah", "pass": "4321"},
    {"name": "ziad", "pass": "5678"},
    {"name": "ahmed", "pass": "8765"}
]

def validate_user(user):
    for i in userd:
        if i["name"] == user:
            return True
    return False

def validate_pass(passw):
    for i in userd:
        if i["pass"] == passw:
            return True
    return False