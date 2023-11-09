# 17/08/2023  Thursdays
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox  
from tkinter import ttk,filedialog
import pyttsx3
from reportlab.lib import colors
import random
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import letter,landscape
import mysql.connector

a = tk.Tk()
a.title('Python Banking System')
a.geometry('800x675')
label_1 = tk.Label(a, text='\U0001F604 Welcome to the Python Banking System \U0001F604'.upper(), font=('Timeroman', 20,'bold'),fg='darkblue')
label_1.pack()

# --------------------------------------------MySql----------------------------------------------------------
try:
    con = mysql.connector.connect(host='localhost',username='root',password='',database='atm')
    print("Database Connected Successfully")
except:
    print('Error') 
mycur = con.cursor()

# -------------------------------------------------------------------------------------------------------------------


all_image_folder_path = 'A:/Python With DS/TKinter/Image/' #--------------------------------- All Photos Comman Path Set -------------------------------------

image_path = all_image_folder_path + 'bank_01.png' 
image = Image.open(image_path)
image = image.resize((400,400), Image.ANTIALIAS)
photo_01 = ImageTk.PhotoImage(image)
label_photo = tk.Label(image=photo_01)
label_photo.pack()
bold_font = ('Helvetica', 12, 'bold')

big_button_style = {
    'font': ('Helvetica', 14),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'green',  
    'activeforeground': 'white', 
    'borderwidth':0,
    'relief': 'ridge'    
}
red_button_style = {
    'font': ('Helvetica', 12),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'darkred',  
    'activeforeground': 'white', 
    'borderwidth': 0,
    'relief': 'ridge'    
}
big_red_button_style = {
    'font': ('Helvetica', 14),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'darkred',  
    'activeforeground': 'white', 
    'borderwidth': 0,
    'relief': 'ridge'    
}

button_style = {
    'font': ('Helvetica', 12),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'green',  
    'activeforeground': 'white', 
    'borderwidth': 0,
    'relief': 'ridge'    
}
    

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------Admin Sections ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

def open_admin_login_window():
    global username_entry, password_entry
    admin_login_window = tk.Toplevel(a)
    admin_login_window.title('Admin Login')
    admin_login_window.geometry('500x500')

   
    login_image_path = all_image_folder_path+'login_page_01.png'
    login_image = Image.open(login_image_path)
    login_image = login_image.resize((200,200), Image.ANTIALIAS)
    login_photo = ImageTk.PhotoImage(login_image)
    
    label_login_photo = tk.Label(admin_login_window, image=login_photo)
    label_login_photo.image = login_photo  
    label_login_photo.pack()

    admin_login_label = tk.Label(admin_login_window,text='ADMIN LOGIN',font=('Helvetica',16,'bold'))
    admin_login_label.pack(pady=10)


    username_label = tk.Label(admin_login_window,text="USERNAME -",font=('Helvetica',12,'bold '))
    username_label.place(x=20, y=300)

    username_entry = tk.Entry(admin_login_window,font=('Helvetica',12),width=30)
    username_entry.place(x=150, y=300,width=300)


    password_label = tk.Label(admin_login_window, text="PASSWORD -", font=('Helvetica', 12,'bold'))
    password_label.place(x=20, y=350)

    password_entry = tk.Entry(admin_login_window,font=('Helvetica',12),width=30)
    password_entry.place(x=150, y=350,width=300)


    back_button = tk.Button(admin_login_window,text='BACK',width=30,**red_button_style,command=lambda: back_to_main_window(admin_login_window))
    back_button.place(x=20,y=400,width=220)
    
    login_button = tk.Button(admin_login_window,text='LOGIN',width=30,**button_style,command=admin_login)
    login_button.place(x=250,y=400,width=220)

# --------------------------------------------------------------------------------------------------------------------------------------------------> 
def back_to_main_window(window):
    window.destroy()

def admin_login():
    
    global username_entry, password_entry ,entered_username
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    sqlQuery = "SELECT * FROM admin WHERE username='{}' AND password='{}'".format(entered_username, entered_password)
    mycur.execute(sqlQuery)
    admin_data = mycur.fetchall()
    if admin_data:
        messagebox.showinfo('Login Message',entered_username.upper()+" LOGIN SUCCESSFULLY ")
        admin_info_window()
    else:
        messagebox.showerror('Login Message',"invalid login")

def admin_info_window():
    global username_entry, password_entry ,entered_username
    admin_info_window = tk.Toplevel(a)
    admin_info_window.title('WELCOME '+entered_username.upper())
    admin_info_window.geometry('800x700')

   
    login_image_path = all_image_folder_path+'ac_01.png'
    login_image = Image.open(login_image_path)
    login_image = login_image.resize((400,300), Image.ANTIALIAS)
    login_photo = ImageTk.PhotoImage(login_image)
    
    label_login_photo = tk.Label(admin_info_window, image=login_photo)
    label_login_photo.image = login_photo  
    label_login_photo.pack()

    label_info = tk.Label(admin_info_window,text='ADMIN PANEL',font=('Helvetica',16,'bold'))
    label_info.pack(pady=5)



  
    button_1 = tk.Button(admin_info_window,text='CREATE NEW ACCOUNT',width=30,**big_button_style,command=createnewaccount)
    button_1.pack(pady=10)
    
    button_2 = tk.Button(admin_info_window,text='CHECK TOTAL BALANCE',width=30,**big_button_style,command=checkTotalBal)
    button_2.pack(pady=10)

    button_3 = tk.Button(admin_info_window,text='CHECK TOTAL ACCOUNT',width=30,**big_button_style,command=checktotalac)
    button_3.pack(pady=10)

    button_4 = tk.Button(admin_info_window,text='ADD NEW ADMIN',width=30,**big_button_style,command=addnewadmin)
    button_4.pack(pady=10)

    button_5 = tk.Button(admin_info_window,text='DELETE ADMIN ACCOUNT',width=30,**big_button_style,command=deleteadmin)
    button_5.pack(pady=10)

    button_6 = tk.Button(admin_info_window,text='LOGOUT',width=30,**big_red_button_style,command=lambda:back_to_main_window(admin_info_window))
    button_6.pack(pady=10)


    footer_frame = tk.Frame(admin_info_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

# __________________________________________create new account________________________________________________________________________________
def createnewaccount():
    global name_entry,city_entry,account_type_combobox,balance_entry,account_type_var
    create_ac_window = tk.Toplevel(a)
    create_ac_window.title('CREATE NEW ACCOUNT')
    create_ac_window.geometry('800x480')

    
    craete_image_path = all_image_folder_path+'newAccountCreateImg.png'
    create_image = Image.open(craete_image_path)
    create_image = create_image.resize((300,250), Image.ANTIALIAS)
    create_photo = ImageTk.PhotoImage(create_image)
    
    label_create_photo = tk.Label(create_ac_window, image=create_photo)
    label_create_photo.image = create_photo  
    label_create_photo.place(x=0,y=150)


    new_ac_label = tk.Label(create_ac_window,text='\U0001F604 CREATE NEW ACCOUNT \U0001F604',font=('Helvetica',16,'bold'),fg='darkblue')
    new_ac_label.place(x=380,y=100)

    
    name_label = tk.Label(create_ac_window,text="ENTER YOUR NAME: ",font=('Helvetica',12,'bold '))
    name_label.place(x=300, y=150)

    name_entry = tk.Entry(create_ac_window,font=('Helvetica',12),width=30)
    name_entry.place(x=520, y=150,width=250)


    city_label = tk.Label(create_ac_window, text="ENTER YOUR CITY:", font=('Helvetica', 12,'bold'))
    city_label.place(x=300, y=200)

    city_entry = tk.Entry(create_ac_window,font=('Helvetica',12),width=30)
    city_entry.place(x=520, y=200,width=250)
    
    account_type_label = tk.Label(create_ac_window, text="ACCOUNT TYPE: ", font=('Helvetica', 12, 'bold'))
    account_type_label.place(x=295, y=250)

    account_type_var = tk.StringVar()
    account_type_var.set('Savings Account')
    current_radio = tk.Radiobutton(create_ac_window, text='Current Account', variable=account_type_var, value='Current Account', font=('Helvetica', 12, 'bold'))
    current_radio.place(x=470, y=250)

    savings_radio = tk.Radiobutton(create_ac_window, text='Savings Account', variable=account_type_var, value='Savings Account', font=('Helvetica', 12, 'bold'))
    savings_radio.place(x=630, y=250)

    balance_label = tk.Label(create_ac_window, text="ENTER OPENING BALANCE: ", font=('Helvetica', 12,'bold'))
    balance_label.place(x=290, y=300)

    balance_entry = tk.Entry(create_ac_window,font=('Helvetica',12),width=30)
    balance_entry.place(x=520, y=300,width=250)


    logout = tk.Button(create_ac_window,text='BACK',width=35,**big_red_button_style,command=lambda:back_to_main_window(create_ac_window))
    logout.place(x=290,y=350,width=200)

    create = tk.Button(create_ac_window,text='CREATE',width=35,**big_button_style,command=createAccount)
    create.place(x=500,y=350,width=200)

    footer_frame = tk.Frame(create_ac_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

def createAccount():
    global name_entry,city_entry,account_type_combobox,balance_entry,account_type_var
    ac_pin=random.randrange(1000,9999)
    ac_no=random.randrange(100000000000,999999999999)
    name = name_entry.get()
    city = city_entry.get()
    acType = account_type_var.get()
    balance = balance_entry.get()
    confirm = messagebox.askyesno("CREATE ACCOUNT", f"Are you sure you want to create new account. {name}?".upper())
    if confirm :
        sqlQuery = "insert into createaccount values('{}','{}','{}','{}','{}','{}')".format(name,city,acType,balance,ac_no,ac_pin)
        mycur.execute(sqlQuery)
        con.commit()
        messagebox.showinfo('CREATE ACCOUNT',"ACCOUNT CREATED SUCCESSFULLY")
        create_account_window = tk.Toplevel(a)
        create_account_window.title('CREATE ACCOUNT')
        create_account_window.geometry('500x600')
        create_account_image_path = 'A:/Python With DS/TKinter/Image/createAccountInfo.png'
        create_account_image = Image.open(create_account_image_path)
        create_account_image =  create_account_image.resize((200,200), Image.ANTIALIAS)
        create_photo = ImageTk.PhotoImage(create_account_image)
        label_craete_photo = tk.Label(create_account_window, image=create_photo)
        label_craete_photo.image = create_photo  
        label_craete_photo.pack()
        

        label_info = tk.Label(create_account_window,text=f'{name.upper()} ACCOUNT CREATED SUCCESSFULLY',font=('Helvetica',12,'bold'))
        label_info.pack()
        style = ttk.Style(a)
        style.theme_use("winnative")
        style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background='#FFD700', foreground='black')
        tree = ttk.Treeview(create_account_window, columns=("Info", "Value"), show="headings")
        tree.heading("Info", text="BANK")
        tree.heading("Value", text="PASSBOOK")
        tree.pack()
        
        tree.insert("", "end", values=("Name", name))
        tree.insert("", "end", values=("City", city))
        tree.insert("", "end", values=("Account Type", acType))
        tree.insert("", "end", values=("Balance", balance))
        tree.insert("", "end", values=("Account Number", ac_no))
        tree.insert("", "end", values=("PIN", ac_pin))

        footer_frame = tk.Frame(create_account_window, height=10)
        footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
        footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
        footer_label.pack(pady=5)
        def generate_and_download_passbook(name, city, acType, balance, ac_no, ac_pin):
            doc = SimpleDocTemplate("bank_passbook.pdf", pagesize=landscape(letter))

            account_info = [
                ["Name", name],
                ["City", city],
                ["Account Type", acType],
                ["Balance", balance],
                ["Account Number", ac_no],
                ["PIN", ac_pin],
            ]
            

            table_data = []
            for item in account_info:
                table_data.append(item)

            table = Table(table_data, colWidths=[200, 300])
            table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
                ('FONTSIZE', (0, 0), (-1, -1), 14),
                ('GRID', (0, 0), (-1, -1), 1, '#d5dbdb'),
            ]))
            doc.build([table])
            messagebox.showinfo("Passbook Created", "Bank passbook PDF created successfully.".upper())
            return "bank_passbook.pdf"

        def save_and_download_pdf():
            pdf_filename = generate_and_download_passbook(name, city, acType, balance, ac_no, ac_pin)
            destination = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

            if destination:
                import shutil
                shutil.move(pdf_filename, destination)
                messagebox.showinfo("Download Complete", f"PDF saved as {destination}")
        generate_passbook_button = tk.Button(create_account_window, text='PRINT PASSBOOK', width=35, **big_button_style, command=save_and_download_pdf)
        generate_passbook_button.pack(pady=10)

    else:
        messagebox.showerror('CREATE ACCOUNT',"ACCOUNT NOT CREATED")
     




# ______________________________________________________Check Total Amount ________________________________________________________________________
def checkTotalBal():
    sqlQuery="SELECT SUM(opening_balanace) FROM createaccount"
    mycur.execute(sqlQuery)
    total_account = mycur.fetchall()[0]
    con.commit()
    messagebox.showinfo('TOTAL BALANCE',"TOTAL BALANCE RS.{}".format(total_account))
    admin_info_window()
# ________________________________________________________Check Total Account ________________________________________________________________________
def checktotalac():
    def generate_pdf():
        doc = SimpleDocTemplate("TotalAccounts.pdf", pagesize=letter)
        elements = []

        data = [['Name', 'City', 'Account Type', 'Balance', 'Account Number', 'PIN']]

        for item in table.get_children():
            values = [table.item(item, "values")[i] for i in range(6)]
            data.append(values)

        t = Table(data)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), '#3498db'),
            ('TEXTCOLOR', (0, 0), (-1, 0), 'white'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), '#ecf0f1'),
            ('GRID', (0, 0), (-1, -1), 1, '#d5dbdb'),
        ]))

        elements.append(t)
        doc.build(elements)
    def save_pdf():
        generate_pdf()
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            import shutil
            shutil.move("TotalAccounts.pdf", file_path)

    a = tk.Tk()
    a.geometry('1200x400')
    a.title('TOTAL ACCOUNTS')

    label_1 = tk.Label(a, text="TOTAL ACCOUNTS ", font=('Times', 14, 'bold'))
    label_1.pack()

    style = ttk.Style(a)
    style.theme_use("winnative")
    style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background='#3498db', foreground='white')
    
    table = ttk.Treeview(a, columns=('Name', 'City', 'AccountType', 'Balance', 'AccountNumber', 'Pin'), show='headings')
    table.heading('Name', text='NAME')
    table.heading('City', text='CITY')
    table.heading('AccountType', text='ACCOUNT TYPE')
    table.heading('Balance', text='BALANCE')
    table.heading('AccountNumber', text='ACCOUNT NUMBER')
    table.heading('Pin', text='PIN')
    table.pack()

    sqlQuery = "SELECT * FROM createaccount"
    mycur.execute(sqlQuery)
    all_accounts = mycur.fetchall()

    for item in all_accounts:
        table.insert('', 'end', values=item)

    save_pdf_button = tk.Button(a, text="Download PDF", command=save_pdf,width=20,font=('Helvetica',12,'bold'),bg='red')
    save_pdf_button.pack(pady=50)

# _____________________________________________________Add New ADMIN __________________________________________________________________________________
def addnewadmin():
    global username_entry,password_entry
    addnewadmin_window = tk.Toplevel(a)
    addnewadmin_window.title("ADD NEW ADMIN")
    addnewadmin_window.geometry('500x500')

    addnewadmin_image_path =all_image_folder_path+'addnewadmin.png'
    addnewadmin_image = Image.open(addnewadmin_image_path).resize((300,250))
    addnewadmin_image = ImageTk.PhotoImage(addnewadmin_image)
    label_addnewadmin_image = tk.Label(addnewadmin_window, image=addnewadmin_image )
    label_addnewadmin_image .image = addnewadmin_image
    label_addnewadmin_image.pack()
        
    addnewadmin = tk.Label(addnewadmin_window,text='ADD NEW ADMIN',font=('Timeroman',16,'bold'))
    addnewadmin.pack()
 
    username_label = tk.Label(addnewadmin_window,text="NEW USERNAME -",font=('Helvetica',12,'bold '))
    username_label.place(x=20, y=300)

    username_entry = tk.Entry(addnewadmin_window,font=('Helvetica',12),width=30)
    username_entry.place(x=170, y=300,width=300)

    password_label = tk.Label(addnewadmin_window, text="NEW PASSWORD -", font=('Helvetica', 12,'bold'))
    password_label.place(x=20, y=350)

    password_entry = tk.Entry(addnewadmin_window,font=('Helvetica',12),width=30)
    password_entry.place(x=170, y=350,width=300)

    back_button = tk.Button(addnewadmin_window,text='BACK',width=30,**red_button_style,command=lambda: back_to_main_window(addnewadmin_window))
    back_button.place(x=20,y=400,width=220)
    
    login_button = tk.Button(addnewadmin_window,text='ADD ADMIN',width=30,**button_style,command=newadmin)
    login_button.place(x=250,y=400,width=220)

def newadmin():
    global username_entry,password_entry
    new_username = username_entry.get()
    new_password = password_entry.get()
    sqlQuery="insert into admin values ('{}','{}')".format(new_username,new_password)       
    mycur.execute(sqlQuery)
    con.commit()
    messagebox.showinfo("Confirm","NEW ADMIN ADDED")  
    admin_info_window()

# _____________________________________________________________DELETE ADMIN ACCOUNT___________________________________________________________________________________

def deleteadmin():
    global username_entry, password_entry
    admin_username = username_entry.get()
    admin_password = password_entry.get()
    sqlQuery="DELETE FROM admin where username='{}' AND password='{}'".format(admin_username,admin_password)
    mycur.execute(sqlQuery)
    con.commit()
    confirmation = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the admin account {admin_username}?".upper())
    if confirmation:
        sqlQuery = "DELETE FROM admin WHERE username='{}' AND password='{}'".format(admin_username, admin_password)
        mycur.execute(sqlQuery)
        con.commit()
        messagebox.showinfo("Delete Account", "Admin account deleted successfully".upper())
        open_admin_login_window()
    else:
        messagebox.showerror("Delete Account", "Admin account not deleted".upper())
        admin_info_window()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------User sections ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

def user_login():
    global account_entry,pin_entry,dop_entry,balance,entered_account,entered_pin,with_entry
    enterd_user_account = account_entry.get()
    enterd_user_pin = pin_entry.get()

    sqlQuery="SELECT *  FROM createaccount WHERE account_number=%s AND pin=%s"
    mycur.execute(sqlQuery,(enterd_user_account,enterd_user_pin))
    user_data = mycur.fetchone()
  
    if user_data:
         messagebox.showinfo("User Login", "Login Successfully")
         user_panel()
    else:
        messagebox.showerror("User Login", "Invalid login")

def open_user_login_window():
    global account_entry,pin_entry,dop_entry,balance,entered_account,entered_pin,with_entry
    global account_entry,pin_entry
    user_login_window = tk.Toplevel(a)
    user_login_window.title('User Login')
    user_login_window.geometry('500x500')

   
    user_login_image_path = all_image_folder_path+'userloginlogo2.png'
    user_login_image = Image.open(user_login_image_path)
    user_login_image = user_login_image.resize((350,250), Image.ANTIALIAS)
    user_login_photo= ImageTk.PhotoImage(user_login_image)
    
    user_label_login_photo = tk.Label(user_login_window, image=user_login_photo)
    user_label_login_photo.image = user_login_photo  
    user_label_login_photo.pack()

    user_login_label = tk.Label(user_login_window,text='USER LOGIN',font=('Timeroman',16,'bold'))
    user_login_label.pack(pady=5)


    account_label = tk.Label(user_login_window,text="ACCOUNT NUMBER -",font=('Helvetica',12,'bold'))
    account_label.place(x=20,y=300)

    account_entry = tk.Entry(user_login_window,font=('Timeroman',12),width=30)
    account_entry.place(x=200,y=300,width=250)


    pin_label = tk.Label(user_login_window, text="PIN NUMBER -", font=('Helvetica', 12,'bold'))
    pin_label.place(x=20,y=350)

    pin_entry = tk.Entry(user_login_window,font=('Timeroman',12),width=30)
    pin_entry.place(x=200,y=350,width=250)

   
    login_button = tk.Button(user_login_window,text='LOGIN',width=30,**button_style,command=user_login)
    login_button.place(x=250,y=400,width=200)

    
    back_button = tk.Button(user_login_window,text='BACK',width=30,**red_button_style,command=lambda:back_to_main_window(user_login_window))
    back_button.place(x=20,y=400,width=200)

def user_panel():
    user_panel_window = tk.Toplevel(a)
    user_panel_window.title('WELCOME')
    user_panel_window.geometry('800x680')
    
    user_panel_image_path = all_image_folder_path+'user_panel_logo2.png'
    user_panel_image = Image.open(user_panel_image_path)
    user_panel_image = user_panel_image.resize((350,250), Image.ANTIALIAS)
    user_login_photo= ImageTk.PhotoImage(user_panel_image)
    
    user_label_panel_photo = tk.Label(user_panel_window, image=user_login_photo)
    user_label_panel_photo.image =  user_login_photo  
    user_label_panel_photo.pack()

  
    user_panel_label_01 = tk.Label(user_panel_window,text='USER PANEL',font=('Timeroman',16,'bold'))
    user_panel_label_01.pack(pady=10)

    button_1 = tk.Button(user_panel_window,text='DIPOSIT',width=30,**big_button_style,command=diposit)
    button_1.pack(pady=10)
    
    button_2 = tk.Button(user_panel_window,text='WITHDRAWAL',width=30,**big_button_style,command=withdrawal) 
    button_2.pack(pady=10)

    button_3 = tk.Button(user_panel_window,text='INFORMATION',width=30,**big_button_style,command=info)
    button_3.pack(pady=10)

    button_4 = tk.Button(user_panel_window,text='UPDATE INFORMATION',width=30,**big_button_style,command=updateinfo)
    button_4.pack(pady=10)

    button_5 = tk.Button(user_panel_window,text='CHANGE PIN',width=30,**big_button_style,command=changepin)
    button_5.pack(pady=10)

    button_6 = tk.Button(user_panel_window,text='LOGOUT',width=30,**big_red_button_style,command=lambda:back_to_main_window(user_panel_window))
    button_6.pack(pady=10)

    footer_frame = tk.Frame(user_panel_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

# ____________________________________________________________Deposit_______________________________________________________________________________________________________

def diposit():
    global account_entry,pin_entry,dop_entry,balance,entered_account,entered_pin
    entered_account = account_entry.get()
    entered_pin =pin_entry.get()
    
    sqlQuery="select opening_balanace from createaccount where account_number='{}' and pin='{}'".format(entered_account,entered_pin)
    mycur.execute(sqlQuery)
    balance = mycur.fetchone()[0]
    con.commit()

    deposit_window = tk.Toplevel(a)
    deposit_window.title("DEPOSIT")
    deposit_window.geometry('500x500')

    deposit_image_path = all_image_folder_path+'diposit.png'
    deposit_image = Image.open(deposit_image_path).resize((350,250))
    deposit_image = ImageTk.PhotoImage(deposit_image)
    label_deposit_image = tk.Label(deposit_window, image=deposit_image )
    label_deposit_image .image = deposit_image
    label_deposit_image.pack()
        
    dop_label = tk.Label(deposit_window,text='DEPOSIT AMOUNT',font=('Timeroman',16,'bold'))
    dop_label.pack()
    
    dop_label_bal = tk.Label(deposit_window,text='YOUR CURRENT BALANCE IS : ' +balance,font=('Timeroman',10,'bold'))
    dop_label_bal.pack()

    dop_label2 = tk.Label(deposit_window,text='ENTER AMOUNT TO DEPOSIT :',font=('Timeroman',11,'bold'))
    dop_label2.place(x=10,y=350)

    dop_entry = tk.Entry(deposit_window,font=('Timeroman',12),width=30)
    dop_entry.place(x=250,y=350,width=210)

    dop_button = tk.Button(deposit_window,text='DEPOSIT',**big_button_style,command=dipoAmount)
    dop_button.place(x=240,y=400,width=220)
    dop_button_back = tk.Button(deposit_window,text='BACK',**big_red_button_style,command=lambda:back_to_main_window(deposit_window))
    dop_button_back.place(x=10,y=400,width=220)

    footer_frame = tk.Frame(deposit_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)    

def dipoAmount():
    global account_entry,pin_entry,dop_entry,balance,entered_account,entered_pin
    amount = dop_entry.get()
    total_amount = float((float)(balance)+ (float)((amount)))
    sqlQuery = "UPDATE createaccount SET opening_balanace='{}' where account_number='{}' and pin='{}'".format(total_amount,entered_account,entered_pin)
    mycur.execute(sqlQuery)
    con.commit()
    messagebox.showinfo("DIPOSIT BALANCE","Amount Deposited Successfully Rs.{} \nYour Current Balance is Rs.{}".format(amount,total_amount))
    user_panel()
# ____________________________________________________________Withdrawal_______________________________________________________________________________________________________

def withdrawal():
    global account_entry,pin_entry,dop_entry,balance,entered_account,entered_pin,with_entry
    entered_account = account_entry.get()
    entered_pin = pin_entry.get()
    
    sqlQuery="select opening_balanace from createaccount where account_number='{}' and pin='{}'".format(entered_account,entered_pin)
    mycur.execute(sqlQuery)
    balance = mycur.fetchone()[0]
    con.commit()

    withdrawal_window = tk.Toplevel(a)
    withdrawal_window.title("WITHDRAWAL")
    withdrawal_window.geometry('500x500')

    withdrawal_image_path = all_image_folder_path+'withdrawal.png'
    withdrawal_image = Image.open(withdrawal_image_path).resize((350,250))
    withdrawal_image = ImageTk.PhotoImage(withdrawal_image)
    label_withdrawal_image = tk.Label(withdrawal_window, image=withdrawal_image )
    label_withdrawal_image.image = withdrawal_image
    label_withdrawal_image.pack()
    
    
    with_label = tk.Label(withdrawal_window,text='WITHDRAWAL AMOUNT',font=('Timeroman',16,'bold'))
    with_label.pack()

    with_label_bal = tk.Label(withdrawal_window,text='YOUR CURRENT BALANCE IS : ' +balance,font=('Timeroman',10,'bold'))
    with_label_bal.pack()
    
    with_label2 = tk.Label(withdrawal_window,text='ENTER AMOUNT TO DEPOSIT :',font=('Timeroman',11,'bold'))
    with_label2.place(x=10,y=350)

    with_entry = tk.Entry(withdrawal_window,font=('Timeroman',12),width=30)
    with_entry.place(x=250,y=350,width=210)

    with_button = tk.Button(withdrawal_window,text='WITHDRAWAL',**big_button_style,command=withAmount)
    with_button.place(x=240,y=400,width=220)

    with_button_back = tk.Button(withdrawal_window,text='BACK',**big_red_button_style,command=lambda:back_to_main_window(withdrawal_window))
    with_button_back.place(x=10,y=400,width=220)

    footer_frame = tk.Frame(withdrawal_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

def withAmount():
    global account_entry,pin_entry,dop_entry,balance,entered_account,entered_pin,with_entry
    amount = with_entry.get()
    total_amount = float((float)(balance)+(float)((amount)))
    sqlQuery = "UPDATE createaccount SET opening_balanace='{}' where account_number='{}' and pin='{}'".format(total_amount,entered_account,entered_pin)
    mycur.execute(sqlQuery)
    con.commit()
    if int((int)(amount)>(float)(balance)):
        messagebox.showerror('WITHDRWAL MESSAGE',"Insufficient balance, You can't Withdraw this much money".upper())
        user_panel()
    else:
        result=float((float)(balance)-(int)(amount))
        sqlQuery = "UPDATE createaccount SET opening_balanace='{}' where account_number='{}' and pin='{}'".format(result,entered_account,entered_pin)
        mycur.execute(sqlQuery)
        con.commit()
        messagebox.showinfo('WITHDRWAL MESSAGE',"You have Successfully withdrawal Rs.{}\nYour Current Balance is Rs.{}".format(amount,result))
        user_panel()
# _______________________________________________________________INFORATION_____________________________________________________________________________________

def info():
    global account_entry,pin_entry,dop_entry,balance,entered_account,entered_pin,with_entry
    enterd_user_account = account_entry.get()
    enterd_user_pin = pin_entry.get()

    sqlQuery = "SELECT * FROM createaccount WHERE account_number='{}' AND pin='{}'".format(enterd_user_account,enterd_user_pin)
    mycur.execute(sqlQuery)
    all_accounts = mycur.fetchall()

    a = tk.Tk()
    a.geometry('1200x400')
    a.title('INFORMATIONS')

    label_1 = tk.Label(a, text="INFORMATIONS", font=('Times', 14, 'bold'))
    label_1.pack()

    style = ttk.Style(a)
    style.theme_use("winnative")
    style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background='#3498db', foreground='white')
    style.configure("Treeview", background="white", rowheight=30, font=('Helvetica', 12))

    table = ttk.Treeview(a, columns=('Name', 'City', 'AccountType', 'Balance', 'AccountNumber', 'Pin'), show='headings')
    table.heading('Name', text='NAME')
    table.heading('City', text='CITY')
    table.heading('AccountType', text='ACCOUNT TYPE')
    table.heading('Balance', text='BALANCE')
    table.heading('AccountNumber', text='ACCOUNT NUMBER')
    table.heading('Pin', text='PIN')
    table.pack()
    for item in all_accounts:
        table.insert('', 'end', values=item)
    
    footer_frame = tk.Frame(a, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

# __________________________________________________________UPDATE INFORMATIONS_______________________________________________________________________________
def updateinfo():
    update_window = tk.Toplevel(a)
    update_window.title('UPDATE INFORMATIONS')
    update_window.geometry('800x480')

    
    update_image_path = all_image_folder_path+'update.png'
    update_image = Image.open(update_image_path)
    update_image = update_image.resize((300,250), Image.ANTIALIAS)
    update_photo = ImageTk.PhotoImage(update_image)
    
    label_update_photo = tk.Label(update_window, image=update_photo)
    label_update_photo.image = update_photo  
    label_update_photo.place(x=0,y=130)


    new_ac_label = tk.Label(update_window,text='\U0001F604 UPDATE INFORMATIONS \U0001F604',font=('Helvetica',16,'bold'),fg='darkblue')
    new_ac_label.place(x=360,y=100)

    logout = tk.Button(update_window,text='UPDATE NAME',width=35,**big_button_style,command=updatename)
    logout.place(x=290,y=150,width=410)

    create = tk.Button(update_window,text='UPDATE CITY',width=35,**big_button_style,command=updatecity)
    create.place(x=290,y=200,width=410)

    logout = tk.Button(update_window,text='UPDATE AC TYPE',width=35,**big_button_style,command=updateactype)
    logout.place(x=290,y=250,width=410)

    
    logout = tk.Button(update_window,text='BACK',width=35,**big_red_button_style,command=lambda:back_to_main_window(update_window))
    logout.place(x=290,y=300,width=410)

    footer_frame = tk.Frame(update_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)



def updatename():
    global updatename_entry
    updatename_window = tk.Toplevel(a)
    updatename_window.title("UPDATE NAME")
    updatename_window.geometry('500x500')

    updatename_window_image_path =  all_image_folder_path+'UPPDATENAME.png'
    updatename_image = Image.open(updatename_window_image_path).resize((330,250))
    updatename_image = ImageTk.PhotoImage(updatename_image)

    label_updatename_image = tk.Label(updatename_window, image=updatename_image )
    label_updatename_image.image = updatename_image
    label_updatename_image.pack()
    
    
    with_label = tk.Label(updatename_window,text='UPDATE NAME',font=('Timeroman',16,'bold'))
    with_label.pack()
    
    with_label2 = tk.Label(updatename_window,text='ENTER NEW NAME - ',font=('Timeroman',11,'bold'))
    with_label2.place(x=10,y=350)

    updatename_entry = tk.Entry(updatename_window,font=('Timeroman',12),width=30)
    updatename_entry.place(x=190,y=350,width=280)

    with_button = tk.Button(updatename_window,text='UPDATE',**big_button_style,command=updatenameGUI)
    with_button.place(x=240,y=400,width=220)

    with_button_back = tk.Button(updatename_window,text='BACK',**big_red_button_style,command=lambda:back_to_main_window(updatename_window))
    with_button_back.place(x=10,y=400,width=220)

    footer_frame = tk.Frame(updatename_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

def updatenameGUI():
    global account_entry,pin_entry,dop_entry,balance,entered_account,entered_pin,with_entry,updatename_entry
    enterd_user_account = account_entry.get()
    enterd_user_pin = pin_entry.get()
    entered_name = updatename_entry.get()

    confirmation = messagebox.askyesno("UPDATE NAME", f"Are you sure you want to update name {entered_name}".upper())
    if confirmation:
        sqlQuery="update createaccount set name='{}' where account_number='{}' and pin='{}'".format(entered_name,enterd_user_account,enterd_user_pin)
        mycur.execute(sqlQuery)
        con.commit()
        messagebox.showinfo('UPDATE NAME',f'NAME UPDATED SUCCESSFUL ! NEW NAME {entered_name}')
        user_panel()
    else:
        messagebox.showerror("UPDATE NAME", "NOT UPDATE NAME".upper())
        updateinfo()

    

# ______________________________________________________________UPDATE CITY _________________________________________________________________________


def updatecity():
    global updatecity_entry
    updatecity_window = tk.Toplevel(a)
    updatecity_window.title("UPDATE CITY")
    updatecity_window.geometry('500x500')

    updatename_window_image_path =all_image_folder_path+'UPPDATENAME.png'
    updatename_image = Image.open(updatename_window_image_path).resize((330,250))
    updatename_image = ImageTk.PhotoImage(updatename_image)

    label_updatename_image = tk.Label(updatecity_window, image=updatename_image )
    label_updatename_image.image = updatename_image
    label_updatename_image.pack()
    
    
    with_label = tk.Label(updatecity_window,text='UPDATE NAME',font=('Timeroman',16,'bold'))
    with_label.pack()
    
    with_label2 = tk.Label(updatecity_window,text='ENTER NEW CITY -',font=('Timeroman',11,'bold'))
    with_label2.place(x=10,y=350)

    updatecity_entry = tk.Entry(updatecity_window,font=('Timeroman',12),width=30)
    updatecity_entry.place(x=190,y=350,width=280)

    with_button = tk.Button(updatecity_window,text='UPDATE',**big_button_style,command=updatecityGUI)
    with_button.place(x=240,y=400,width=220)

    with_button_back = tk.Button(updatecity_window,text='BACK',**big_red_button_style,command=lambda:back_to_main_window(updatecity_window))
    with_button_back.place(x=10,y=400,width=220)

    footer_frame = tk.Frame(updatecity_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)


def updatecityGUI():
    global account_entry,pin_entry,updatecity_entry
    enterd_user_account = account_entry.get()
    enterd_user_pin = pin_entry.get()
    entered_city = updatecity_entry.get()

    confirmation = messagebox.askyesno("UPDATE NAME", f"Are you sure you want to update name {entered_city}".upper())
    if confirmation:
        sqlQuery="update createaccount set city='{}' where account_number='{}' and pin='{}'".format(entered_city,enterd_user_account,enterd_user_pin)
        mycur.execute(sqlQuery)
        con.commit()
        messagebox.showinfo('UPDATE CITY',f'CITY UPDATED SUCCESSFUL ! NEW NAME {entered_city}')
        user_panel()
    else:
        messagebox.showerror("UPDATE CITY", "NOT UPDATE CITY".upper())
        user_panel()


# _________________________________________________UPDATE ACCOUNT TYPE ___________________________________________________________________________________
def updateactype():
    global account_type_combobox_update,account_type_var
    updateactype_window = tk.Toplevel(a)
    updateactype_window.title("UPDATE ACCOUNT TYPE")
    updateactype_window.geometry('500x500')

    updatename_window_image_path =all_image_folder_path+'UPPDATENAME.png'
    updatename_image = Image.open(updatename_window_image_path).resize((330,250))
    updatename_image = ImageTk.PhotoImage(updatename_image)

    label_updatename_image = tk.Label(updateactype_window, image=updatename_image )
    label_updatename_image.image = updatename_image
    label_updatename_image.pack()
    
    
    with_label = tk.Label(updateactype_window,text='UPDATE ACCOUNT TYPE',font=('Timeroman',16,'bold'))
    with_label.pack()
    
    with_label2 = tk.Label(updateactype_window,text='ENTER NEW ACCOUNT TYPE - ',font=('Timeroman',11,'bold'))
    with_label2.place(x=10,y=350)

    account_type_var = tk.StringVar()
    account_type_var.set('Savings Account')
    current_radio = tk.Radiobutton(updateactype_window, text='Current Account', variable=account_type_var, value='Current Account', font=('Helvetica', 12, 'bold'))
    current_radio.place(x=250, y=350)

    savings_radio = tk.Radiobutton(updateactype_window, text='Savings Account', variable=account_type_var, value='Savings Account', font=('Helvetica', 12, 'bold'))
    savings_radio.place(x=410, y=350)

    with_button = tk.Button(updateactype_window,text='UPDATE',**big_button_style,command=updateacTypeGUI)
    with_button.place(x=240,y=400,width=220)

    with_button_back = tk.Button(updateactype_window,text='BACK',**big_red_button_style,command=lambda:back_to_main_window(updateactype_window))
    with_button_back.place(x=10,y=400,width=220)

    footer_frame = tk.Frame(updateactype_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

def updateacTypeGUI():
    global account_entry,pin_entry,account_type_combobox_update,account_type_var
    enterd_user_account = account_entry.get()
    enterd_user_pin = pin_entry.get()
    entered_acType = account_type_var.get()

    confirmation = messagebox.askyesno("UPDATE NAME", f"Are you sure you want to update Account Type {entered_acType}".upper())
    if confirmation:
        sqlQuery="update createaccount set account_type='{}' where account_number='{}' and pin='{}'".format(entered_acType,enterd_user_account,enterd_user_pin)
        mycur.execute(sqlQuery)
        con.commit()
        messagebox.showinfo('UPDATE ACCOUNT TYPE',f'ACCOUNT TYPE UPDATED SUCCESSFUL ! NEW NAME {entered_acType}')
        user_panel()
    else:
        messagebox.showerror("UPDATE ACCOUNT TYPE", "NOT UPDATE ACCOUNT TYPE".upper())
        user_panel()


# _________________________________________________________________CHANGE PIN __________________________________________________________________________________
def changepin():
    global old_pin_entry
    changepin_window = tk.Toplevel(a)
    changepin_window.title("CHANGE PIN")
    changepin_window.geometry('500x500')

    changepin_image_path = all_image_folder_path+'changepin.png'
    changepin_image = Image.open(changepin_image_path).resize((370,300))
    changepin_image = ImageTk.PhotoImage(changepin_image)

    label_changepin_image = tk.Label(changepin_window, image=changepin_image )
    label_changepin_image.image = changepin_image
    label_changepin_image.pack()
    
    
    with_label = tk.Label(changepin_window,text='CHANGE PIN',font=('Timeroman',16,'bold'))
    with_label.pack()

    with_label2 = tk.Label(changepin_window,text='ENTER OLD PIN :',font=('Timeroman',11,'bold'))
    with_label2.place(x=10,y=350)

    old_pin_entry = tk.Entry(changepin_window,font=('Timeroman',12),width=30)
    old_pin_entry.place(x=150,y=350,width=300)

    with_button = tk.Button(changepin_window,text='CHANGE PIN',**big_button_style,command=pin)
    with_button.place(x=240,y=400,width=220)

    with_button_back = tk.Button(changepin_window,text='BACK',**big_red_button_style,command=lambda:back_to_main_window(changepin_window))
    with_button_back.place(x=10,y=400,width=220)

    footer_frame = tk.Frame(changepin_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

def pin():
    global old_pin_entry,pin_entry,new_pin_entry
    user_pin = pin_entry.get()
    old_pin = old_pin_entry.get()
    entered_username = account_entry.get()
    if user_pin==old_pin:
            changepin_window = tk.Toplevel(a)
            changepin_window.title("NEW PIN")
            changepin_window.geometry('500x500')

            changepin_image_path = all_image_folder_path+'changepin.png'
            changepin_image = Image.open(changepin_image_path).resize((370,300))
            changepin_image = ImageTk.PhotoImage(changepin_image)

            label_changepin_image = tk.Label(changepin_window, image=changepin_image )
            label_changepin_image.image = changepin_image
            label_changepin_image.pack()
            
            
            with_label = tk.Label(changepin_window,text='NEW PIN',font=('Timeroman',16,'bold'))
            with_label.pack()

            with_label2 = tk.Label(changepin_window,text='ENTER 4 DIGITS NEW PIN :',font=('Timeroman',11,'bold'))
            with_label2.place(x=10,y=350)

            new_pin_entry = tk.Entry(changepin_window,font=('Timeroman',12),width=30)
            new_pin_entry.place(x=210,y=350,width=260)

            with_button = tk.Button(changepin_window,text='SET PIN',**big_button_style,command=setpin)
            with_button.place(x=240,y=400,width=220)

            with_button_back = tk.Button(changepin_window,text='BACK',**big_red_button_style,command=lambda:back_to_main_window(changepin_window))
            with_button_back.place(x=10,y=400,width=220)

            footer_frame = tk.Frame(changepin_window, height=10)
            footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
            footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
            footer_label.pack(pady=5)
    else:
        messagebox.showerror('WRONG OLD PIN',"ENTER CORRECT OLD PIN!")
        user_panel()
def setpin():
    global old_pin_entry,pin_entry,new_pin_entry
    new_pin_entry = new_pin_entry.get()
    user_pin = pin_entry.get()
    entered_username = account_entry.get()
    sqlQuery="update createaccount set pin ='{}' where account_number='{}' and  pin='{}'".format(new_pin_entry,entered_username,user_pin)
    mycur.execute(sqlQuery)
    con.commit()
    messagebox.showinfo('NEW PIN','PIN CHANGE SUCCESSFUL !')
    user_panel()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------Exit----------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
def Exit_app():
    a.quit()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
button_01 = tk.Button(a,text='ADMIN LOGIN',width=30,**big_button_style,command=open_admin_login_window)
button_01.pack(pady=10)

button_02 = tk.Button(a,text='USER LOGIN',width=30,**big_button_style,command=open_user_login_window)
button_02.pack(pady=10)

button_03 = tk.Button(a,text='EXIT',width=30,**big_red_button_style,command=Exit_app)
button_03.pack(pady=10)
# -----------------------------------------------------------------Footer---------------------------------------------------------------------------------------
footer_frame = tk.Frame(a, height=10)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
footer_label.pack(pady=5)
a.mainloop()

# Completed Date 
# 20/08/2023
