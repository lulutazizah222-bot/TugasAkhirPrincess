import tkinter as tk
from tkinter import messagebox

def login():
    nama = entry_nama.get()
    nim = entry_nim.get()

    # Validasi nama (tidak kosong dan hanya huruf)
    if not nama or not nama.replace(" ", "").isalpha():
        messagebox.showerror("Gagal", "Masukkan Nama mu Dengan Benar")
        return

    # Validasi NIM (harus angka)
    try:
        nim_int = int(nim)
    except ValueError:
        messagebox.showerror("Gagal", "Masukkan NIM mu Dengan Benar")
        return

    # Jika berhasil
    messagebox.showinfo(
        "Berhasil",
        f"Login berhasil!\nNama: {nama}\nNIM: {nim_int}"
    )

# Membuat window utama
root = tk.Tk()
root.title("Login Mahasiswa")
root.geometry("300x250")

# Label dan Entry Nama
label_nama = tk.Label(root, text="NAMA")
label_nama.pack(pady=10)

entry_nama = tk.Entry(root)
entry_nama.pack(pady=5)

# Label dan Entry NIM
label_nim = tk.Label(root, text="NIM")
label_nim.pack(pady=10)

entry_nim = tk.Entry(root)
entry_nim.pack(pady=5)

# Tombol Login
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
