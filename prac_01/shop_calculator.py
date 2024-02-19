DISCOUNT_THRESHOLD = 100
DISCOUNT = 0.1
total_price = 0
products_number = int(input("Number of items: "))
while products_number < 0:
    print("Invalid number of items!")
    products_number = int(input("Number of items: "))

for i in range(products_number):
    item_price = float(input("Price of item: "))
    while item_price < 0:
        print("Invalid price of item!")
        item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    total_price -= total_price * DISCOUNT

print(f"Total price for 3 items is ${total_price: .2f}")
