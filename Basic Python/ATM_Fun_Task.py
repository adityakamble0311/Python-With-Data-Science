'''
ATM using functin  Task                                                                      

date 05/07/2023

'''



def withdraw (balance):
    amount=int(input("Amount: "))
    if balance<amount:
        print("Insufficient funds")
       
    else:
        balance=balance-amount
        print("Balance: ",balance)
        
def deposit (balance):
    amount=int(input("Amount: "))
    balance=balance+amount
    print("Balance: ",balance)

def display():
    print('*'*20)
    print("      Balance")
    print('*'*20)
    print("Name: ",name)
    print("Balance: ",balance)
    print("City: ",city)
    print('*'*20)
    
def menu():
        ch=0
        while ch != 4:
            print('*'*20)
            print('        Menu')
            print('*'*20)
            print("1.Withdraw")
            print("2.Deposit")
            print("3.balance")
            print("4.Exit")
            break
        
name = input("Name: ")
city = input("City :")
balance = int(input("Balance:"))
pin1 = int(input("Enter a pin :"))
pin2 = int(input("Enter Confirm pin :"))
if pin1!=pin2:
    pin2 = int(input("Please Enter a currect pin :"))
    if pin1 == pin2 :
        menu()
        ch=int(input("Enter Choise:"))
        if ch==1:
            balance=withdraw(balance)
            print("Balance withdraw sucessful !")
        elif ch==2:
            balance=deposit(balance)
            print("Balance deposit sucessful !")
        elif ch==3:
            display()
        else:
            ch=int(input("Enter Choise:"))
    else:
        print("Incurrect password")
        
else :
   if pin1 == pin2 :
        menu()
        ch=int(input("Enter Choise:"))
        if ch==1:
            balance=withdraw(balance)
            print("Balance withdraw sucessful !")
        elif ch==2:
            balance=deposit(balance)
            print("Balance deposit sucessful !")
        elif ch==3:
            display()
        else:
            ch=int(input("Enter Choise:"))