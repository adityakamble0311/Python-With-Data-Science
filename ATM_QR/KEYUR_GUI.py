import qrcode
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import random
import requests

ATM_QR = tk.Tk()
ATM_QR.title("WELCOME TO ATM QR SYSTEM")
ATM_QR.geometry('500x500')

# ... (previous code)

# Define a global variable to store the generated OTP
generated_otp = None

def generate_otp():
    # Generate a random 6-digit OTP
    return str(random.randint(100000, 999999))

def send_otp(mobile_number, otp):
    # Fast2SMS API URL
    url = "https://www.fast2sms.com/dev/bulk"

    # Replace 'YOUR_API_KEY' with your actual Fast2SMS API key
    api_key = "YOUR_API_KEY"

    # Create the message with the OTP
    message = f"Your OTP is: {otp}"

    # Specify the parameters
    params = {
        'authorization': api_key,
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': mobile_number
    }

    try:
        # Send the OTP via Fast2SMS API
        response = requests.get(url, params=params)

        # Check the HTTP status code
        response.raise_for_status()

        # Check if the response contains valid JSON data
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

# ... (rest of your code)

# Add a label and entry for the mobile number
mobile_number_label = tk.Label(ATM_QR, text="Mobile Number:", font=('Timeroman', 13, 'bold'))
mobile_number_label.place(x=20, y=380)
mobile_number_entry = tk.Entry(ATM_QR, font=('Helvetica', 12), width=30)
mobile_number_entry.place(x=170, y=380, width=280)

# Update the button command to call atm_operations
pay_button = tk.Button(ATM_QR, text='PAY NOW', width=30, **button_style, command=atm_operations)
pay_button.place(x=250, y=440, width=220)

ATM_QR.mainloop()
