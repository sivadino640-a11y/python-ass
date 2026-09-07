sentence = "Python is very easy to learn"
words = sentence.split()
longest = max(words, key=len)
shortest = min(words, key=len)
print("Longest word:", longest)
print("Shortest word:", shortest)