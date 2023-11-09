
# # 28/07/2023

# # create accounts 
# # login accounts
# # total accounts
# # total Balances



class ATM:
    id = 1
    all_accounts = []  

    def __init__(self, name, city, actype, balance):
        self.name = name
        self.city = city
        self.actype = actype
        self.balance = balance
        self.id = ATM.id
        ATM.id += 1
        ATM.all_accounts.append(self)  

    def info(self):
        print("-"*20)
        print("ID:", self.id)
        print('Name:', self.name)
        print("City:", self.city)
        print("Account Type:", self.actype)
        print("Deposited Balance:", self.balance)
        print("-"*20)
        while True:
            print("*"*20)
            print("1.Deposite")
            print("2.Withdraw")
            print("3.Info")
            print("4.Exit")
            print("*"*20)
            choice=int(input("Enter a choice "))
            if choice==1:
                self.diposite()
            elif choice==2:
                self.withdraw()
            elif choice==3:
                self.info()
            elif choice == 4:
                break
            
    def diposite(self):
        deposite=int(input("Enter Deposit Amount :"))
        self.balance+=deposite
        print("Diposite Amount Successful !!! ",self.balance)
    
    def withdraw(self):
        amount = int(input("Enter the Amount to Withdraw : "))
        if amount>=self.balance:
            print("insufficent amount")
        else:
            self.balance=self.balance-amount
            print("Withdraw Amount Successful !!!!",self.balance)

    def displayID(self): 
         print("ID :",self.id)
        
    def createAc():
        name = input("Enter a name: ")
        city = input("Enter a city: ")
        actype = input("1.Savings\n2.Current\nChoice Account: ")
        balance = int(input("Enter a balance: "))

        obj = ATM(name, city, actype, balance)
        print("-"*20)
        print("Welcome |",name)
        print("Account Created ID :",obj.id)
        print("-"*20)
        

    @classmethod
    def login_account(cls):
        id_input = int(input("Enter the ID : "))
        for account in cls.all_accounts:
            if account.id == id_input:
                account.info()
                return
        print("ID not found....!!")

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
    