
import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
import base64
import os

def pad(text):
    return text + (16 - len(text) % 16) * ' '

def encrypt_aes():
    message = entry_plain.get("1.0", tk.END).strip()
    key = entry_key.get().strip()
    if len(key) != 16:
        messagebox.showerror("Error", "AES key must be 16 characters.")
        return
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode('utf-8'))
    ciphertext = base64.b64encode(encrypted).decode('utf-8')
    entry_result.delete("1.0", tk.END)
    entry_result.insert(tk.END, ciphertext)

def decrypt_aes():
    ciphertext = entry_result.get("1.0", tk.END).strip()
    key = entry_key.get().strip()
    if len(key) != 16:
        messagebox.showerror("Error", "AES key must be 16 characters.")
        return
    try:
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        decrypted = cipher.decrypt(base64.b64decode(ciphertext)).decode('utf-8').strip()
        entry_plain.delete("1.0", tk.END)
        entry_plain.insert(tk.END, decrypted)
    except Exception as e:
        messagebox.showerror("Decryption Failed", str(e))

app = tk.Tk()
app.title("AES Text Encryption - Educational")

tk.Label(app, text="Plaintext").grid(row=0, column=0)
entry_plain = tk.Text(app, height=5, width=40)
entry_plain.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="AES Key (16 chars)").grid(row=1, column=0)
entry_key = tk.Entry(app, width=40, show="*")
entry_key.grid(row=1, column=1, padx=10, pady=5)

tk.Button(app, text="Encrypt", command=encrypt_aes, bg="green", fg="white").grid(row=2, column=0, pady=10)
tk.Button(app, text="Decrypt", command=decrypt_aes, bg="blue", fg="white").grid(row=2, column=1)

tk.Label(app, text="Encrypted/Decrypted Text").grid(row=3, column=0)
entry_result = tk.Text(app, height=5, width=40)
entry_result.grid(row=3, column=1, padx=10, pady=5)

app.mainloop()
