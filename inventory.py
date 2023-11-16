# Initialize an empty inventory dictionary to store items
inventory = {}

# Function to add new items to the inventory
def add_item():
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: $"))
    inventory[item_name] = {'quantity': quantity, 'price': price}
    print(f"{item_name} added to inventory.")

# Function to update existing items' quantities
def update_quantity():
    item_name = input("Enter item name to update quantity: ")
    if item_name in inventory:
        new_quantity = int(input("Enter new quantity: "))
        inventory[item_name]['quantity'] += new_quantity
        print(f"Quantity updated for {item_name}.")
    else:
        print("Item not found in inventory.")

# Function to view current inventory
def view_inventory():
    print("Current Inventory:")
    for item, details in inventory.items():
        print(f"Item: {item}, Quantity: {details['quantity']}, Price: ${details['price']}")

# Function to remove items from the inventory
def remove_item():
    item_name = input("Enter item name to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from inventory.")
    else:
        print("Item not found in inventory.")

# Main menu
def main():
    while True:
        print("\n--- Grocery Store Inventory Management ---")
        print("1. Add new item")
        print("2. Update item quantity")
        print("3. View current inventory")
        print("4. Remove item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_quantity()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            print("Exiting inventory management system.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
