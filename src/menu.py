from shopping_list import add_item, remove_list, view_list, shop_list


def show_menu():
    while True:
        print("\nMenu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Exit")

        choice = input("Choose an option 1-4: ").strip()

        if choice == "1":
            name = input("Item Name: ").strip()
            try:
                quantity = int(input("Quantity: "))
                price = float(input("Price: $"))
            except ValueError:
                print("Quantity must be a whole number and price must be a number.")
                continue
            add_item(name, quantity, price)
        elif choice == "2":
            name = input("Item to remove: ").strip()
            remove_list(name)
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    show_menu()
