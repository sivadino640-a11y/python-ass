s = input("Enter a sentence: ")

words = s.split()

for word in words[::-1]:
    print(word, end=" ")