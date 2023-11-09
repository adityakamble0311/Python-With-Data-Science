# 01/08/2023
import random
import mysql.connector
class ATM:
    
    ac_pin=random.randrange(1000,9999)
    ac_no=random.randrange(100000000000,999999999999)
    user={"aditya":1234}
    all_accounts=[]
    def __init__(self,name,city,account_type,balance):
        self.name = name
        self.city = city
        self.account_type = account_type
        self.balance = balance
        ATM.all_accounts.append(self)
try:
    con = mysql.connector.connect(host='localhost',username='root',password='Aditya@12072004@',database='atm')
    print("Database connected successfully.......")
except:
    print("Error")
    mycur = con.cursor()
#-----------------------admin login-------------------------------------
    @classmethod
    def adminLogin(cls):
        while True:
            print("-"*25)
            print("| Admin Login |".center(25,'-'))
            print("-"*25)
            username = input("Please Enter a username: ")
            password = input("Please Enter a password: ")
            if username in cls.user and cls.user [username]== password:
                        print("-"*30)
                        print(username.upper(),"Login Successfully ".upper())
                        print("-"*30)
                        break
            else:
                        print("Invalid login please try aagain !")

    @classmethod
    def craeteAccount(cls):
        print("-"*30)
        print("Create Account".center(30,'-'))
        print("-"*30)
        name = str(input("Please enter your Name :"))
        city= str(input ("Please Enter Your City :" ))
        account_type= input("1.Savings Account \n2.Current Account \nPlease Choice Your Accounts: ")
        balance=float(input("How much do you want to deposit : "))

        sqlQuery = "INSER INTO createaccount values('{}','{}','{}','{}','{}','{}')".format(name,city,account_type,balance,ac_no,ac_pin)
        mycur.execute(sqlQuery)
        con.commit()
        print("Data Inserted Succesfully")


       
        while True:
            if not any(account.ac_no==cls.ac_no for account in cls.all_accounts):
                if not any(account.ac_pin==ac_pin for account in cls.all_accounts):
                    break

        print("-"*30) 
        print("WELCOME".center(30,"-"))
        print("-"*30)
        print("NAME           | ",name.upper())
        print("ACCOUNT NUMBER | ",cls.ac_no)
        print("Your PIN       | ",cls.ac_pin)
        print("-"*30)
        obj = ATM(name,city,account_type,balance)
        return obj
     
    @classmethod
    def total_balance(cls):
       return sum(account.balance for account in cls.all_accounts)
       
    @classmethod
    def total_account(cls):
        return len(cls.all_accounts)

    @classmethod
    def AddNewAdmin(cls):
            while True:
                new_username=input("Please Enter a new username :")
                new_password = input("Please Enter a new password : ")
                if new_username in cls.user:
                    print("Username already exists.")
                else:
                    cls.user[new_username]=new_password
                    print("New admin added successfully.")
                    break
            
    def  adminChoiceOP():
        while True:
            print("="*30)
            print("| Admin Panel |".center(30,'-'))
            print("="*30)
            print("1.Create New Account")
            print("2.Total Balance Check")
            print("3.Total Accounts Check")
            print("4.Add New Admin")
            print("5.logout")
            print("-"*30)
            ch = int(input("Please Enter What to do :"))
            if ch == 1:
                demo_obj=ATM.craeteAccount()
            elif ch == 2:
                print("Total Balance :",ATM.total_balance())
            elif ch==3:
                print("Total Accounts :",ATM.total_account())
            elif ch==4:
                ATM.AddNewAdmin()
            elif ch==5:
                print("Logout Successful.....!")
                break

#----------------------user login--------------------------------------
    # @classmethod
    def info(self):
               print("="*40)
               print("INFORMATION".center(40,'-'))
               print("="*40)
               print("Name           |",self.name)
               print("City           |",self.city)
               print("Balance        |",self.balance)
               print("Account Type   |",self.account_type)
    @classmethod
    def info2(cls):
            print("Account Number |",cls.ac_no)
            print("Your PIN       |",cls.ac_pin)
            print("_"*40)
    
    @classmethod
    def updateInfo(cls):
          for account in cls.all_accounts:
                            print("=" * 40)
                            print("-"*40)
                            print("UPDATE INFORMATION".center(40,'-'))
                            print("-"*40)
                            print("1. Update Name")
                            print("2. Update City")
                            print("3. Update Account Type")
                            print("4. Exit")
                            update_choice = int(input("Please Enter Your Choice: "))

                            if update_choice == 1:
                                new_name = input("Enter new name: ")
                                account.name = new_name
                                print("-"*50)
                                print("Name updated successfully")
                                print("-"*50)
                            elif update_choice == 2:
                                new_city = input("Enter new city: ")
                                account.city = new_city
                                print("-"*50)
                                print("City updated successfully")
                                print("-"*50)
                            elif update_choice == 3:
                                new_account_type = input("Enter new account type: ")
                                account.account_type = new_account_type
                                print("-"*50)
                                print("Account type updated successfully")
                                print("-"*50)
                            elif update_choice == 4:
                                print(" Information update")
                            else:
                                print("Invalid choice. Please try again.")

    def diposite(self):
        try:
            amount=int(input('Please Enter The Amount you want to deposit :'))
        except:
            print("Invalid Input!!!")
        self.balance+=amount
        print("-"*50)
        print("Your Current Balance is :",self.balance)
        print("-"*50)

    def withdraw(self):
        try:
            amount = int(input("Please Enter The Amount yo want to withdraw : "))
        except:
            print("Invalid Input ")
        if amount>=self.balance:
            print("Insufficient balance, You can't Withdraw this much money")
        else:
            self.balance-=amount
            print("-"*100)
            print("You have Successfully withdrew Your Current Balance is :",self.balance)
            print("-"*100)


    @classmethod
    def loginUser(cls):
        while True:
            for account in cls.all_accounts:
                user_input = int(input("Please Enter Your Account Number: "))
                user_pin = input("Please Enter Your 4 Digit Pin: ")
                if account.ac_no == user_input and account.ac_pin == user_pin:
                        print("-"*30)
                        print("User Login Successfully".center(30,'-'))
                        print("-"*30) 
                        while True:
                            print("="*50)
                            print("OPERATIONS".center(50,'-'))
                            print("="*50)
                            print("1.Diposite")
                            print("2.Withdraw")
                            print("3.Information")
                            print("4.Update Info")
                            print("5.Change Pin")
                            print("6.logout")
                            print("-"*50)

                            ch = int(input("Please Enter What to do :"))

                            if ch == 1:
                                account.diposite()
                            elif ch == 2:
                                account.withdraw()
                            elif ch == 3:
                                account.info()
                                account.info2()
                            elif ch ==  4:
                                ATM.updateInfo()
                                pass
                            elif ch == 5 :
                                account.updatePin()
                            elif ch == 6 :
                                print("Thank U For Visit Our Python Banking System\nDesign & Devloped By | Aditya Kamble")
                                break 
                            else :
                                print("Invalid Choice , Please try again !")                
                      
                else:
                        print("Invalid Account Number or PIN. Please try again.") 
            break      
                
            

    @classmethod
    def updatePin(cls):
        while True:
            cls.ac_pin=input(("Please Enter a old pin : "))
            new_pin=input("Please Enter a 4 digit new pin :")
            cls.ac_pin==new_pin
            if cls.ac_pin!=new_pin:
                 print("Pin Changed Successfully")
                 break
            else:
                print("Please don't use same pin please try agian new pin")
                

def main():
        print("-"*40)
        print("Welcome to the Python Banking System".upper())
        print("-"*40)
        while True:
            print("-"*25)
            print("1.Admin Login")
            print("2.User Login")
            print("3.Exit")
            print("-"*25)
            ch = int(input("Please Enter a choice:"))
            if ch == 1:
                print("-"*25)
                ATM.adminLogin()
                ATM.adminChoiceOP()
                print("-"*5)
            elif ch == 2:
                print("-"*25)
                ac_obj=ATM.loginUser()
                print("-"*25)
            elif ch == 3:
                print("-"*25)
                print("Thank U For Visit Our Python Banking System\nDesign & Devloped By | Aditya Kamble")
                print("-"*25)
                break
            else:
                print("Invalid choice. Please try again")

if __name__ == "__main__":

    main()


