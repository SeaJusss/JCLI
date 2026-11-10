shopping_list = [
    {"Name": "Apple", "Quantity": 3, "Price": 3.00},
    {"Name": "Egg", "Quantity": 5, "Price": 6.00},
]


# add name amount price to new dictionary in shopping_list
def add_item(name, amount, price):
    item = {"Name": name, "Quantity": amount, "Price": price}
    shopping_list.append(item)


# allows to view new dictionary in shopping_list
def view_list():
    if len(shopping_list) == 0:
        print("Your list is empty")
        return

    print(f"You have {len(shopping_list)} item(s) in your shopping list")

    for item in shopping_list:
        print(f"{item['Name']}: {item['Quantity']} x ${item['Price']}")


# allows removal or item from new dictionary in shopping_list
def remove_list(name):
    if len(shopping_list) == 0:
        print("Your shopping list is empty")
        return

    for item in shopping_list:
        if name.lower() == item["Name"].lower():
            shopping_list.remove(item)
            print(f"You have removed {name} from your shopping list")
            return
    print(f"{name} is not in your shopping list")
