text = "2 apples and 5 oranges"

numbers = ""

for char in text:
    if char.isdigit():
        numbers += char

print(numbers)