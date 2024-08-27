import tkinter as tk
from tkinter import font as tkfont

# Function to encrypt the text
def encrypt_text():
    text = entry_text.get()
    shift = int(entry_shift.get())
    encrypted_text = ''.join([chr(((ord(char) - 65 + shift) % 26) + 65) if char.isupper() else
                              chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else char
                              for char in text])
    result_var.set(encrypted_text)

# Function to decrypt the text
def decrypt_text():
    text = entry_text.get()
    shift = int(entry_shift.get())
    decrypted_text = ''.join([chr(((ord(char) - 65 - shift) % 26) + 65) if char.isupper() else
                              chr(((ord(char) - 97 - shift) % 26) + 97) if char.islower() else char
                              for char in text])
    result_var.set(decrypted_text)

# Function to clear the input and output fields
def clear_fields():
    entry_text.delete(0, tk.END)
    entry_shift.delete(0, tk.END)
    result_var.set("")

# Setting up the Tkinter window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("800x500")

# Load images for buttons (.png)
try:
    encrypt_img = tk.PhotoImage(file="encrypt.png")
    decrypt_img = tk.PhotoImage(file="decrypt.png")
    clear_img = tk.PhotoImage(file="reset.png")
except tk.TclError as e:
    print("Error loading image files:", e)

# Create a custom font
custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

# Main frame
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(expand=True, fill=tk.BOTH)

# Text Entry
tk.Label(main_frame, text="Enter Text:", font=custom_font).grid(row=0, column=0, padx=10, pady=10, sticky="W")
entry_text = tk.Entry(main_frame, width=50, font=custom_font)
entry_text.grid(row=0, column=1, padx=10, pady=10)

# Shift Entry
tk.Label(main_frame, text="Shift:", font=custom_font).grid(row=1, column=0, padx=10, pady=10, sticky="W")
entry_shift = tk.Entry(main_frame, width=10, font=custom_font)
entry_shift.grid(row=1, column=1, padx=10, pady=10, sticky="W")

# Buttons for Encrypt, Decrypt, and Clear
button_frame = tk.Frame(main_frame)
button_frame.grid(row=2, column=0, columnspan=2, pady=20)

tk.Button(button_frame, image=encrypt_img, command=encrypt_text, borderwidth=0).grid(row=0, column=0, padx=10)
tk.Button(button_frame, image=decrypt_img, command=decrypt_text, borderwidth=0).grid(row=0, column=1, padx=10)
tk.Button(button_frame, image=clear_img, command=clear_fields, borderwidth=0).grid(row=0, column=2, padx=10)

# Result display
result_var = tk.StringVar()
tk.Label(main_frame, text="Result:", font=custom_font).grid(row=3, column=0, padx=10, pady=10, sticky="W")
result_label = tk.Label(main_frame, textvariable=result_var, relief="sunken", width=50, font=custom_font)
result_label.grid(row=3, column=1, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
