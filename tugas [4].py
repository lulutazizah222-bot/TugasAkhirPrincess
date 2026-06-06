import json # Untuk simpan dan baca data dalam format JSON
import random # Untuk buat data acak (random) sesuai kebutuhan kita

# 1. Fungsi buat bikin data Fashion Cewek
def data_barang(num=100):
    dataset = []
    kategori = ["Hijab Bella", "Pashmina Silk", "Gamis Brokat", "Blouse Korea", 
                "Rok Plisket", "Tunik Rayon", "Cardigan Rajut", "Kulot Highwaist"]
    
    for i in range(num):
        item_fashion = random.choice(kategori)
        dataset.append({
            "product_id": f"FSH-{i:05d}",
            "nama_produk": f"{item_fashion}-{random.randint(100, 999)}",
            # CARANYA: Random angka 5-100, lalu dikali 1000
            # Hasilnya pasti belakangnya 000 (Contoh: 7 * 1000 = 7.000)
            "harga": random.randint(5, 100) * 1000, 
            "rating": round(random.uniform(4.0, 5.0), 1)
        })
    return dataset

# 2. Fungsi Selection Sort (Harga Ascending, Rating Descending)
def selection_sort_custom(arr):
    n = len(arr)
    for i in range(n):
        target_idx = i
        for j in range(i + 1, n):
            if arr[j]['harga'] < arr[target_idx]['harga']:
                target_idx = j
            elif arr[j]['harga'] == arr[target_idx]['harga']:
                if arr[j]['rating'] > arr[target_idx]['rating']:
                    target_idx = j
        arr[i], arr[target_idx] = arr[target_idx], arr[i]
    return arr

# 3. Eksekusi Program
data_awal = data_barang(100)
with open("data_produk.json", "w") as f:
    json.dump(data_awal, f, indent=4)

with open("data_produk.json", "r") as f:
    data_produk = json.load(f)

hasil = selection_sort_custom(data_produk)

# 4. Tampilkan Hasil
print("=" * 75)
print(f"{'No':<4} {'Nama Produk':<25} {'Harga':>15} {'Rating':>8}")
print("=" * 75)
for i, p in enumerate(hasil[:10], start=1):
    # Format :, ditaruh di harga agar muncul pemisah ribuan (titik/koma)
    print(f"{i:<4} {p['nama_produk']:<25} Rp {p['harga']:>10,} {p['rating']:>8}")
print("=" * 75)