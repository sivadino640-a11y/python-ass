string = input("Enter a string: ")

for ch in string:
    if ch.isalpha() and ch.lower() not in "aeiou":
        print(ch)