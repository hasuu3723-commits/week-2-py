
# Python Week 1 Assignment: Item Price Calculator

# Ask the user to enter the item price and quantity
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity you want: "))

# Calculate the total price
total = price * quantity

# Display the calculation using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")

print("Thank you!")
