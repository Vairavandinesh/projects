def checkbalance():
    print(f'{balance:.2f}')
def deposit():
    amount=float(input("Enter deposit amount : "))
    if amount<=0:
        print("Deposit an amount greater than 0")
        return 0
    else:
        return amount
        
def withdraw():
    amount=float(input("Enter an amount to withdraw : "))
    if amount<=0:
        print("Withdrawal amount should be greater than 0")
        return 0
    else:
        return amount

balance=0
running=True
while running:
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.Exit")
    choice=input("Enter a choice : ")
    if choice=='1':
        checkbalance()
    elif choice=='2':
        balance+=deposit()
    elif choice=='3':
        balance-=withdraw()
    elif choice=='4':
        running=False
    else:
        print("Invalid choice")
print("Thank you, have a nice day")