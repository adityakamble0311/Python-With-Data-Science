'''
25/07/2023 Task
'''


class ATM():
    id=1
    def __init__(self,name,city,balance):
        self.name=name
        self.city=city
        self.balance = balance
        self.id=ATM.id
        ATM.id+=1
    def info (self):
        print()
        print("*"*20)
        print("     INFORMATION")
        print("*"*20)
        print("ID :",self.id)
        print("Name:",self.name)
        print("City",self.city)
        print("Balance :",self.balance)
        print("*"*20)
    
    def withdraw(self):
        amount = int(input("Enter the Amount to Withdraw : "))
        if amount>=self.balance:
            print("insufficent amount")
        else:
            self.balance=self.balance-amount
            print("Withdraw Amount Successful !!!!",self.balance)
    
    def diposite(self):
        deposite=int( input ("Enter Deposit Amount :"))
        self.balance+=deposite
        print("Diposite Amount Successful !!! ",self.balance)

aditya = ATM("aditya","Shirdi",1000)
anupam =  ATM("anupam","Rahata",2000)
mohit =  ATM("Mohit","Rahata",3000)


def operation(obj):
            while True:
                print("*"*20)
                print("1.Withdraw")
                print("2.Diposite")
                print("3.Information")
                print("4.Exit")
                print("*"*20)
                choice=int(input("Enter a choice :"))
                if choice == 1:
                    obj.withdraw()
                elif choice == 2:
                    obj.diposite()
                elif choice == 3:
                    obj.info()
                elif choice==4:
                    break
                else :
                    print("Wrong input")
def main():
            while True:
                print("*"*20)
                print("1.Aditya")
                print("2.Anupam")
                print("3.Mohit")
                print("4.Exit")
                print("*"*20)
                ch = int(input("Enter a choice :"))
                print("*"*20)
                pin1 = int(input("Enter a pin :"))
                pin2 = int(input("Enter confirm pin :"))
                if pin1==pin2:
                    if ch == 1 :
                        operation(aditya)
                    elif ch == 2:
                        operation(anupam)
                    elif ch == 3:
                        operation(mohit)
                    elif ch == 4:
                        break
                    else :
                
                       print("Unknown Student")
                else :
                    print('Pin does not match')
                    
main()

