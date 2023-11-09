import qrcode
import tkinter as tk

from PIL import Image,ImageTk
from tkinter import messagebox  
from tkinter import ttk,filedialog

# upi_url_format = "upi://pay?pa={}&am={}&cu=INR"
# user_upi_id = "mohitsuradkar274@oksbi"

# amount = input("Enter the amount: ")
# upi_url = upi_url_format.format(user_upi_id,amount)
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data(upi_url)
# qr.make(fit=True)
# qr_img = qr.make_image(fill_color="black", back_color="white")
# qr_img.show()



a = tk.Tk()
a.title('Python Banking System')
a.geometry('800x675')

