s = input("Enter a sentence: ")
count = 0

for i in range(len(s)):
    if s[i] == ' ':
        count += 1

print("Number of words:", count + 1)