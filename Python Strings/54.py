s = input("Enter a sentence: ")

for word in s.split():
    print(word[::-1], end=" ")