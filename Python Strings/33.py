password = input("Enter your password: ") 
has_digit = any(char.isdigit() for char in password) 
print(has_digit)