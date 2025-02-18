menu = {
    "pizza": 40,
    "pasta": 50,
    "burger": 60,
    "salad": 70,
    "coffee": 80,
}
print("Welcome to the Python Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total = 0

# Loop to take multiple orders
while True:
    item = input("Enter the name of the item you want to order: ")
    if item in menu:
        order_total += menu[item]
        print(f"{item} has been added to your order.")
    else:
        print(f"{item} is not available. Please choose something else.")

    # Ask if they want to add another item
    another_item = input("Do you want to add another item? (Yes/No): ").strip().lower()
    if another_item == "no":
        break

# Display the total bill
print(f"Your total bill is: Rs{order_total}")