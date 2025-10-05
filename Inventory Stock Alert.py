inventory = {
    "Apples": 45,
    "Bananas": 8,
    "Oranges": 15,
    "Milk Cartons": 5,
    "Bread Loaves": 20
}

for item, stock in inventory.items():
    if (stock<10):
        print("Low Stock Alert!",item,"have only",stock,"units left.")
