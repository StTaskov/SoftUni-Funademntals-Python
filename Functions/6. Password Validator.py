def password_validator(pasword):
    is_valid = True
    digit_counter = 0
    for elements in pasword:
        if elements.isdigit():
            digit_counter += 1
    if not 6 <= len(pasword) <= 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not pasword.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    if not digit_counter >= 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")
    return ""


password = input()
print(password_validator(password))
