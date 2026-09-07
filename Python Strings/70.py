sentence = "hello world python"
words = sentence.split()
for word in words:
    print(word[0].upper() + word[1:], end=" ")