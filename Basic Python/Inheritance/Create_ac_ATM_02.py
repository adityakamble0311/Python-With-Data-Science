# 31/07/2023
import random
class ATM:
    all_accounts = []  

    def __init__(self, name, city,actype,balance,r1,pin):
        self.name = name
        self.city = city
        self.actype = actype
        self.balance = balance
        self.r1=r1
        self.pin=pin
        ATM.all_accounts.append(self)

    def info(self):
        print("-"*20)
        print("Account Number :",self.r1)
        print('Name:', self.name)
        print("City:", self.city)
        print("Account Type:", self.actype)
        print("Balance:", self.balance)
        print("-"*20)

    def operations(self):
        while True:
                print("*"*20)
                print("1.Deposite")
                print("2.Withdraw")
                print("3.Info")
                print("4.Exit")
                print("*"*20)
                self.choice=int(input("Enter a choice :"))
                if self.choice==1:
                    self.diposite()
                elif self.choice==2:
                    self.withdraw()
                elif self.choice==3:
                    self.info()
                elif self.choice == 4:
                    break      

    def diposite(self):
        deposite=int(input("Enter Deposit Amount :"))
        self.balance+=deposite
        print("Diposite Amount Successful !",self.balance)
    
    def withdraw(self):
        amount = int(input("Enter the Amount to Withdraw : "))
        if amount>=self.balance:
            print("insufficent amount")
        else:
            self.balance=self.balance-amount
            print("Withdraw Amount Successful !!!!",self.balance)
    
    @classmethod
    def createAc(cls):
        name = input("Enter a name: ")
        city = input("Enter a city: ")
        actype = input("1.Savings\n2.Current\nChoice Account: ")
        balance = int(input("Enter a balance: "))
        while True:
            r1 = random.randrange(100000000000,999999999999)            #account generate
            pin = random.randrange(0000,9999)                           #pin generate 
            if not any(account.r1==r1 for account in cls.all_accounts):
                break
            if not any(account.pin==pin for account in cls.all_accounts):
                break
        obj = ATM(name, city, actype, balance,r1,pin)
        print("-"*20)
        print("Welcome |",obj.name)
        print("Account Number :",obj.r1)
        print("Your pin is generated :",obj.pin)
        print("-"*20) 

        enter_pin=int(input("Enter 4 digit pin :"))
        if pin == enter_pin:
            print("-"*20)
            print("login Successfully !".upper())
            print("-"*20)
            obj.info()
            obj.operations()
        else:
            print("Pin is wrong please check your pin")

    @classmethod
    def login_account(cls):
        ac_input = int(input("Enter the Account Number : "))
        for account in cls.all_accounts:
            if account.r1 == ac_input:
                account.info()
                return
        print("Account is not found....!!")

    @classmethod
    def t_ac(cls):
        return len(cls.all_accounts)

    @classmethod
    def t_bal(cls):
        return sum(account.balance for account in cls.all_accounts)

def main():
    user = {"aditya": 1234,"anupam":1234,"harshal":1234}
    print("*"*25)
    print("       Admin Login")
    print("*"*25)
    username = input("Enter a username: ")
    password = int(input("Enter a password:"))
    print("*"*25)
    if username in user and user[username] == password:
        print("-"*20)
        print(username.upper(),"Login Successfully !!")
        print("-"*20)
        while True:
            print("*"*25)
            print("         Menu")
            print("*"*25)
            print("1.Create Account")
            print("2.Login Account")
            print("3.Total Account")
            print("4.Total Balance")
            print("5.Exit")
            print("*"*25)
            ch = int(input("Enter a choice:"))
            if ch == 1:
                print("-"*20)
                ac_obj = ATM.createAc()
                print("-"*20)
            elif ch == 2:
                ATM.login_account()
            elif ch == 3:
                print("-"*20)
                print("Total Accounts:", ATM.t_ac())
                print("-"*20)
            elif ch == 4:
                print("-"*20)
                print("Total Balance:", ATM.t_bal())
                print("-"*20)
            elif ch == 5:
                print("-"*20)
                print("Exiting program...")
                print("-"*20)
                break
            else:
                print("Invalid choice. Please try again")

    else:
        print("Invalid Username or Password!")

if __name__ == "__main__":
    main()
    