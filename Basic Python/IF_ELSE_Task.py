'''
    If else Task         29/06/2023 
'''



# a = 5 
# b = 8
# c = 8

# if a==b and b==c and c ==a:
#     print("All Are Equal")
# elif a==b:
#     print("A And B Match")
# elif b==c :
#     print("B And C Match")
# elif c==a:
#     print("C And A Match")
# else :
#     print("All Are different")



name = input("Name: ")
city = input("City :")
balance = float(input("Balance:"))
pin1 = int(input("Enter a pin :"))
pin2 = int(input("Confirm pin :"))

if pin1 == pin2:
   pass
else :
    print("Pin is not match")
    pin2 = int(input("Please Enter your currect pin :"))
if pin1== pin2:
    ch=0
    while ch != 4:
        print('*'*20)
        print('       Menu')
        print('*'*20)
        print("1.Withdraw")
        print("2.Deposit")
        print("3.balance")
        print("4.Exit")
        print('*'*20)
        print('*'*20)
        break
    ch=int(input("Enter Choise: "))
if ch==1:
    amount=int(input("Amount: "))
    if balance<amount:
        print("Insufficient funds")
        
    else:
        balance=balance-amount
        print("Balance: ",balance)  
    
elif ch==2:
    amount=int(input("Amount: "))
    balance=balance+amount
    print("Balance: ",balance)
    
elif ch==3:
    print("*"*20)
    print("    Balance")
    print("*"*20)
    print("Name :",name)
    print("Balance :",balance)
    print("City :",city)
    print("*"*20)
else:
    print("Exit Success")
    ch=int(input("Enter Choise: "))


