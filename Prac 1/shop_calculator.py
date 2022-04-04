no_of_items = int(input("Number of items: "))
total_price = 0
while no_of_items < 0:
    print("Invalid number of items")
    no_of_items = int(input("Number of items: "))

for i in range(0, no_of_items):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price

if total_price > 100:
    discount = 10 / 100
    total_price = total_price - (total_price * discount)

print("Total price for {} items is $ {:.2f}".format(no_of_items, total_price))