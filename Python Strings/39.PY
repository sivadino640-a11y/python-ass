string = input("Enter a string: ")

count = 0

for ch in string:
    if ch == ' ':
        count += 1

print("Number of spaces =", count)