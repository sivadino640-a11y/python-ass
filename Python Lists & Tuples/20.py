numbers = [25, 10, 45, 30, 60, 15]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest number:", smallest)