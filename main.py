menu = {
    'pizza' : 80,
    'burger': 70,
    'drinks': 50,
    'salad': 30,
    'iceCream': 60,
 }

print('''
      ---Welcome To Our Cafe---
          ---Python Cafe---
      ''')
print("-----------MENUS--------------")
print("pizza: 80\nburger: 70\ndrinks: 50\nsalad: 30\niceCream: 60")
print("---------")

order_total = 0
while True:
    item_1 = input("Enter your choice that u want:- ")
    print("----------------------------------------")
    if item_1 in menu:
        order_total += menu[item_1]
        print(f'Your order item "{item_1}" has been added')    
    else:
        print(f"Sry, '{item_1}' is not available right now")

    another_item = input("Do u want to add something else? (Yes/No)")
    print("---------------------------------------------------------")
    if another_item == "Yes":
        item_2 = input("Enter Your Another Choice That U Want To Add:- ")
        print("----------------------------------------------------")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f'Your Order Item "{item_2}" has been added')
        else:
            print(f"Sry, '{item_2}' if not available right now")
    print(f"The Total amount of your order is {order_total}")
    print("Thanku for coming come back soon-----")
    



