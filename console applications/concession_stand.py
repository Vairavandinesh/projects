#we are creating a concession stand program for a movie theatre
#it will have a dictionary of food items.users can access them and add to their cart and purchase them
#first lets create a menu of the food projects in the counter
#its a dictionary with food as key and value is their priice
menu={"pizza":2.0,
      'popcorn':6.0,
      'chips':4.0,
      'biscuits':3.0,
      'soda':2.50}
#then we will have a cart to store all the things that the user orders
cart=[]
#and the total price of all the purchases that he/she made
total=0
for k,v in menu.items():
    print(f"{k:10}: ${v:.2f}")
#now the products are in display to the user
#now prompt the user to enter the product the want to purchase
#use a while loop, as it will ask to enter again and again until the user quits
while True:
    food=input("Enter the food name to order [q to quit] : ")
    if food=="q":
        break
    else:
        if menu.get(food) is not None: #if the asked food is in the menu
            cart.append(food)#add the food to user's cart
            total+=menu[food]
print("Your cart : ")
for i in cart:
    print(i,end=" ")
print()
print(f"Total price is {total:.2f}")