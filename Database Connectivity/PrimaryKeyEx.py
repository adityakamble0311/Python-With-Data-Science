import mysql.connector
import datetime as date
try:
    con = mysql.connector.connect(host='localhost',username='root',password='Aditya@12072004@',database='adityadb')
    print("Connected")
except:
    print("Error")
mycur = con.cursor()
date1 = date.datetime.now()
c =  input()
d = input()
sql = "INSERT INTO transections VALUES('{}','{}','{}')".format(c,d,date1)
mycur.execute(sql)
con.commit()
print("Inserted")