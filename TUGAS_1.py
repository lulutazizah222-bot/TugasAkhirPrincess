# Meminta input dari pengguna
nama_depan = input("Masukkan nama depan: ")
nama_belakang = input("Masukkan nama belakang: ")

# Menggabungkan nama
nama_lengkap = nama_depan + " " + nama_belakang

# Menampilkan hasil sesuai format
print("\n=== Hasil Format Nama ===")
print("Huruf kapital semua   :", nama_lengkap.upper())
print("Huruf kecil semua     :", nama_lengkap.lower())
print("Panjang total nama    :", len(nama_lengkap.replace(" ", "")))  # tanpa spasi

# Kalimat awal
kalimat = "Belajar Python itu menyenangkan"

# 1. Cari panjang kalimat
panjang_kalimat = len(kalimat)

# 2. Temukan index posisi kata "Python"
index_python = kalimat.find("Python")

# 3. Ganti kata "Python" menjadi "Pemrograman Python"
kalimat_baru = kalimat.replace("Python", "Pemrograman Python")

# 4. Hitung berapa kali huruf "a" muncul
jumlah_a = kalimat_baru.count("a")

# Tampilkan hasil
print("\n=== Hasil Analisis Kalimat ===")
print("Kalimat asli          :", kalimat)
print("Panjang kalimat       :", panjang_kalimat)
print("Index kata 'Python'   :", index_python)
print("Kalimat baru          :", kalimat_baru)
print("Jumlah huruf 'a'      :", jumlah_a)
