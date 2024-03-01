def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        print("Password is valid")
    else:
        print("Password is not valid")


password = input("Enter the Password: ")
validate_password(password)
