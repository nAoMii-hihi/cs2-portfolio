def calculate_total(price, quantity):
    return price * quantity

def calculate_change(payment, total):
    return payment - total

price = float(input("Enter the item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter the amount paid: "))

total = calculate_total(price, quantity)
change = calculate_change(payment, total)

print(f"The total Cost: PHP {total:.2f}")

if change >= 0:
    print(f"Change: PHP {change:.2f}")
else:
    print(f"Shortage: PHP {-change:.2f}")


#1. What does each function do?
# The calculate_total() multiplies price by quantity, and the calculate_change() subtracts total from the payment.
#2. What is the difference between the parameters price and quantity and the actual arguments passed to the function?
# Parameters are variables in a function definition, while arguments are values passed when calling a function. 
#3. Where is the returned total stored, and how is it reused?
#The returned total is stored in the variable total. It is reused to calculate the change and display the cost.
#4. Why is it useful to separate total calculation from change calculation?
# It makes the program easier to read, test, and reuse.
