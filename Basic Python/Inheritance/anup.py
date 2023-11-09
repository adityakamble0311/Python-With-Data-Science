
import random
class atm:

    all_accounts=[]
    admin_user="Anupam"
    admin_password="0810"
    id=random.randint(100000000000,999999999999)
    password=random.randint(1000,9999)
    def _init_(self,id,name,balance,passwoed):
        self.id=id
        self.name=name
        self.balance=balance
        self.password=passwoed
        
        
#-------------------------------Admin----------------------------------------------
    def admin():

        while True:
            print("\n")
            print("Admin login page".center(50,"-"))
            username=input("Enter Admin Username: ")
            password=input("Enter Admin Password: ")

            if username==atm.admin_user and password==atm.admin_password:
                atm.adminpanal()
                break
            else:
                print("Invalid Username & Password try again")
                break

    def adminpanal():
        print("login sucessful...")
        while True:

            
            print(f"{atm.admin_user} is logged in ".center(50,"="))
            print("1.create account")
            print("2.ceck balance")
            print("3.ceck account")
            print("4.Log out")

            c=int(input("enter coice: "))
            if c==1:
                atm. create()
                

            elif c==2:
                balance=0
                for account in atm.all_accounts:
                    balance+=account.balance

                print(balance)

            elif c==3:
                print(len(atm.all_accounts))

            elif c==4:
                break


    def create():

        id=atm.id
        name=input("Enter Name: ")
        password=atm.password
        balance=int(input("Enter openin balance: "))
        obj=atm(id,name,balance,password)
        atm.all_accounts.append(obj)
        print("account created")
        print("REMEMBER YOUR ACCOUNT INFO".center(50,"="))
        print("ID           : ",id)
        print("NAME         : ",name)
        print("PASSWORD     : ",password)
        print("*"*50)
#----------------------------------Usetr----------------------------------------------------------------------------

    def user():
        print("user loin page".center(50,"-"))
    
        id=int(input("Enter id: "))
        password=int((input("Enter Password: ")))
        for account in atm.all_accounts:
            if account.id==id and account.password==password:
                print("loin sucessful")
                while True:

                    print("MENU".center(50,"-"))
                    print("1.info")
                    print("2.widrow")
                    print("3.deposite")
                    print("4.change password")
                    print("5.Log Out")
                    c=int(input("enter te coice: "))
                    if c==1:
                        while True:
                            test=int(input("Enter Password: "))
                            if test==account.password:
                                atm.info(account)
                                break
                            
                    elif c==2:
                        while True:
                            test=int(input("Enter Password: "))
                            if test==account.password:
                                atm.widrow(account)
                                break
                                
                            

                    elif c==3:
                        while True:
                            test=int(input("Enter Password: "))
                            if test==account.password:
                                atm.diposite(account)
                                break

                    elif c==4:
                        while True:
                            old_pass=int(input("Enter old password: "))
                            if old_pass==account.password:
                                new_password=int(input("Enter new password: "))
                                account.password=new_password
                                print("Password changed")
                                break
                            else:
                                print("Old Password is wrong \nTry Again")


                    elif c==5:
                        break

           


    

    def info(obj):
        print("information".center(50,"-"))
        
        print("Id          :",obj.id)
        print("Name        :",obj.name)
        print("Balance     :",obj.balance)


    def widrow(obj):
        print("WIDROW".center(50,"-"))

        while True:
            ammount=int(input("enter ammount: "))
            if ammount<obj.balance:
                obj.balance-=ammount
                print(obj.balance)
                break
            else:
                print("ammount is to more then your balance")
                

    def diposite(obj):
        print("DIPOSITE".center(50,"-"))

        ammount=int(input("enter ammount: "))
        obj.balance+=ammount
        print(obj.balance)






def main():
    while True:
        print("\n")
        print("Welcome in my project".center(50,"-"))
        print("1.Admin loin")
        print("2.user loin")
        print("3.Exit")
        c=int(input("Enter the coice: "))
        print("="*50)
        if c==1:
            atm.admin()

        elif c==2:
            atm.user()
        
        
        elif c==3:
            break


main()

