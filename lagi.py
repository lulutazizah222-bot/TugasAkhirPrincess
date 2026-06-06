import json
import random

def data_barang(num=10000):
    dataset = []
    for i in range(num):
        dataset.append({
            "product_id": f"PRD-{i:05d}-{'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i % 26]}",
            "nama_produk": f"Produk-{i:05d}-{'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[i % 26]}",
            "harga": random.randint(5, 500) * 1000,
            "rating": round(random.uniform(1.0, 5.0), 1)
        })
    return dataset

data_awal = data_barang(10000)
with open("data_produk.json", "w") as f:
    json.dump(data_awal, f, indent=4)

# Selection Sort - harga ascending
def selection_sort_by_price(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j]['harga'] < arr[min_idx]['harga']:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort - rating descending
def insertion_sort_by_rating(arr):
    n = len(arr)
    for i in range(1, n):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key_item['rating'] > arr[j]['rating']:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

with open("data_produk.json", "r") as f:
    data_produk = json.load(f)

# Filter rating >= 4.0 dulu, baru sort harga
filtered = [p for p in data_produk if p['rating'] >= 4.0]
hasil = selection_sort_by_price(filtered)

print("=" * 60)
print(f"{'No':<4} {'Nama Produk':<22} {'Harga':>12} {'Rating':>7}")
print("=" * 60)
print("--- Top 10 Termurah dengan Rating Tertinggi ---")
for i, p in enumerate(hasil[:10], start=1):
    print(f"{i:<4} {p['nama_produk']:<22} Rp{p['harga']:>9,} {p['rating']:>7}")
print("=" * 60)