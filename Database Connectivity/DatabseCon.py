import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user='root',
    password='Aditya@12072004@',
    database = 'adityadb'
)
curObj=con.cursor()
if con:
    # print("Database Connected Successfully !")
   curObj.execute("""CREATE TABLE IF NOT EXISTS employee (
    id INT AUTO_INCREMENT PRIMARY KEY, NAME VARCHAR(20), CITY VARCHAR(30) 
    )""")


else:
    print('Error in Connection')

con.close()