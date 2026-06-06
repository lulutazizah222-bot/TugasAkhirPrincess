import tkinter as tk
from tkinter import messagebox

def login():
    nama = entry_nama.get()
    nim = entry_nim.get()

    if not nama or nama.isalpha():
        messagebox.showerror("Gagal", "Masukkan Nama mu Dengan Benar")
        return

    try:
        nim_int = int(nim)
    except ValueError:
        messagebox.showerror("Gagal", "Masukkan NIM mu Dengan Benar")
        return

    messagebox.showinfo("Berhasil", f"Login berhasil!\nNama: {nama}\nNIM: {nim_int}")

root = tk.Tk()
root.title("Login Mahasiswa")
root.geometry("300x250")

label_nama = tk.Label(root, text="NAMA")
label_nama.pack(pady=10)

entry_nama = tk.Entry(root)
entry_nama.pack(pady=5)

label_nim = tk.Label(root, text="NIM")
label_nim.pack(pady=10)

entry_nim = tk.Entry(root)
entry_nim.pack(pady=5)

button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

root.mainloop()