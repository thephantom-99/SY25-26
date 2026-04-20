
inventory = {}

while True:
    print("\nOptions: [1] Add Item, [2] Remove Item, [3] List, [4] Exit]")
    choice = input("Select an option (1-4): ")

    if choice == "1":
        name = input("Enter item name: ").strip().capitalize()
        qty = int(input(f"How many {name}s? "))
        inventory[name] = inventory.get(name, 0) + qty

    elif choice == "2":
        name = input("Which item would you like to remove? ").strip().capitalize()
        if name in inventory:
            del inventory[name]
            print(f"Removed {name} from inventory.")

    elif choice == "3":
        print("\n--- Current Inventory ---")
        for item, qty in inventory.items():
            print(f"- {item}: {inventory[item]}")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

