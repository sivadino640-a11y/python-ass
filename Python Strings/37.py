text = input("Enter a string: ") 
count = 0 
for char in text: 
    if char.isalpha() and char.lower() not in "aeiou": 
        count += 1 
print("Number of consonants:", count)