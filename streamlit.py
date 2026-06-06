import streamlit as st

# ==================================================
# PENGATURAN HALAMAN
# ==================================================

st.set_page_config(
    page_title="Toko Serba Guna",
    page_icon="🛒",
    layout="wide"
)

# ==================================================
# DATA PRODUK
# ==================================================

produk = [
    "Chitato", "Qtela", "Taro", "Momogi", "Oreo",
    "Beng Beng", "SilverQueen", "Nabati", "Good Time", "Roma Kelapa",
    "Pilus Garuda", "JetZ", "Lays", "Pringles", "Piattos",
    "Potabee", "Chocolatos", "Astor", "Biskuat", "Marie Regal",
    "Malkist", "Nextar", "Tango", "Better", "Fullo",
    "Hello Panda", "Yupi Burger", "Yupi Pizza", "Fox Candy", "Relaxa",
    "Mentos Mint", "Mentos Fruit", "Nano Nano", "Happytos", "BonCabe Snack",
    "BonCabe Makaroni", "Keripik Pisang", "Keripik Singkong", "Emping Balado", "Emping Original",
    "Kripik Tempe", "Kripik Talas", "Leo", "Kusuka", "Siip",
    "Twister", "Chiki Balls", "Cheetos", "Maxicorn", "Popcorn Caramel",
    "Popcorn Cheese", "Garuda Kacang", "Choki Choki", "Delfi Top", "Delfi Milk",
    "Richese", "Wafer Superstar", "Wafer Selamat", "Stick Wafer Keju", "Stick Wafer Coklat",
    "Sari Gandum", "Roma Malkist", "Piattos Keju", "Piattos Balado", "Piattos Sapi Panggang",
    "Potabee BBQ", "Potabee Rumput Laut", "JetZ Balado", "JetZ BBQ", "Taro BBQ",
    "Taro Seaweed", "Qtela Balado", "Qtela Original", "Chitato BBQ", "Chitato Sapi Panggang",
    "SilverQueen Almond", "SilverQueen Cashew", "Beng Beng Maxx", "Oreo Coklat", "Oreo Original",
    "Good Time Choco", "Good Time Double Choco", "Nabati Richeese", "Nabati Richoco", "Astor Vanilla",
    "Astor Coklat", "Malkist Crackers", "Malkist Abon", "Nextar Brownies", "Nextar Pineapple",
    "Fullo Coklat", "Fullo Vanilla", "Hello Panda Coklat", "Hello Panda Strawberry",
    "Yupi Strawberry", "Yupi Gummy", "Yupi Cola", "Yupi Mango", "Yupi Watermelon"
]

# ==================================================
# BUBBLE SORT
# ==================================================

def bubble_sort(data):
    arr = data.copy()

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):

            if arr[j].lower() > arr[j + 1].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

produk = bubble_sort(produk)

# ==================================================
# KONVERSI KATA KE ANGKA
# ==================================================

def nilai_kata(teks):
    return sum(ord(huruf) for huruf in teks.lower())

nilai_produk = [nilai_kata(p) for p in produk]

# ==================================================
# INTERPOLATION SEARCH
# ==================================================

def interpolation_search(arr, target):

    low = 0
    high = len(arr) - 1

    while (
        low <= high and
        target >= arr[low] and
        target <= arr[high]
    ):

        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            return -1

        pos = low + (
            (target - arr[low]) *
            (high - low)
        ) // (
            arr[high] - arr[low]
        )

        if pos < 0 or pos >= len(arr):
            return -1

        if arr[pos] == target:
            return pos

        elif arr[pos] < target:
            low = pos + 1

        else:
            high = pos - 1

    return -1

# ==================================================
# TAMPILAN
# ==================================================

st.title("🛒 TOKO SERBA GUNA")

st.info("""
📌 INFORMASI SISTEM

• Algoritma Sorting : Bubble Sort
• Algoritma Searching : Interpolation Search
• Data Produk : 100 Produk Makanan Ringan
• Framework : Streamlit
• Bahasa Pemrograman : Python
""")

# ==================================================
# PENCARIAN PRODUK
# ==================================================

st.subheader("🔍 Pencarian Produk")

nama_produk = st.text_input(
    "Masukkan Nama Produk",
    placeholder="Contoh: Chitato"
)

if st.button("Cari Produk"):

    target = nilai_kata(nama_produk)

    hasil = interpolation_search(
        nilai_produk,
        target
    )

    ditemukan = False

    if hasil != -1:
        if produk[hasil].lower() == nama_produk.lower():
            ditemukan = True

    if ditemukan:

        rak = (hasil // 10) + 1

        st.success("✅ Produk Ditemukan")

        st.write("### Hasil Pencarian")
        st.write(f"**Nama Produk :** {produk[hasil]}")
        st.write(f"**Posisi Rak :** Rak {rak}")
        st.write(f"**Index Data :** {hasil}")
        st.write("**Metode :** Interpolation Search")

    else:
        st.error("❌ Produk Tidak Ditemukan")

# ==================================================
# RAK DIGITAL
# ==================================================

st.markdown("---")
st.subheader("📦 Rak Digital Produk")

for rak in range(10):

    st.write(f"### Rak {rak + 1}")

    cols = st.columns(10)

    for slot in range(10):

        idx = rak * 10 + slot

        if idx < len(produk):
            cols[slot].button(
                produk[idx],
                disabled=True,
                key=f"produk_{idx}"
            )

# ==================================================
# TABEL DATA
# ==================================================

st.markdown("---")
st.subheader("📋 Daftar Produk")

st.dataframe(
    produk,
    use_container_width=True
)

st.success(f"Total Produk : {len(produk)}")