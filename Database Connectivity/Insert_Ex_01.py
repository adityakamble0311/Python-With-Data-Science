import mysql.connector

def connect():
    try:
        conn = mysql.connector.connect(
        host="localhost",
        user= "root",
        password="Aditya@12072004@",
        database='adityadb'
    )
        return conn

    except:
        print("Error in connection")


def insert_data(username,password):
    conn=connect()
    if conn:
        cursorObj = conn.cursor()
        sqlQuery ='INSERT INTO admin (username,password) VALUES (%s,%s)'
        val =(username,password,)
        cursorObj.execute(sqlQuery,val)
        conn.commit()
        print('Data Inserted')
    else:
        print ("Connection Failed!!!")
    cursorObj.close()
    conn.close()

def main():
    username = input("Enter Username : ")
    password  =input("Enter Password : ")
    insert_data(username ,password)
main()

def fectch():
    conn=connect()
    if conn:
        cursorobj=conn.cursor()
        query ="SELECT * FROM admin"
        cursorobj.execute(query)
        result = cursorobj.fetchall()[0:-1] 
        for i in result:
            print("Username :",i)
            print("password :",i)
            break

fectch()
