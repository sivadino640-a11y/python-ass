str = input("Enter a string: ")

for ch in str:
    if ch.lower() in "aeiou":
        print(ch)