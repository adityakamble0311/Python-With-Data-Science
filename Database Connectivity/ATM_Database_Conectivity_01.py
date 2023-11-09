# 11/08/2023
import random
import pyttsx3
import datetime as date
from tabulate import tabulate
import mysql.connector
from datetime import datetime, timedelta


ac_pin=random.randrange(1000,9999)
ac_no=random.randrange(100000000000,999999999999)
try:
    con =  mysql.connector.connect(host='localhost',username='root',password='',database='atm')
    # print("Database Connected Successfully !")
except:
    print("Error")
mycur = con.cursor()
info_date = date.datetime.now()

    
print("\033[1m"+"="*45)
print("\U0001F604 Welcome to the Python Banking System \U0001F604".upper().center(40,' '))
print("="*45)
engine = pyttsx3.init()
engine.say("Welcome to the Python Banking System")
engine.runAndWait()
engine.stop()
     
while True:
        print("-"*25)
        print("1.Admin Login \U0001F512")
        print("2.User Login \U0001F464")
        print("3.Exit \U0000274C")
        print("-"*25)
        while True:
            try:
                ch = int(input("Please Enter What to do \U0001F4E5 :"))
                break
            except:
                print("Please enter digits only ")
        if ch == 1:
            while True:
                print("=" * 25)
                print("xx Admin Login xx".center(25, '-'))
                print("=" * 25)
                admim_username = input("Please Enter a username: ")
                admim_password = input("Please Enter a password: ")
                sqlQuery = "SELECT * FROM admin WHERE username = '{}' AND password = '{}'".format(admim_username, admim_password)
                mycur.execute(sqlQuery)
                admin_data = mycur.fetchall()
                if admin_data:
                    engine = pyttsx3.init()
                    engine.say(admim_username+"Login Successfully ")
                    engine.runAndWait()
                    engine.stop()
                    print("x" * 40)
                    print("\U0001F618",admim_username.upper()+" LOGIN SUCCESSFULLY \U0001F618 ")
                    print("x" * 40)
                    break
                else:
                    print("Invalid login please try again!")
   
            while True:
                    print("="*30)
                    print("| Admin Panel |".center(30,'-'))
                    print("="*30)
                    print("1.Create New Account \U0001F4CB\U00002705")
                    print("2.Total Balance Check \U0001F4B0")
                    print("3.Total Accounts Check \U0001F4BC")
                    print("4.Add New Admin \U0001F195")
                    print("5.logout \U0000274C")
                    print("-"*30)
                    while True:
                        try:
                            ch = int(input("Please Enter What to do \U0001F4E5 :"))
                            break
                        except:
                            print("Please enter digits only ")
                    if ch == 1:
                            print("-"*30)
                            print("Create Account".center(30,'-'))
                            print("-"*30)
                            name = str(input("Please enter your Name :"))
                            city= str(input ("Please Enter Your City :" ))
                            account_type= input("1.Savings Account \n2.Current Account \nPlease Choice Your Accounts: ")
                            balance=float(input("How much do you want to deposit : "))
                            print("="*55)
                            print("WELCOME".center(60,"-"))
                            print("="*55)
                            total_info = [[name,balance,ac_no,ac_pin,info_date]]
                            header = ['Name','BALANCE','ACCOUNT NUMBER','YOUR PIN','DATE']
                            print(tabulate(total_info,header,tablefmt='heavy_grid'))
                            try:
                                sqlQuery = "insert into createaccount values('{}','{}','{}','{}','{}','{}')".format(name,city,account_type,balance,ac_no,ac_pin)
                                mycur.execute(sqlQuery)
                                con.commit()
                                engine = pyttsx3.init()
                                engine.say("welcome"+name)
                                engine.runAndWait()
                                engine.stop()
                                print("x"*50)
                                print(name.center(50,' '))
                                print("\U0001F618 Account Has Been Created Successfully \U0001F618".center(50,' '))
                                print("x"*50)
                            except:
                                print("Error")

                    elif ch == 2:
                        sqlQuery="SELECT SUM(opening_balanace) FROM createaccount"
                        mycur.execute(sqlQuery)
                        total_account = mycur.fetchall()[0]
                        con.commit()
                        print("x"*50)
                        print("Total Balance is Rs.",total_account)
                        print("x"*50)
                    elif ch==3:
                        sqlQuery="SELECT COUNT(*) FROM createaccount"
                        mycur.execute(sqlQuery)
                        total_account = mycur.fetchall()[0]
                        con.commit()
                        print("x"*50)
                        print("Total Accounts is :",total_account)
                        print("x"*50)
                    elif ch==4:   
                        while True:
                            new_username=input("Please Enter a new username :")
                            new_password = input("Please Enter a new password : ")

                            sqlQuery="insert into admin values ('{}','{}')".format(new_username,new_password)          #insert query
                            mycur.execute(sqlQuery)
                            con.commit()
                            print("New admin added successfully \u2713")
                            break
                    elif ch==5:
                            print("x"*50)
                            print("Logout Successful.....!")
                            print("x"*50)
                            break
                    else:
                            print("Invalid Choice Try Again.......")
        elif ch == 2:
            while True:
                user_input = int(input("Please Enter Your Account Number: "))
                user_pin = int(input("Please Enter Your 4 Digit Pin: "))
                sqlQuery = "select * from createaccount where account_number='{}' and pin='{}'".format(user_input,user_pin)
                mycur.execute(sqlQuery)
                data = mycur.fetchall()
                if data:
                            print("x"*50)
                            print("\U0001F618 User Login Successfully \U0001F618".center(50,'-'))
                            print("x"*50)
                            while True:
                                print("="*50)
                                print("OPERATIONS".center(50,'-'))
                                print("="*50)
                                print("1.Diposite \U0001F4B0")
                                print("2.Withdraw \U0001F4B8")
                                print("3.Information \U00002139")
                                print("4.Update Info \U0000270F")
                                print("5.Change Pin \U0001F511")
                                print("6.Delete Account \U0001F5D1")
                                print("7.Last Transections")
                                print("8.logout \U0000274C")
                                print("-"*50)
                                while True:
                                    try:
                                        ch = int(input("Please Enter What to do \U0001F4E5 : "))
                                        break
                                    except:
                                        print("Please enter digits only ")
                                if ch == 1:
                                    debited=0 
                                    sqlQuery="select opening_balanace from createaccount where account_number='{}' and pin='{}'".format(user_input,user_pin)
                                    mycur.execute(sqlQuery)
                                    balance = mycur.fetchone()[0]
                                    con.commit()
                                    print("-"*50)
                                    print("Your Current Balance is :",balance)
                                    print("-"*50)
                                    amount = float(input("Enter Amount To Diposit : "))
                                    total_amount = float((float)(balance)+ (float)((amount)))
                                    sqlQuery = "UPDATE createaccount SET opening_balanace='{}' where account_number='{}' and pin='{}'".format(total_amount,user_input,user_pin)
                                    mycur.execute(sqlQuery)
                                    con.commit()
                                    print("x"*50)
                                    print("Amount Deposited Successfully Rs.{} \nYour Current Balance is Rs.{}".format(amount,total_amount))
                                    print("x"*50)
                                    mn="insert into transection values('{}','{}','{}','{}')".format(amount,debited,user_input,info_date)
                                    mycur.execute(mn)
                                    con.commit()
                                elif ch == 2:
                                    sqlQuery="select opening_balanace from createaccount where account_number='{}' and pin='{}'".format(user_input,user_pin)
                                    mycur.execute(sqlQuery)
                                    balance = mycur.fetchone()[0]
                                    con.commit()
                                    print("-"*50)
                                    print("Your Current Balance is :",balance)
                                    print("-"*50)

                                    amount = int(input("Please Enter The Amount yo want to withdraw : "))
                                    if int((int)(amount)>(float)(balance)):
                                        print("Insufficient balance, You can't Withdraw this much money")
                                    else:
                                        result=float((float)(balance)-(int)(amount))
                                        sqlQuery = "UPDATE createaccount SET opening_balanace='{}' where account_number='{}' and pin='{}'".format(result,user_input,user_pin)
                                        mycur.execute(sqlQuery)
                                        con.commit()
                                        print("x"*60)
                                        print("You have Successfully withdrew Rs.{} \nYour Current Balance is Rs.{}".format(amount,result))
                                        print("x"*60)

                                        withdrawal_query = "INSERT INTO transection (amount, debited, account_number, info_date) VALUES ('{}', 1, '{}', '{}')".format(amount, user_input, info_date)
                                        mycur.execute(withdrawal_query)
                                        con.commit()
                                        
                                elif ch == 3:
                                    sqlQuery = "SELECT * FROM createaccount where account_number='{}' and pin='{}'".format(user_input,user_pin)
                                    mycur.execute(sqlQuery)
                                    all_accounts=mycur.fetchall()
                                    print("x"*75)
                                    print("INFORMATIONS".center(70,' '))
                                    print("x"*75)
                                    table_data = []
                                    for account in all_accounts:
                                        table_data.append([account[0],account[1],account[2],account[3],account[4],account[5]])
                                        
                                    headers = ["Name", "City", "Account Type", "Balance", "Account Number", "Pin"]
                                    print(tabulate(table_data,headers, tablefmt="rounded_grid"))
                                    con.commit()

                                elif ch ==  4:
                                            print("-"*40)
                                            print("UPDATE INFORMATION".center(40,'-'))
                                            print("-"*40)
                                            print("1. Update Name  \U0001F4DD")
                                            print("2. Update City \U0001F3D9 FE0F")
                                            print("3. Update Account Type \U0001F4B3")
                                            print("4. Exit \U0000274C")
                                            while True:
                                                try:
                                                    update_choice = int(input("Please Enter What to do : "))
                                                    break
                                                except:
                                                    print("Please enter digits only ")
                                            if update_choice == 1:
                                                new_name = input("Enter new name: ")
                                                sqlQuery="update createaccount set name='{}' where account_number='{}' and pin='{}'".format(new_name,user_input,user_pin)
                                                mycur.execute(sqlQuery)
                                                con.commit()
                                                print("-"*50)
                                                print ("xx Name is Updated Successfully xx".center(50,' '))
                                                print("-"*50)
                                            elif update_choice == 2:
                                                new_city = input("Enter new city: ")
                                                sqlQuery="update createaccount  set city='{}' where account_number='{} and pin='{}'".format(new_city,user_input,user_pin)
                                                mycur.execute(sqlQuery)
                                                con.commit()
                                                print("-"*50)
                                                print ("xx City is Updated Successfully xx".center(50,' '))
                                                print("-"*50)
                                            elif update_choice == 3:
                                                new_account_type = input("Enter new account type: ")
                                                sqlQuery="update createaccount set account_type='{}' where account_number='{}' and pin='{}'".format(new_account_type,user_input,user_pin)
                                                mycur.execute(sqlQuery)
                                                con.commit()
                                                print("-"*50)
                                                print ("xx Account Type is Updated Successfully xx".center(50,' '))
                                                print("-"*50)
                                            elif update_choice == 4:
                                                print("Exit")
                                            else:
                                                print("Invalid choice. Please try again.")
                                elif ch == 5 :  
                                    while True:     
                                            old_pin = int(input("Enter a old pin :"))
                                            if user_pin==old_pin:
                                                new_pin= int(input("Please Enter a 4 digit new pin :"))
                                                sqlQuery="update createaccount set pin ='{}' where account_number='{}' and  pin='{}'".format(new_pin,user_input,user_pin)
                                                mycur.execute(sqlQuery)
                                                con.commit()
                                                print("Pin Changed Successfully")
                                                break
                                            else:
                                                print('old Pin does not match Please try Again')
                                                continue
                                elif ch == 6 :
                                    sqlQuery="DELETE FROM createaccount where account_number='{}'".format(user_input)
                                    mycur.execute(sqlQuery)
                                    con.commit()
                                    print("="*50)
                                    print("Record Deleted successfully")
                                    print("="*50)
    
          
                                elif ch == 7:
                                    today = datetime.now()
                                    one_month_ago = today - timedelta(days=30)
                                    
                                    sqlQuery = "SELECT * FROM transection WHERE account_number='{}' AND info_date >= '{}'".format(user_input, one_month_ago)
                                    mycur.execute(sqlQuery)
                                    transaction_data = mycur.fetchall()

                                    print("=" * 50)
                                    print("Transaction History (Last 1 Month)".center(50, '-'))
                                    print("=" * 50)

                                    headers = ["Amount", "Transaction Type", "Account Number", "Date"]
                                    transaction_table = []

                                    for transaction in transaction_data:
                                        amount = transaction[0]
                                        transaction_type = "Deposit" if transaction[1] == 0 else "Withdrawal"
                                        account_number = transaction[2]
                                        transaction_date = transaction[3].strftime("%Y-%m-%d %H:%M:%S")
                                        transaction_table.append([amount, transaction_type, account_number, transaction_date])

                                    print(tabulate(transaction_table, headers, tablefmt="grid"))
                                    con.commit()



                                elif ch == 8 :
                                            engine = pyttsx3.init()
                                            engine.say("Thank U For Visit Our Python Banking System\nDesign & Devloped By | Aditya")
                                            engine.runAndWait()
                                            engine.stop()
                                            print("-"*25)
                                            print("Thank U For Visit Our Python Banking System\nDesign & Devloped By | \U00002764 Aditya Kamble \U00002764")
                                            print("-"*25)
                                            break
                                else :
                                        print("Invalid Choice , Please try again !")    
                else:
                    print("Wrong Username or password")    
                break
        elif ch == 3:
            engine = pyttsx3.init()
            engine.say("Thank U For Visit Our Python Banking System\nDesign & Devloped By | Aditya")
            engine.runAndWait()
            engine.stop()
            print("-"*25)
            print("Thank U For Visit Our Python Banking System\nDesign & Devloped By | \U00002764 Aditya Kamble \U00002764")
            print("-"*25)
            break
        else:
            print("Invalid choice. Please try again  \U0000274C")


            