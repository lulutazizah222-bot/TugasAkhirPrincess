produk = []

merek = [
    "Indomie Goreng",
    "Indomie Soto",
    "Mie Sedaap Kari",
    "Mie Sedaap Goreng",
    "Sarimi Ayam",
    "Sarimi Soto",
    "Pop Mie Ayam",
    "Pop Mie Baso",
    "Supermi Ayam",
    "Lemonilo Goreng"
]

for i in range(500):
    produk.append({
        "id": 1001 + i,
        "nama": merek[i % len(merek)] + f" {i+1}",
        "harga": 3000 + (i % 10) * 500,
        "rak": f"R{(i // 25) + 1}"
    })