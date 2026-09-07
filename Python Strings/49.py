string = input("Enter a string: ")

for ch in string:
    if string.count(ch) > 1:
        print("First repeated character:", ch)
        break
else:
    print("No repeated character found")