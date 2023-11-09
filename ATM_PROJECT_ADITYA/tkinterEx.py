import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox  
import pyttsx3
import mysql.connector

a = tk.Tk()
a.title('Python Banking System')
a.geometry('800x675')
label_1 = tk.Label(a, text='🙂 Welcome to the Python Banking System 🙂'.upper(), font=('Timeroman', 20,'bold'),fg='darkblue')
label_1.pack()

# --------------------------------------------MySql----------------------------------------------------------
try:
    con = mysql.connector.connect(host='localhost',username='root',password='Aditya@12072004@',database='atm')
    print("Database Connected Successfully")
except:
    print('Error') 
mycur = con.cursor()

# -------------------------------------------------------------------------------------------------------------------

image_path = 'A:/Python With DS/TKinter/Image/bank_01.png'
image = Image.open(image_path)
image = image.resize((400,400), Image.ANTIALIAS)
photo_01 = ImageTk.PhotoImage(image)
label_photo = tk.Label(image=photo_01)
label_photo.pack()
bold_font = ('Helvetica', 12, 'bold')

button_style = {
    'font': ('Helvetica', 14),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'green',  
    'activeforeground': 'white', 
    'borderwidth': 2,
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


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------Admin Sections ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

def open_admin_login_window():
    global username_entry, password_entry
    admin_login_window = tk.Toplevel(a)
    admin_login_window.title('Admin Login')
    admin_login_window.geometry('500x500')

   
    login_image_path = 'A:/Python With DS/TKinter/Image/login_page_01.png'
    login_image = Image.open(login_image_path)
    login_image = login_image.resize((200,200), Image.ANTIALIAS)
    login_photo = ImageTk.PhotoImage(login_image)
    
    label_login_photo = tk.Label(admin_login_window, image=login_photo)
    label_login_photo.image = login_photo  
    label_login_photo.pack()

    admin_login_label = tk.Label(admin_login_window,text='ADMIN LOGIN',font=('Timeroman',16,'bold'))
    admin_login_label.pack(pady=10)


    username_label = tk.Label(admin_login_window,text="USERNAME -",font=('Helvetica',12,'bold '))
    username_label.place(x=20, y=300)

    username_entry = tk.Entry(admin_login_window,font=('Timeroman',12),width=30)
    username_entry.place(x=150, y=300,width=300)


    password_label = tk.Label(admin_login_window, text="PASSWORD -", font=('Helvetica', 12,'bold'))
    password_label.place(x=20, y=350)

    password_entry = tk.Entry(admin_login_window,font=('Timeroman',12),width=30)
    password_entry.place(x=150, y=350,width=300)

    button_style = {
    'font': ('Helvetica', 12),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'green',  
    'activeforeground': 'white', 
    'borderwidth': 0,
    'relief': 'ridge'    
}
    
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
        messagebox.showinfo('Login Message',"Login Successfully")
        admin_info_window()
    else:
        messagebox.showerror('Login Message',"invalid login")

def admin_info_window():
    global username_entry, password_entry ,entered_username
    admin_info = tk.Tk()
    admin_info.title("WELCOME "+entered_username.upper())
    admin_info.geometry('1000x700')
    label_admin_info = tk.Label(admin_info, text='🙂 Welcome to the Python Banking System 🙂'.upper(), font=('Timeroman',12,'bold'),fg='darkblue')
    label_admin_info.pack()




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------User sections ---------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

def user_login():
    enterd_user_account = account_entry.get()
    enterd_user_pin = pin_entry.get()

    sqlQuery="SELECT *  FROM createaccount WHERE account_number=%s AND pin=%s"
    mycur.execute(sqlQuery,(enterd_user_account,enterd_user_pin))
    user_data = mycur.fetchone()
    con.commit()

    if user_data:
         messagebox.showinfo("User Login", "Login Successful!")
    else:
        messagebox.showerror("User Login", "Invalid login credentials")

def open_user_login_window():
    user_login_window = tk.Toplevel(a)
    user_login_window.title('User Login')
    user_login_window.geometry('500x500')

   
    user_login_image_path = 'A:/Python With DS/TKinter/Image/userloginlogo2.png'
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

    button_style = {
    'font': ('Helvetica', 12),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'green',  
    'activeforeground': 'white', 
    'borderwidth': 0,
    'relief': 'ridge'    
}
    
    login_button = tk.Button(user_login_window,text='LOGIN',width=30,**button_style,command=user_login)
    login_button.place(x=250,y=400,width=200)

    
    back_button = tk.Button(user_login_window,text='BACK',width=30,**red_button_style,command=lambda:back_to_main_window(user_login_window))
    back_button.place(x=20,y=400,width=200)

    



# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------Exit----------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

def Exit_app():
    a.quit()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

button_01 = tk.Button(a,text='ADMIN LOGIN',width=30,**button_style,command=open_admin_login_window)
button_01.pack(pady=10)


button_02 = tk.Button(a,text='USER LOGIN',width=30,**button_style,command=open_user_login_window)
button_02.pack(pady=10)


button_03 = tk.Button(a,text='EXIT',width=30,**button_style,command=Exit_app)
button_03.pack(pady=10)

  
# -----------------------------------------------------------------Footer---------------------------------------------------------------------------------------

footer_frame = tk.Frame(a, height=10)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Devloped by Aditya Kamble', fg='black')
footer_label.pack(pady=5)
a.mainloop()
