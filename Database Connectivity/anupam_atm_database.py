#ATM PROJECT ANUPAM
import random
import mysql.connector

atmdb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anup0810",
    database="atm"
)

mycursor=atmdb.cursor()

class atm:
    admin_user="Anupam"
    admin_password="0810"
    id=random.randint(100000000000,999999999999)
    password=random.randint(1000,9999)        
#-------------------------------Admin----------------------------------------------
    def admin():

        while True:
            try:
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
            except:
                print("read carefully and please Enter Proper value")
            else:
                break

    def adminpanal():
        print("login sucessful...")
        while True:
            try:
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
            except:
                print("read carefully and please Enter Proper value")
            else:
                break

    def create():
        while True:
            try:
                id=atm.id
                fname=input("Enter First Name: ")
                mname=input("Enter Middle Name: ")
                lname=input("Enter Last Name: ")
                balance=int(input("Enter openin balance: "))
                password=atm.password
                
                sql="INSERT INTO atmpro(id,f_name, m_name, l_name, bal, password) VALUES(%s,%s,%s,%s,%s,%s)"
                values=(id,fname,mname,lname,balance,password)
                mycursor.execute(sql,values)
                atmdb.commit()

                
                print("account created")
                print("REMEMBER YOUR ACCOUNT INFO".center(50,"="))
                print("ID           : ",id)
                print("NAME         : ",fname)
                print("PASSWORD     : ",password)
                print("*"*50)
            except:
                print("read carefully and please Enter Proper value")
            else:
                break
#----------------------------------Usetr----------------------------------------------------------------------------

    def user():
        mycursor=atmdb.cursor()
        print("user loin page".center(50,"-"))
    
        id=int(input("Enter id: "))
        password=int((input("Enter Password: ")))
        sql=f"SELECT * FROM atmpro WHERE id={id} AND password={password}"
        print("ok")
        mycursor.execute(sql)
        
        match=mycursor.fetchone()
        if match:

                print("loin sucessful")
                while True:
                    try:
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
                                if test==password:
                                    atm.info(match)
                                    break
                                
                        elif c==2:
                            while True:
                                test=int(input("Enter Password: "))
                                if test==password: 
                                    atm.widrow(match)
                                    break
                                    
                        elif c==3:
                            while True:
                                test=int(input("Enter Password: "))
                                if test==password:
                                    atm.diposite(match)
                                    break

                        elif c==4:
                            while True:
                                try:
                                    mycursor=atmdb.cursor()
                                    old_pass=int(input("Enter old password: "))
                                    if old_pass==match[-1]:
                                        new_password=int(input("Enter new password: "))
                                        pdate=f"UPDATE atmpro SET password={new_password} WHERE id={match[0]}"
                                        mycursor.execute(pdate)
                                        atmdb.commit()
                                        print("Password changed")
                                        break
                                    else:
                                        print("Old Password is wrong \nTry Again")
                                except:
                                    print("Read Carefully And insert proper value")
                                finally:
                                    mycursor.close()
                                

                        elif c==5:
                            break
                    except:
                        print("read carefully and please Enter Proper value..")
                    finally:
                        mycursor.close()
                    
                        
        else:
            print("Account is not Extst.")            

    def info(obj):
        try:
            mycursor=atmdb.cursor()
            sql=f"SELECT * FROM atmpro WHERE id={obj[0]}"
            mycursor.execute(sql)
            result=mycursor.fetchone()
            print("information".center(50,"-"))
            
            print("Id          :",result[0])
            print(f"Name        :{result[1]} {result[2]} {result[3]}")
            print("Balance     :",result[4])
        except:
            print("abc")
        finally:
            mycursor.close()

    def widrow(obj):
            while True:
                try:
                    mycursor=atmdb.cursor()
                    print("WIDROW".center(50,"-"))
                
                    ammount=int(input("enter ammount: "))
                    password=int(input("Enter the PIN: "))
                    sql=f"SELECT bal FROM atmpro WHERE id={obj[0]}"
                    mycursor.execute(sql)
                    
                    num=mycursor.fetchone()
                    balance=num[0]
                    balance-=ammount
                    update=f"UPDATE atmpro SET bal={balance} WHERE id={obj[0]}"
                    mycursor.execute(update)
                    atmdb.commit()
                    
                    break
                    
                except:
                    print("read carefully and please Enter Proper value")
                else:
                    break
                finally:
                    mycursor.close()
                    

                
    def diposite(obj):
        while True:
            try:
                mycursor=atmdb.cursor()
                print("DIPOSITE".center(50,"-"))
                ammount=int(input("enter ammount: "))
                password=int(input("Enter the PIN: "))

                sql=f"SELECT bal FROM atmpro WHERE id={obj[0]}"
                mycursor.execute(sql)
                num=mycursor.fetchone()
                balance=num[0]
                balance+=ammount
                update=f"UPDATE atmpro SET bal={balance} WHERE id={obj[0]}"
                mycursor.execute(update)
                atmdb.commit()
                
            except:
               print("read carefully and please Enter Proper value")
            else:
                break
            finally:
                mycursor.close()
                

def main():
    while True:
        try:
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
        except:
             print("read carefully and please Enter Proper value.")
        

main() 

