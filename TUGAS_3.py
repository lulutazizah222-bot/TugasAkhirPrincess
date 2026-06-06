# Program: Kalkulator Diskon - Studi Kasus
# Format Struk Belanja

print(f"{'Rama Indah' :^40}")
print("=" * 42)
print("Kasus 1: Kalkulator Diskon")
print("Toko memberikan diskon 20%")
print("untuk pembelian di atas Rp100.000")
print("=" * 42)

# Input total belanja
total = float(input("Masukkan total belanja (Rp): ")) 

# Hitung diskon
if total > 100000:
    diskon = 0.2 * total
else:
    diskon = 0

# Hitung total bayar
total_bayar = total - diskon

# Cetak struk hasil
print("\n" + "-" * 35)
print("Total Belanja : Rp", total)
print("Diskon        : Rp", diskon)
print("Total Bayar   : Rp", total_bayar)
print("-" * 35)
print("/- TERIMA KASIH TELAH BERBELANJA -/")