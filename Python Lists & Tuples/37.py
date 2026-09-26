products = [
    ("Laptop", 50000, 2),
    ("Mouse", 500, 5),
    ("Keyboard", 1000, 3)
]

for name, price, quantity in products:
    total = price * quantity
    print(name, "Total Value:", total)