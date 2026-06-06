# Meminta input total belanja 
total_belanja = float(input("Masukkan total belanja Anda(Rp): "))

# Mengecek apakah total belanja lebih dari 100.000
if total_belanja > 100000 :
    diskon = 2.0 * total_belanja
    total_bayar = total_belanja - diskon
    print(f"Anda mendapat diskon 20% sebesar Rp{diskon:,.0f}")
else:
    total_bayar = total_belanja 
    print("Belanja Anda tidak mendapat diskon.")

    #Menampilkan total yang harus di bayar 
    print(f"Total yang harus di bayar : Rp{total_bayar:,.0f}")