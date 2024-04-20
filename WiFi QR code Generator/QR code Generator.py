#Modules

import tkinter as tk
import qrcode
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox


#functional code

def generate_qr_with_file_name():
    wifiName = ssid_entry.get()
    wifiPassword = password_entry.get()
    file_name = simpledialog.askstring("File Name", "Enter the file name:")
    if file_name:
        generate_qr(wifiName, wifiPassword, file_name)

def generate_qr(wifiName, wifiPassword, file_name):
    wifi_config = f"WIFI:T:WPA;S:{wifiName};P:{wifiPassword};;"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=40,
        border=5,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)

#QR IMAGE COLOR DEFINE

    img = qr.make_image(fill_color="black", back_color="white")
    
#file typr anf path

    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile=file_name)
    if file_path:
        img.save(file_path)
        messagebox.showinfo("QR Code Saved", f"The QR code has been saved as '{file_path}'.")

# WIFI QR CODE GENERATOR UI 

window = tk.Tk()
window.config(bg='black')
window.title("Wi-Fi QR Code Generator")
window.geometry('450x380')

#widi name + password input section

ssid_label = tk.Label(window, text='Enter your WIFI NAME', font=50, background='black', fg='white')
ssid_label.pack(pady=10)

ssid_entry = tk.Entry(window, font=18, width=35, bg='#2C3E50', fg='white', bd=3, relief='solid')
ssid_entry.pack(pady=15)

password_label = tk.Label(window, text='Enter your WIFI PASSWORD', font=50, background='black', fg='white')
password_label.pack(pady=10)

password_entry = tk.Entry(window, font=18, width=35, bg='#2C3E50', fg='white', bd=3, relief='solid')
password_entry.pack(pady=15)

#QR code generator/ submit button

submit_button = tk.Button(window, bd=7, bg='#FFB2E5', font=12, relief='groove', text='Generate QR code', command=generate_qr_with_file_name)
submit_button.pack(pady=51)

#exit butoon

exit_button = tk.Button(window, bd=7, background='red', font=12, relief='groove', text='Exit', command= window.destroy)
exit_button.pack(pady=1)

window.mainloop()
