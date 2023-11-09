import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector

def set_row_colors():
    for i, item in enumerate(table.get_children()):
        if i % 2 == 0:
            table.item(item, tags=('even',))
        else:
            table.item(item, tags=('odd',))

try:
    con = mysql.connector.connect(host='localhost', username='root', password='Aditya@12072004@', database='atm')
    print("Database Connected Successfully")
except mysql.connector.Error as err:
    print('Error:', err)

mycur = con.cursor()

a = tk.Tk()
a.geometry('1200x400')
a.title('INFORMATIONS')

label_1 = tk.Label(a, text="INFORMATIONS", font=('Times', 14, 'bold'))
label_1.pack()

style = ttk.Style(a)
style.theme_use("winnative")
style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background='#3498db', foreground='white')
style.configure("Treeview", background="#ecf0f1", fieldbackground="#ecf0f1", rowheight=30, font=('Helvetica', 11))

table = ttk.Treeview(a, columns=('Name', 'City', 'AccountType', 'Balance', 'AccountNumber', 'Pin'), show='headings')
table.heading('Name', text='NAME')
table.heading('City', text='CITY')
table.heading('AccountType', text='ACCOUNT TYPE')
table.heading('Balance', text='BALANCE')
table.heading('AccountNumber', text='ACCOUNT NUMBER')
table.heading('Pin', text='PIN')
table.pack()

table.tag_configure('even', background='#d5dbdb')
table.tag_configure('odd', background='#FFD700')

sqlQuery = "SELECT * FROM createaccount"
mycur.execute(sqlQuery)
all_accounts = mycur.fetchall()

for item in all_accounts:
    table.insert('', 'end', values=item)

set_row_colors()

a.mainloop()
