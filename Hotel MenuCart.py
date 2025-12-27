#Define the Menu of the Restaurant
menu = {
    'Pizza': 40,
    'Burger': 50,
    'Coffee': 15,
    'Pasta': 60,
    'Dosa': 60,
}
print("Welcome to Naveen's Restaurant")
print("Pizza : Rs.40\nBurger : Rs.50\nCoffee : Rs.15\nPasta : Rs.60\nDosa : Rs.60")
Order_total=0
Item_1 = input("Enter the name of item you want to order : ")
if Item_1 in menu:
    order_total = menu[Item_1] #50+0
    print(f"Your item {Item_1} has been added to your order")
else:
    print(f"Ordered item {Item_1} is not avaliable yet sorry !")
another_order = input("Do you want to order another item ? (Yes/No)")
if another_order == "Yes":
    Item_2 = input("ENter the name of second item : ")
    if Item_2 in menu:
        order_total += menu[Item_2]
        print(f"Item {Item_2} has been added to your order")
    else:
        print(f"Ordered item {Item_2} is not avaliable yet sorry !")
print(f"The total amount of item to pay is {order_total}")