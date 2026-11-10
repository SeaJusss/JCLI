shop_list = [
    {"Name": "Apple", "Quantity": 3, "Price": 3.00},
    {"Name": "Egg", "Quantity": 5, "Price": 6.00},
]


# add name amount price to new dictionary in shopping_list
def add_item(name, amount, price):
    item = {"Name": name, "Quantity": amount, "Price": price}
    shop_list.append(item)


# allows to view new dictionary in shopping_list
def view_list():
    if len(shop_list) == 0:
        print("Your shopping list is empty.")
        return

    print(f"You have {len(shop_list)} item(s) in your shopping list")

    total = 0

    for item in shop_list:
        line_total = item["Quantity"] * item["Price"]
        print(f"{item['Name']}: {item['Quantity']} x ${item['Price']:.2f}")
        total += line_total

    print(f"Total price: ${total:.2f}")


# allows removal or item from new dictionary in shopping_list
def remove_list(name):
    if len(shop_list) == 0:
        print("Your shopping list is empty")
        return

    for item in shop_list:
        if name.lower() == item["Name"].lower():
            shop_list.remove(item)
            print(f"You have removed {name} from your shopping list")
            view_list()
            return
    print(f"{name} is not in your shopping list")
