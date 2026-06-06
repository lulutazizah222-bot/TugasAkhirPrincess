# Aplikasi Kriptografi Berbasis Pesan
# Algoritma: Caesar Cipher

def enkripsi(pesan, kunci):
    hasil = ""

    for huruf in pesan:
        if huruf.isalpha():
            if huruf.isupper():
                hasil += chr((ord(huruf) - ord('A') + kunci) % 26 + ord('A'))
            else:
                hasil += chr((ord(huruf) - ord('a') + kunci) % 26 + ord('a'))
        else:
            hasil += huruf

    return hasil


def dekripsi(pesan, kunci):
    return enkripsi(pesan, -kunci)


while True:
    print("\n" + "="*40)
    print("APLIKASI KRIPTOGRAFI BERBASIS PESAN")
    print("="*40)
    print("1. Enkripsi Pesan")
    print("2. Dekripsi Pesan")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        pesan = input("Masukkan pesan: ")
        kunci = int(input("Masukkan kunci: "))

        hasil = enkripsi(pesan, kunci)

        print("\nPesan Asli     :", pesan)
        print("Pesan Terenkripsi :", hasil)

    elif pilihan == "2":
        pesan = input("Masukkan pesan terenkripsi: ")
        kunci = int(input("Masukkan kunci: "))

        hasil = dekripsi(pesan, kunci)

        print("\nPesan Terenkripsi :", pesan)
        print("Pesan Asli        :", hasil)

    elif pilihan == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")