import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Database connection setup
con = mysql.connector.connect(host='localhost', user='root', password='Aditya@12072004@', database='atm')
mycur = con.cursor()

# Global variables
entered_account = ""
entered_pin = ""
balance = 0.0

def back_to_main_window(window):
    window.destroy()

def user_panel():
    # ... (existing code)

    button_7 = tk.Button(user_panel_window, text='TRANSACTIONS', width=30, **big_button_style, command=transactions)
    button_7.pack(pady=10)

    # ... (existing code)

def add_transaction(account_number, transaction_type, amount):
    sqlQuery = "INSERT INTO transactions (account_number, transaction_type, amount) VALUES ('{}', '{}', '{}')".format(account_number, transaction_type, amount)
    mycur.execute(sqlQuery)
    con.commit()

def dipoAmount():
    global account_entry, pin_entry, dop_entry, balance, entered_account, entered_pin
    amount = dop_entry.get()
    total_amount = float(balance) + float(amount)

    add_transaction(entered_account, 'Deposit', amount)  # Add deposit transaction

    sqlQuery = "UPDATE createaccount SET opening_balance='{}' WHERE account_number='{}' AND pin='{}'".format(total_amount, entered_account, entered_pin)
    mycur.execute(sqlQuery)
    con.commit()

    messagebox.showinfo("DEPOSIT BALANCE", "Amount Deposited Successfully Rs.{}\nYour Current Balance is Rs.{}".format(amount, total_amount))
    user_panel()

def display_transactions():
    transactions_window = tk.Toplevel(a)
    transactions_window.title("TRANSACTIONS")
    transactions_window.geometry('500x500')

    # Retrieve transactions from the transactions table for the current user (entered_account)
    sqlQuery = "SELECT * FROM transactions WHERE account_number='{}'".format(entered_account)
    mycur.execute(sqlQuery)
    transactions_data = mycur.fetchall()

    transactions_listbox = tk.Listbox(transactions_window, width=40, height=10)
    for transaction in transactions_data:
        transactions_listbox.insert(tk.END, f"{transaction[2]}: Rs.{transaction[3]}")
    transactions_listbox.pack(pady=20)

    transactions_button_back = tk.Button(transactions_window, text='BACK', **big_red_button_style, command=transactions_window.destroy)
    transactions_button_back.pack()

def transactions():
    global account_entry, pin_entry, balance, entered_account, entered_pin

    entered_account = account_entry.get()
    entered_pin = pin_entry.get()

    sqlQuery = "SELECT opening_balance FROM createaccount WHERE account_number='{}' AND pin='{}'".format(entered_account, entered_pin)
    mycur.execute(sqlQuery)
    balance = mycur.fetchone()[0]
    con.commit()

    transactions_window = tk.Toplevel(a)
    transactions_window.title("TRANSACTIONS")
    transactions_window.geometry('500x500')

    transactions_label = tk.Label(transactions_window, text='RECENT TRANSACTIONS', font=('Timeroman', 16, 'bold'))
    transactions_label.pack(pady=10)

    display_transactions_button = tk.Button(transactions_window, text='DISPLAY TRANSACTIONS', **big_button_style, command=display_transactions)
    display_transactions_button.pack(pady=10)

    transactions_button_back = tk.Button(transactions_window, text='BACK', **big_red_button_style, command=transactions_window.destroy)
    transactions_button_back.pack()

    footer_frame = tk.Frame(transactions_window, height=10)
    footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
    footer_label = tk.Label(footer_frame, text='Python Banking System | Designed & Developed by Aditya Kamble', fg='black')
    footer_label.pack(pady=5)

# ... (other existing functions and UI setup)

# Main program
a = tk.Tk()
a.title("BANK MANAGEMENT SYSTEM")
a.geometry('800x600')

# UI styles
big_button_style = {"font": ('Times New Roman', 12), "bg": "lightblue", "activebackground": "lightblue"}
big_red_button_style = {"font": ('Times New Roman', 12), "bg": "red", "activebackground": "red"}

# ... (other UI elements and main loop)

a.mainloop()
