def calculate_total(price, quantity):
    return price * quantity

def calculate_change(payment, total):
    return payment - total

price = float(input("Enter the item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter the amount paid: "))

total = calculate_total(price, quantity)
change = calculate_change(payment, total)

print(f"The total Cost: Php {total:.2f}")

if change >= 0:
    print(f"Change: Php {change:.2f}")
else:
    print(f"Shortage: Php {-change:.2f}")
