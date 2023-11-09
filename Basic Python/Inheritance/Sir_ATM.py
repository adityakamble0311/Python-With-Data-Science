class Atm:

    id = 0

    def _init_(self,name,balance):
        self.name = name
        self.balance = balance
        self.id+=1
        Atm.id+=1
   

    def info(self):
        print("Id: ",self.id)
        print("Name: ",self.name)
        print("Balance: ",self.balance)
    
    def withdraw(self):
        amt = int(input("Enter Amount to Withdraw: "))
        if amt > self.balance:
            print("Insufficient Balance: ",self.balance)
        else:
            self.balance = self.balance + amt
            print(" Successfull Withdraw: ",self.balance)

    def deposite(self):
        amt = int(input("Enter Amount to Deposite: "))
        self.balance =self.balance + amt
        print(" Successfull Deposite: ",self.balance)



def main():
    users = []
    while True:
        print("Welcome To Atm".center(20,'-'))
        print("1.Create Account")
        print("2.Login Account")
        print("3.Total Accounts")
        print("4.Total Balance")
        print("5.Quit")
        choice = int(input("Enter Choice: "))
        if choice == 1 :
            name = input("Enter Name: ")
            balance = int(input("Enter Opening Balance: "))
            obj = Atm(name,balance)
            users.append(obj)
            print("Account Created: ID:",obj.id)
        elif choice == 2:
            while True:
                print(users)
                user_id = []
                for i in users: 
                    user_id.append(int(i.id))
                print(user_id)
                u_id = int(input("Enter Id: "))
                if u_id in user_id:
                    index = user_id.index(u_id)
                    obj = users[index]
                    print(obj.name.upper(),"Logged In Sucessfully!!")
                    break
                else:
                    print("ID not found!!")
                    continue

            while True:
                print("MENU".center(20,'-'))
                print("1.Deposite")
                print("2.Withdraw")
                print("3.Info")
                print("4.Logout")
                ch = int(input("Enter Choice: "))
                if ch  == 1:
                    obj.deposite()
                elif ch == 2:
                    obj.withdraw()
                elif ch == 3:
                    obj.info()
                elif ch == 4:
                    break
                else:
                    print("Invalid Input")
        elif choice == 3:
            print("Total Accounts: ",len(users))
        elif choice == 4:
            total_balance = []
            for i in users:
                total_balance.append(int(i.balance))
            total_balance = sum(total_balance)
            print("Total Balance in Bank:",total_balance)
        
        elif choice == 5:
                break
        else:
            print("Wrong Input!!")

main()