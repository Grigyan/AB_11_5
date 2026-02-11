class InvalidPasswordError(Exception):
    pass

def validate_password(pw):
    if len(pw) < 8:
        raise InvalidPasswordError("Too short (min 8 chars).")
    if not any(c.isdigit() for c in pw):
        raise InvalidPasswordError("Must contain a digit.")
    if not any(c.isupper() for c in pw):
        raise InvalidPasswordError("Must contain an uppercase letter.")

try:
    pwd = input("Enter password: ")
    validate_password(pwd)
    print("Password accepted.")
except InvalidPasswordError as e:
    print(f"Invalid: {e}")