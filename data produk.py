import json
import random

# Membuat data produk
def generate_produk(jumlah=20):
    produk = []

    for i in range(1, jumlah + 1):
        item = {
            "product_id": i,
            "nama_produk": f"Produk_{i}",
            "harga": random.randint(100000, 5000000),
            "rating": round(random.uniform(1.0, 5.0), 1)
        }

        produk.append(item)

    return produk


# ==============================
# Selection Sort Harga Ascending
# ==============================
def sort_harga_ascending(data):
    panjang = len(data)

    for i in range(panjang):

        posisi_min = i

        for j in range(i + 1, panjang):

            if data[j]["harga"] < data[posisi_min]["harga"]:
                posisi_min = j

        # Tukar data
        data[i], data[posisi_min] = data[posisi_min], data[i]

    return data


# ==============================
# Insertion Sort Rating Descending
# ==============================
def sort_rating_descending(data):

    for i in range(1, len(data)):

        current = data[i]
        j = i - 1

        while j >= 0 and data[j]["rating"] < current["rating"]:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = current

    return data


# Generate data
data_produk = generate_produk()

# Simpan ke file JSON
with open("produk.json", "w") as file:
    json.dump(data_produk, file, indent=4)

# Copy data agar data asli tidak berubah
data_harga = data_produk.copy()
data_rating = data_produk.copy()

# Sorting
hasil_harga = sort_harga_ascending(data_harga)
hasil_rating = sort_rating_descending(data_rating)

# ==============================
# OUTPUT HARGA ASCENDING
# ==============================
print("\n")
print("=" * 65)
print("      DAFTAR PRODUK BERDASARKAN HARGA TERMURAH")
print("=" * 65)

print(f"{'No':<5} {'Nama Produk':<20} {'Harga':<15} {'Rating'}")
print("-" * 65)

for no, produk in enumerate(hasil_harga[:10], start=1):
    print(
        f"{no:<5} "
        f"{produk['nama_produk']:<20} "
        f"Rp {produk['harga']:<12,} "
        f"{produk['rating']}"
    )

# ==============================
# OUTPUT RATING DESCENDING
# ==============================
print("\n")
print("=" * 65)
print("     DAFTAR PRODUK BERDASARKAN RATING TERTINGGI")
print("=" * 65)

print(f"{'No':<5} {'Nama Produk':<20} {'Harga':<15} {'Rating'}")
print("-" * 65)

for no, produk in enumerate(hasil_rating[:10], start=1):
    print(
        f"{no:<5} "
        f"{produk['nama_produk']:<20} "
        f"Rp {produk['harga']:<12,} "
        f"{produk['rating']}"
    )

print("\n")
print("Sorting selesai dilakukan.")