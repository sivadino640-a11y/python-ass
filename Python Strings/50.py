str = input("Enter a string: ")
remove = input("Enter a character to remove: ")
result = ""

for ch in str:
    if ch != remove:
        result += ch

print("String after removing character:", result)