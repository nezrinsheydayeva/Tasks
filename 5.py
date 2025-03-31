password = input("Enter a password: ")
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
is_long_enough = len(password) >= 8
if is_long_enough and has_upper and has_lower and has_digit:
    print("Strong password")
else:
    print("Weak password")