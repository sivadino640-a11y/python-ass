text = "i am siva"
letter = "siva"
words = text.split()
for word in words:
    if word.startswith(letter):
        print(word)