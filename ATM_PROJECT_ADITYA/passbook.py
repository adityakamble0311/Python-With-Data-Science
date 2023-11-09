import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import random
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Your global variables, styles, and other setup code here

def createnewaccount():
    global name_entry, city_entry, account_type_combobox, balance_entry, account_type_var
    create_ac_window = tk.Toplevel(a)
    create_ac_window.title('CREATE NEW ACCOUNT')
    create_ac_window.geometry('800x480')

    def createAccount():
        global name_entry, city_entry, account_type_combobox, balance_entry, account_type_var
        ac_pin = random.randrange(1000, 9999)
        ac_no = random.randrange(100000000000, 999999999999)
        name = name_entry.get()
        city = city_entry.get()
        acType = account_type_var.get()
        balance = balance_entry.get()
        confirm = messagebox.askyesno("CREATE ACCOUNT", f"Are you sure you want to create a new account, {name}?".upper())
        if confirm:
            sqlQuery = "insert into createaccount values('{}','{}','{}','{}','{}','{}')".format(name, city, acType, balance, ac_no, ac_pin)
            mycur.execute(sqlQuery)
            con.commit()
            messagebox.showinfo('CREATE ACCOUNT', "ACCOUNT CREATED SUCCESSFULLY")
            create_account_window = tk.Toplevel(a)
            create_account_window.title('CREATE ACCOUNT')
            create_account_window.geometry('500x500')
            create_account_image_path = 'A:/Python With DS/TKinter/Image/createAccountInfo.png'
            create_account_image = Image.open(create_account_image_path)
            create_account_image = create_account_image.resize((200, 200), Image.ANTIALIAS)
            create_photo = ImageTk.PhotoImage(create_account_image)
            label_create_photo = tk.Label(create_account_window, image=create_photo)
            label_create_photo.image = create_photo
            label_create_photo.pack()

            label_info = tk.Label(create_account_window, text=f'{name.upper()} ACCOUNT CREATED SUCCESSFULLY', font=('Helvetica', 12, 'bold'))
            label_info.pack()

            generate_passbook_button = tk.Button(create_account_window, text='PRINT PASSBOOK', width=35, **big_button_style, command=save_and_download_pdf)
            generate_passbook_button.pack()

            footer_frame = tk.Frame(create_account_window, height=10)
            footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
            footer_label = tk.Label(footer_frame, text='Python Banking System | Design & Developed by Aditya Kamble', fg='black')
            footer_label.pack(pady=5)

            # Passbook generation functions here

            create_account_window.mainloop()  # Placed outside the save_and_download_pdf() function

        else:
            messagebox.showerror('CREATE ACCOUNT', "ACCOUNT NOT CREATED")

    # Your remaining GUI layout code here

# Your remaining code here

a = tk.Tk()
createnewaccount()
a.mainloop()
