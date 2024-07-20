import re

def validate_username(username):
    if len(username) > 50:
        return False
    if len(username) == 0:
        return False
    return True

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[_@$]", password):
        return False
    return True

def validate_email(email):
    if "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    if not re.match("^[a-zA-Z0-9_.]+$", parts[0]):
        return False
    domain_parts = parts[1].split(".")
    if len(domain_parts) < 2:
        return False
    for part in domain_parts:
        if not re.match("^[a-zA-Z0-9]+$", part):
            return False
    return True

def main():
    username = input("Enter username: ")
    while not validate_username(username):
        print("Invalid username. It should not be empty and should not exceed 50 characters.")
        username = input("Enter username: ")

    password = input("Enter password: ")
    while not validate_password(password):
        print("Invalid password. It should be at least 8 characters long, contain at least one special symbol, one or more numbers, and one or more uppercase and lowercase characters.")
        password = input("Enter password: ")

    email = input("Enter email: ")
    while not validate_email(email):
        print("Invalid email. It should have alphanumeric characters before and after the @ symbol, and letters having . character in between after the @ symbol.")
        email = input("Enter email: ")

    print("Username, password, and email are valid.")

if __name__ == "__main__":
    main()
