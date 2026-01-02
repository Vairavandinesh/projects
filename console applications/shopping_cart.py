# This program calculates the total amount the user spent for shopping and the list of food he bought
# 2 lists, one for the food and another one for prices of each food and a variable for calculating the total
foods=[]
prices=[]
total=0
#untill the user quits , the program should repeatedly ask him to add products to his/her cart
#while loop is perfect for that
# so if the user enters q - means quit , the loop will terminate
while True:
    #ask the food that the user ordered
    food=input("Enter the food that you want : ")
    #if user typed q , terminate , else ask again
    if food.lower()=="q":
        break
    else:
        foods.append(food)
        #ask the price of that food
        price=float(input(f"Enter the price of {food} : Rs."))
        prices.append(price)
#use two loops , one to print the list of food ordered, another one to calculate the total bill
for i in foods:
    print(i,end=" ")
print()
for i in prices:
    total+=i
print(f"The total amount spent is {total} Rs.")
print("THANK YOU!")