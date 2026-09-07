string = input("Enter a string: ")

for ch in string:
    if string.count(ch) == 1:
        print("First non-repeated character:", ch)
        break
else:
    print("No non-repeated character found")