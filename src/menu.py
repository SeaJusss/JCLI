from shopping_list import shopping_list


def show_menu():
    is_running = True
    while is_running:
        print("\nMenu:")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


choice = input("Choose an option 1-4 : ").strip()
if choice == "1":
    input("Item Name:")
    input("Quantity:")
    input("Price:$")
elif choice == "2":
    print("You chose option 3")
elif choice == "3":
    print("You chose option 2")
elif choice == "4":
    is_running = False
else:
    print("Invalid choice. Please try again.")
