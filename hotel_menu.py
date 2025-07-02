#MENU CARD OF HOTEL SWEET TREATS
menu={
    'Burger':145,
    'Pizza':299,
    'Pasta':185,
    'Cupcake':50,
    'Salad':190,
    'Coffee':85,
    'Biryani':150,
    'Dosa':175,
    'Idli':70,
    'Samosa':50,
    'Momo':145,
    'Lassi':65,
    'Fruit Juice':125
    


}
#Welcome Everyone To Our SWEET TREATS
print("Welcome Everyone To Our SWEET TREATS RESTAURANT")
print("Burger:Rs145\nPizza:Rs299\nPasta:Rs185\nCupcake:Rs50\nSalad:Rs190\nCoffee:Rs85\nBiryani:Rs150\nDosa:Rs175\nIdli:Rs70\nSamosa:Rs50\nMomo:Rs145\nLassi:Rs65\nFruit Juice:Rs125")

order_total=0
#145+65=210

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1] #0+50
    print(f"Your item {item_1} has been added to our order")
else:
    print(f"Ordered item {item_1} is not available,order something else")

another_order=input("Do you want to add another item? (Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"The total amount of items is {order_total}")
