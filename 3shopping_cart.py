# 3. WAP to create a class representing a shopping cart. 
# Include methods for adding, removing & calculating total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity):
        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item, quantity):
        if item in self.items:
            if quantity >= self.items[item]["quantity"]:
                del self.items[item]
            else:
                self.items[item]["quantity"] -= quantity

    def calculate_total(self):
        total_price = sum(item_data["price"] * item_data["quantity"] for item_data in self.items.values())
        return total_price

cart = ShoppingCart()

while True:
    print("\nShopping Cart Operations:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Calculate Total Price")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        item = input("Enter the item name: ")
        price = float(input("Enter the item price: "))
        quantity = int(input("Enter the quantity: "))
        cart.add_item(item, price, quantity)
        print(f"{quantity} {item}(s) added to the cart.")

    elif choice == '2':
        item = input("Enter the item name to remove: ")
        quantity = int(input("Enter the quantity to remove: "))
        cart.remove_item(item, quantity)
        print(f"{quantity} {item}(s) removed from the cart.")

    elif choice == '3':
        total_price = cart.calculate_total()
        print(f"Total Price in the cart: ${total_price:.2f}")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
