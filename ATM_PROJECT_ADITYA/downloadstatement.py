from tkinter import ttk, filedialog
import tkinter as tk
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def set_row_colors():
    for i, item in enumerate(table.get_children()):
        if i % 2 == 0:
            table.item(item, tags=('even',))
        else:
            table.item(item, tags=('odd',))

def generate_pdf():
    doc = SimpleDocTemplate("informations.pdf", pagesize=letter)
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
        shutil.move("informations.pdf", file_path)

a = tk.Tk()
a.geometry('1200x400')
a.title('INFORMATIONS')

label_1 = tk.Label(a, text="INFORMATIONS", font=('Times', 14, 'bold'))
label_1.pack()

style = ttk.Style(a)
style.theme_use("clam")
style.configure("Treeview.Heading", font=('Helvetica', 12, 'bold'), background='#3498db', foreground='white')
style.configure("Treeview",
                background="#ecf0f1",
                fieldbackground="#ecf0f1",
                rowheight=30,
                font=('Helvetica', 11))

table = ttk.Treeview(a, columns=('Name', 'City', 'AccountType', 'Balance', 'AccountNumber', 'Pin'), show='headings')
table.heading('Name', text='NAME')
table.heading('City', text='CITY')
table.heading('AccountType', text='ACCOUNT TYPE')
table.heading('Balance', text='BALANCE')
table.heading('AccountNumber', text='ACCOUNT NUMBER')
table.heading('Pin', text='PIN')
table.pack()

# Alternate row colors
table.tag_configure('even', background='#d5dbdb')
table.tag_configure('odd', background='white')

# Example data
data = [
    ("John Doe", "New York", "Savings", "$1000", "123456789", "1234"),
    ("Jane Smith", "Los Angeles", "Checking", "$1500", "987654321", "5678"),
    # Add more data here...
]

# Insert example data into the table
for item in data:
    table.insert('', 'end', values=item)

set_row_colors()

generate_pdf_button = tk.Button(a, text="Generate PDF", command=generate_pdf)
generate_pdf_button.pack()

save_pdf_button = tk.Button(a, text="Download PDF", command=save_pdf)
save_pdf_button.pack()

a.mainloop()
