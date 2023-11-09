import qrcode
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox 
import requests 
import random

def generate_otp():
    return str(random.randint(1000,9999))
def send_otp(mobile_number, otp):
    url = "https://www.fast2sms.com/dev/bulk"

    api_key = "9j25VM4lKTds3azuh1xSgiEPtybRqACc8mYp0nFWBJL7ZUNwDkOi4FYa8uAhWnIMsyGz6UqZTevNQHC3"

    message = f"ATM CASH MACHINE /n Your OTP is: {otp}"
    params = {
        'authorization': api_key,
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': mobile_number
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        response_json = response.json()

        if response_json['return']:
            return True
        else:
            tk.messagebox.showerror("Error", "Failed to send OTP. Please try again.")
            return False
    except requests.exceptions.HTTPError as http_err:
        tk.messagebox.showerror("HTTP Error", f"HTTP error occurred: {http_err}")
        return False
    except requests.exceptions.RequestException as req_err:
        tk.messagebox.showerror("Request Exception", f"Request exception occurred: {req_err}")
        return False
    except ValueError as json_err:
        tk.messagebox.showerror("JSON Error", f"JSON decoding error occurred: {json_err}")
        return False
ATM_QR = tk.Tk()
ATM_QR.title("WELCOME TO ATM QR SYSTEM")
ATM_QR.geometry('500x500')

red_button_style = {
    'font': ('Helvetica', 16),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'darkred',  
    'activeforeground': 'white', 
    'borderwidth': 0,
    'relief': 'ridge'    
}
button_style = {
    'font': ('Helvetica', 16),
    'bg': 'darkblue',        
    'fg': 'white',       
    'activebackground': 'green',  
    'activeforeground': 'white', 
    'borderwidth': 0,
    'relief': 'ridge'    
}

def verify_otp(entered_otp):
    global generated_otp

    if entered_otp == generated_otp:
        return True
    else:
        return False
def atm_operations():
    mobile_number = mobile_number_entry.get()
    enter_amount_str = enter_pay_entry.get()
    global enter_amount
    try:
        enter_amount = float(enter_amount_str)
        formatted_amount = "{:.2f}".format(enter_amount)
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter a valid numeric amount")
        return
    
    generated_otp = generate_otp()

    if send_otp(mobile_number, generated_otp):
        tk.messagebox.showinfo("OTP Sent", "An OTP has been sent to your mobile number.")
        otp_window = tk.Toplevel()
        otp_window.title("Enter OTP")
        otp_window.geometry('400x400')

        otp_label = tk.Label(otp_window, text="Enter the OTP sent to your mobile number:".upper(),font=('Timeroman',10,'bold'))
        otp_label.pack()

        otp_entry = tk.Entry(otp_window)
        otp_entry.place(x=50,y=40,width=300)

        def verify_and_display_qr():
            entered_otp = otp_entry.get()
            
            if entered_otp == generated_otp:
                tk.messagebox.showinfo("OTP Verified", "OTP verified. Proceeding to display QR code.")
                otp_window.destroy()  
                display_qr_code(mobile_number, enter_amount)
            else:
                tk.messagebox.showerror("OTP Verification Failed", "Incorrect OTP. Please try again.")

        verify_button = tk.Button(otp_window, text="Verify OTP".upper(), command=verify_and_display_qr,**button_style)
        verify_button.place(x=50,y=70,width=300)
        
    else:
        tk.messagebox.showerror("Error", "Failed to send OTP. Please try again.")
def display_qr_code(mobile_number, enter_amount):
    
    ATM_QR_CODE = tk.Toplevel()
    ATM_QR_CODE.title("PAY NOW")
    ATM_QR_CODE.geometry('500x400')

    upi_url_format = "upi://pay?pa={}&am={:.2f}&cu=INR"
    bank_id = "8421975372@ybl"
    upi_url = upi_url_format.format(bank_id, enter_amount)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    imgtk = ImageTk.PhotoImage(qr_img)
    label = tk.Label(ATM_QR_CODE, image=imgtk)
    label.image = imgtk
    label.pack()

    set_amount_label_text = f'SET AMOUNT: ₹{enter_amount}'
    set_amount = tk.Label(ATM_QR_CODE, text=set_amount_label_text, font=('Timeroman', 10))
    set_amount.pack()
    ATM_QR_CODE.after(20000, ATM_QR_CODE.destroy)

all_image_folder_path = 'A:/Python With DS/ATM_QR/IMG/'
atm_qr_image = Image.open(all_image_folder_path+'ATM_QR.png').resize((400,350))
atm_qr_image = ImageTk.PhotoImage(atm_qr_image)
label_atm_qr_image = tk.Label(ATM_QR, image = atm_qr_image )
label_atm_qr_image .image = atm_qr_image
label_atm_qr_image.pack()
    
ATM_CASH = tk.Label(ATM_QR,text='ATM CASH MACHINE',font=('Timeroman',16,'bold'))
ATM_CASH.place(x=150, y=310)

enter_pay_label = tk.Label(ATM_QR,text="Enter Amount:".upper(),font=('Timeroman',13,'bold'))
enter_pay_label.place(x=20, y=350)
enter_pay_entry = tk.Entry(ATM_QR,font=('Helvetica',12),width=30)
enter_pay_entry.place(x=170, y=350,width=280)

mobile_number_label = tk.Label(ATM_QR, text="Mobile Number:".upper(), font=('Timeroman', 13, 'bold'))
mobile_number_label.place(x=20, y=380)
mobile_number_entry = tk.Entry(ATM_QR, font=('Helvetica', 12), width=30)
mobile_number_entry.place(x=170, y=380, width=280)
mobile_number_entry = tk.Entry(ATM_QR, font=('Helvetica', 12), width=30)
mobile_number_entry.place(x=170, y=380, width=280)
def Exit_app():
    ATM_QR.quit()
back_button = tk.Button(ATM_QR,text='BACK',width=30,**red_button_style,command=Exit_app)
back_button.place(x=20,y=440,width=220)

pay_button = tk.Button(ATM_QR,text='PAY NOW',width=30,**button_style,command=atm_operations)
pay_button.place(x=250,y=440,width=220)
ATM_QR.mainloop()