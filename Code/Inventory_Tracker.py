global inventory

class Colors:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

inventory = [["Gold", 150], ["Sword", 1], ["Shield", 2],
             ["Health Potion", 5], ["Crossbow", 1],
             ["Arrow", 20], ["Helmet", 1]]

def inv_track():
    print("\nWelcome to the Inventory Tracker!")
    print("")
    search = input("What item are you looking for? ").lower()
    for item, quantity in inventory:
        if search == item.lower():
            print(f"{item}: {quantity}")
            break
    else:
        print("Item not found in inventory.")

    yorn = input("Would you like to view the full inventory? ").lower()           
    if yorn in ("yes", "y"):
        view_inv(search)
    else:
        print("Exiting Inventory Tracker.") 


def view_inv(search=""):
    print("")
    print("---------------------------------------------------------")
    print("")
    while True:
        print("\nCurrent Inventory:")
        for item, quantity in inventory:
            item_lower = item.lower()
            if item_lower == "gold":
                color = Colors.YELLOW
            else:
                color = Colors.RESET

            if item_lower == search:
                color = Colors.GREEN

            print(f"{color}{item}: {quantity}{Colors.RESET}")

        print("\nOptions:")
        print("1. Add Item")
        print("2. Search Inventory")
        print("3. Remove Item")
        print("4. Update Quantity")
        print("5. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            item = input("Enter item name to add: ")
            quantity = int(input("Enter quantity: "))
            for inv_item in inventory:
                if inv_item[0].lower() == item.lower():
                    inv_item[1] += quantity
                    break
            else:
                inventory.append([item, quantity])
            print(f"Added {quantity} of {item}.")
        
        elif choice == "2":
            inv_track()


        elif choice == "3":
            item.lower = input("Enter item name to remove: ")
            for inv_item in inventory:
                if item == "gold":
                    print("Cannot remove Gold from inventory.")
                    break
                elif inv_item[0].lower() == item.lower():
                    inventory.remove(inv_item)
                    print(f"Removed {item}.")
                    break
            else:
                print(f"{item} not found in inventory.")

        elif choice == "4":
            item = input("Enter item name to update: ")
            quantity = int(input("Enter new quantity: "))
            for inv_item in inventory:
                if inv_item[0].lower() == item.lower():
                    inv_item[1] = quantity
                    print(f"Updated {item} to {quantity}.")
                    break
            else:
                print(f"{item} not found in inventory.")

        elif choice == "5":
            print("Exiting Inventory Tracker.")
            break

        else:
            print("Invalid option, please try again.")

inv_track()
