import streamlit as st
import pandas as pd
import random

# =====================================
# KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Sistem Pencarian Produk",
    page_icon="🛒",
    layout="wide"
)

# =====================================
# CSS CUSTOM
# =====================================

st.markdown("""
<style>

.stApp{
    background-color:#050b18;
    color:white;
}

h1,h2,h3{
    color:white;
}

div[data-testid="metric-container"]{
    background:#13213c;
    border-radius:15px;
    padding:15px;
    border:1px solid #274472;
}

.stButton>button{
    background:#22c55e;
    color:white;
    border:none;
    border-radius:10px;
    font-weight:bold;
}

.info-box{
    background:#14325a;
    padding:20px;
    border-radius:15px;
}

.success-box{
    background:#4b500d;
    padding:20px;
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# DATA PRODUK INDOMARET
# =====================================

produk_indomaret = [
    "Indomie Goreng","Indomie Soto","Indomie Kari Ayam",
    "Indomie Ayam Bawang","Mie Sedaap Goreng",
    "Mie Sedaap Soto","Mie Sedaap Kari Spesial",
    "Chitato","Qtela","Taro","Lays",
    "Oreo","Good Time","Roma Kelapa",
    "Beng Beng","SilverQueen","Tic Tac",
    "Wafer Tango","Nabati","Nextar",
    "Aqua","Le Minerale","Club",
    "Teh Botol","Pocari Sweat",
    "Ultra Milk","Milo","Cimory",
    "Kopi Kapal Api","ABC Coffee",
    "Energen","Sari Roti","Richeese",
    "Cheetos","Piattos","Momogi",
    "Yupi","Relaxa","Fox Candy",
    "Kopiko","Torabika","Luwak White Coffee",
    "Frisian Flag","Dancow","Bendera",
    "Susu Zee","Hydro Coco","Floridina",
    "Pulpy Orange","Buavita"
]

# Membuat 500 data

produk = []

for i in range(1, 501):

    produk.append({
        "Nama Produk": random.choice(produk_indomaret),
        "Rak": random.randint(1, 50),
        "Stok": random.randint(10, 100)
    })

# =====================================
# BUBBLE SORT
# =====================================

def bubble_sort(data):

    arr = data.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j]["Nama Produk"] > arr[j+1]["Nama Produk"]:

                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# =====================================
# BINARY SEARCH
# =====================================

def binary_search(data, target):

    low = 0
    high = len(data)-1

    while low <= high:

        mid = (low + high) // 2

        nama = data[mid]["Nama Produk"].lower()

        if nama == target.lower():
            return mid

        elif nama < target.lower():
            low = mid + 1

        else:
            high = mid - 1

    return -1

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("⚙️ Pengaturan")

    jumlah_data = st.slider(
        "Jumlah Produk",
        100,
        500,
        500
    )

    st.divider()

    st.subheader("🔍 Algoritma")

    st.success("Binary Search")

    st.info("Bubble Sort")

# =====================================
# JUDUL
# =====================================

st.title("🛒 Sistem Pencarian Toko princess👸🏼")

st.write(
    "Pencarian nama produk menggunakan Binary Search dan pengurutan menggunakan Bubble Sort."
)

# =====================================
# INFO BOX
# =====================================

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class='info-box'>
    📌 Data produk diurutkan berdasarkan nama produk menggunakan Bubble Sort.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='success-box'>
    📦 Total Produk Aktif : {jumlah_data}
    </div>
    """, unsafe_allow_html=True)

st.divider()

# =====================================
# PENCARIAN
# =====================================

st.header("🔎 Cari Produk")

nama_produk = st.text_input(
    "Masukkan Nama Produk",
    placeholder="Contoh: Chitato"
)

if st.button("Cari Produk"):

    data_sorted = bubble_sort(produk)

    hasil = binary_search(
        data_sorted,
        nama_produk
    )

    if hasil != -1:

        item = data_sorted[hasil]

        st.success(f"""
Produk ditemukan!

Nama Produk : {item['Nama Produk']}
Rak : {item['Rak']}
Stok : {item['Stok']}
        """)

    else:
        st.error("Produk tidak ditemukan.")

st.divider()

# =====================================
# STATISTIK
# =====================================

c1, c2, c3 = st.columns(3)

c1.metric("Total Produk", len(produk))
c2.metric("Jumlah Rak", 50)
c3.metric("Algoritma", "Binary Search")

st.divider()

# =====================================
# TABEL DATA
# =====================================

st.subheader("📋 Data Produk")

df = pd.DataFrame(produk)

st.dataframe(
    df.head(jumlah_data),
    use_container_width=True
)

# =====================================
# GRAFIK
# =====================================

st.subheader("📊 Distribusi Produk per Rak")

grafik = (
    df.groupby("Rak")
      .size()
      .reset_index(name="Jumlah Produk")
)

st.bar_chart(
    grafik.set_index("Rak")
)