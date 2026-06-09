import streamlit as st
import pandas as pd
import random

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Princess Pharmacy",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# CSS TEMA MODERN APOTEK
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── ROOT VARIABLES ── */
/* Warna tema pink: dari gelap ke terang, dipakai di seluruh komponen */
:root {
    --green-900: #6b0f3a;   /* Pink sangat gelap — sidebar, header utama */
    --green-800: #a01458;   /* Pink gelap — aksen heading, hover */
    --green-600: #d63384;   /* Pink utama — tombol, border aktif, nilai statistik */
    --green-400: #e8619e;   /* Pink medium — gradasi tombol, border history */
    --green-200: #f4b8d4;   /* Pink muda — border input, pill badge */
    --green-100: #fce4ef;   /* Pink sangat muda — baris tabel genap, hover tabel */
    --green-50:  #fff0f6;   /* Pink hampir putih — background zebra tabel */
    --cream:     #fdfdf8;   /* Putih krem — background halaman utama */
    --text-dark: #3b0a20;   /* Teks gelap utama */
    --text-mid:  #7a2d50;   /* Teks sedang — deskripsi, sub-label */
    --text-soft: #b06080;   /* Teks lembut — placeholder, keterangan kecil */
    --white:     #ffffff;
    --shadow:    0 4px 24px rgba(214,51,132,.12);   /* Bayangan pink tipis */
    --shadow-lg: 0 8px 40px rgba(214,51,132,.18);   /* Bayangan pink tebal */
}

/* ── GLOBAL ── */
*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--cream);
    color: var(--text-dark);
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(160deg, var(--green-900) 0%, var(--green-800) 100%);
    border-right: none;
}
[data-testid="stSidebar"] * { color: var(--white) !important; }
[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,.07);
    border-radius: 10px;
    padding: 10px 16px;
    margin-bottom: 6px;
    display: block;
    transition: background .2s;
    font-size: 0.95rem;
    cursor: pointer;
}
[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,.15);
}
[data-testid="stSidebar"] .stRadio [aria-checked="true"] + label {
    background: rgba(255,255,255,.22);
    font-weight: 600;
}

/* ── HEADER BAND ── */
.header-band {
    background: linear-gradient(135deg, var(--green-900) 0%, var(--green-600) 100%);
    border-radius: 18px;
    padding: 40px 48px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
}
.header-band::before {
    content: "💊";
    position: absolute;
    right: 40px; top: 50%;
    transform: translateY(-50%);
    font-size: 96px;
    opacity: .12;
}
.header-band h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.4rem;
    color: var(--white) !important;
    margin: 0 0 6px;
}
.header-band p {
    color: var(--green-200);
    font-size: 1rem;
    font-weight: 300;
    margin: 0;
}

/* ── STAT CARDS ── */
.stat-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 28px;
}
.stat-card {
    background: var(--white);
    border-radius: 14px;
    padding: 22px 24px;
    border-left: 4px solid var(--green-600);
    box-shadow: var(--shadow);
    transition: transform .2s, box-shadow .2s;
}
.stat-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-lg); }
.stat-card .label {
    font-size: .78rem;
    color: var(--text-soft);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: .08em;
    margin-bottom: 6px;
}
.stat-card .value {
    font-size: 1.9rem;
    font-weight: 700;
    color: var(--green-600);
    line-height: 1;
}
.stat-card .sub {
    font-size: .8rem;
    color: var(--text-mid);
    margin-top: 4px;
}

/* ── SEARCH BOX ── */
.stTextInput > div > div > input {
    border-radius: 12px !important;
    border: 2px solid var(--green-200) !important;
    padding: 14px 18px !important;
    font-size: 1rem !important;
    transition: border .2s, box-shadow .2s;
    background: var(--white) !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--green-600) !important;
    box-shadow: 0 0 0 3px rgba(214,51,132,.15) !important;  /* Glow pink saat input aktif */
}

/* ── BUTTONS ── */
div.stButton > button {
    background: linear-gradient(135deg, var(--green-600), var(--green-400)) !important;
    color: var(--white) !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 28px !important;
    font-weight: 600 !important;
    font-size: .95rem !important;
    letter-spacing: .02em;
    transition: opacity .2s, transform .15s !important;
    box-shadow: 0 3px 12px rgba(214,51,132,.3) !important;  /* Shadow pink di bawah tombol */
}
div.stButton > button:hover {
    opacity: .9 !important;
    transform: translateY(-1px) !important;
}

/* ── SELECTBOX ── */
.stSelectbox > div > div {
    border-radius: 12px !important;
    border: 2px solid var(--green-200) !important;
}

/* ── DATAFRAME ── */
.stDataFrame { border-radius: 14px; overflow: hidden; box-shadow: var(--shadow); }
.stDataFrame thead th {
    background: var(--green-900) !important;
    color: var(--white) !important;
    font-weight: 600 !important;
}
.stDataFrame tbody tr:nth-child(even) { background: var(--green-50) !important; }
.stDataFrame tbody tr:hover { background: var(--green-100) !important; }

/* ── RESULT PILLS ── */
.pill {
    display: inline-block;
    background: var(--green-100);
    color: var(--green-800);
    border-radius: 99px;
    padding: 5px 14px;
    font-size: .82rem;
    font-weight: 600;
    margin: 4px 4px 4px 0;
}

/* ── HISTORY ITEM ── */
.history-item {
    background: var(--white);
    border-radius: 12px;
    padding: 14px 20px;
    margin-bottom: 10px;
    border-left: 4px solid var(--green-400);
    box-shadow: 0 2px 10px rgba(214,51,132,.08);  /* Bayangan lembut history item */
    display: flex;
    align-items: center;
    gap: 12px;
    font-size: .95rem;
    color: var(--text-dark);
}
.history-item .idx {
    background: var(--green-600);
    color: white;
    border-radius: 50%;
    width: 26px; height: 26px;
    display: flex; align-items: center; justify-content: center;
    font-size: .75rem;
    font-weight: 700;
    flex-shrink: 0;
}

/* ── INFO CARD ── */
.info-card {
    background: var(--white);
    border-radius: 16px;
    padding: 28px 32px;
    margin-bottom: 16px;
    box-shadow: var(--shadow);
    border-top: 4px solid var(--green-600);
}
.info-card h3 {
    color: var(--green-800) !important;
    font-family: 'Playfair Display', serif;
    margin-top: 0;
}
.info-card p, .info-card li { color: var(--text-mid); line-height: 1.7; }

/* ── ALERT OVERRIDES ── */
.stSuccess { border-radius: 12px !important; }
.stError   { border-radius: 12px !important; }
.stInfo    { border-radius: 12px !important; }

/* ── SUBHEADER ── */
h2 { color: var(--green-900) !important; font-family: 'Playfair Display', serif !important; }

/* ── DIVIDER ── */
hr { border-color: var(--green-100) !important; }

/* ── SIDEBAR BRAND ── */
.sidebar-brand {
    text-align: center;
    padding: 24px 0 28px;
    border-bottom: 1px solid rgba(255,255,255,.15);
    margin-bottom: 20px;
}
.sidebar-brand .icon { font-size: 2.8rem; }
.sidebar-brand h2 {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.3rem !important;
    color: white !important;
    margin: 8px 0 4px;
}
.sidebar-brand small { color: rgba(255,255,255,.6); font-size: .8rem; }
</style>
""", unsafe_allow_html=True)

# =========================
# DATA OBAT (500 DATA)
# =========================
random.seed(42)

nama_obat = [
    "Paracetamol", "Amoxicillin", "Promag", "Bodrex", "Antangin",
    "Oskadon", "Panadol", "Sanmol", "Tempra", "Proris",
    "Decolgen", "Mixagrip", "OBH Combi", "Woods", "Komix",
    "Cetirizine", "Loratadine", "CTM", "Alleron", "Amlodipine",
    "Captopril", "Omeprazole", "Lansoprazole", "Mylanta", "Polysilane",
    "Oralit", "Diapet", "Entrostop", "Imodium", "Betadine",
    "Insto", "Rohto", "Vitacimin", "CDR", "Redoxon",
    "Bioplacenton", "Gentamicin", "Canesten", "Nystatin", "Kalmicetine",
    "Neurobion", "Sangobion", "Becom-Zet", "Enervon-C", "Stimuno",
    "Curcuma Plus", "Scott Emulsion", "Tolak Angin", "Laserin", "Siladex"
]

varian = [
    "250 mg", "500 mg", "650 mg", "Tablet", "Kapsul",
    "Sirup 60 ml", "Sirup 100 ml", "Forte", "Extra", "Anak"
]

kategori_list = ["Demam", "Flu", "Batuk", "Maag", "Diare",
                 "Vitamin", "Antibiotik", "Alergi", "Kulit", "Mata"]

bentuk_list = ["Tablet", "Kapsul", "Sirup", "Salep"]

KATEGORI_ICON = {
    "Demam": "🌡️", "Flu": "🤧", "Batuk": "😮‍💨", "Maag": "🫀",
    "Diare": "💧", "Vitamin": "💊", "Antibiotik": "🧬",
    "Alergi": "🌸", "Kulit": "🩹", "Mata": "👁️"
}

data_obat = []
for nama in nama_obat:
    for v in varian:
        data_obat.append({
            "Nama Obat":  f"{nama} {v}",
            "Kategori":   random.choice(kategori_list),
            "Harga (Rp)": random.randint(5000, 100000),
            "Stok":       random.randint(10, 200),
            "Bentuk":     random.choice(bentuk_list)
        })

# =========================
# BUBBLE SORT
# =========================
# Bubble Sort adalah algoritma pengurutan sederhana.
# Cara kerja: membandingkan dua elemen yang berdampingan (arr[j] dan arr[j+1]),
# jika urutannya salah (a > b), maka keduanya ditukar (swap).
# Proses ini diulang sebanyak n kali hingga seluruh data terurut secara alfabetis.
# Kompleksitas waktu: O(n²) — cocok untuk data berukuran sedang.
def bubble_sort(data):
    arr = data.copy()        # Salin data agar data asli tidak berubah
    n = len(arr)             # Jumlah total elemen
    for i in range(n):       # Iterasi luar: n putaran penuh
        for j in range(0, n - i - 1):   # Iterasi dalam: bandingkan elemen berdampingan
            # Jika nama obat [j] lebih besar dari [j+1], tukar posisi (swap)
            if arr[j]["Nama Obat"].lower() > arr[j+1]["Nama Obat"].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr  # Kembalikan data yang sudah terurut alfabetis

sorted_data = bubble_sort(data_obat)

# =========================
# BINARY SEARCH
# =========================
# Binary Search adalah algoritma pencarian cepat pada data yang SUDAH terurut.
# Cara kerja: cek elemen tengah (mid), lalu sempitkan pencarian ke kiri atau kanan.
# Jika target == mid → ketemu! Jika target > mid → cari di kanan. Jika target < mid → cari di kiri.
# Kompleksitas waktu: O(log n) — jauh lebih cepat dari Linear Search O(n).
def binary_search(data, target):
    low, high = 0, len(data) - 1  # Batas bawah dan atas pencarian
    target = target.lower()        # Ubah ke huruf kecil agar tidak case-sensitive
    while low <= high:
        mid = (low + high) // 2    # Hitung indeks tengah
        nama = data[mid]["Nama Obat"].lower()
        if nama == target:         # Target ditemukan tepat di tengah
            return data[mid]
        elif nama < target:        # Target ada di sebelah KANAN, geser batas bawah
            low = mid + 1
        else:                      # Target ada di sebelah KIRI, geser batas atas
            high = mid - 1
    return None  # Target tidak ditemukan

# =========================
# SESSION STATE
# =========================
# Session State di Streamlit berfungsi menyimpan data selama aplikasi berjalan.
# Tanpa ini, setiap interaksi pengguna akan me-reset semua variabel.
# Di sini kita simpan riwayat pencarian agar tidak hilang saat halaman di-refresh.
if "history" not in st.session_state:
    st.session_state.history = []  # Inisialisasi list riwayat pencarian pertama kali

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="icon">💊</div>
        <h2>Princess Pharmacy</h2>
        <small>Sistem Informasi Apotek</small>
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "Navigasi",
        ["🔍  Cari Obat", "📋  Data Obat", "🕒  Riwayat", "ℹ️  Tentang Sistem"],
        label_visibility="collapsed"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<small style='opacity:.6'>Total Obat: <b>{len(sorted_data)}</b></small>", unsafe_allow_html=True)
    st.markdown(f"<small style='opacity:.6'>Riwayat: <b>{len(st.session_state.history)}</b> pencarian</small>", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="header-band">
    <h1>Princess Pharmacy 💊</h1>
    <p>Sistem Pencarian & Manajemen Data Obat Apotek Berbasis Web</p>
</div>
""", unsafe_allow_html=True)

# =========================
# STATISTIK RINGKASAN
# =========================
df_all = pd.DataFrame(sorted_data)
total_stok    = df_all["Stok"].sum()
harga_rata    = int(df_all["Harga (Rp)"].mean())
jenis_kategori = df_all["Kategori"].nunique()

st.markdown(f"""
<div class="stat-row">
    <div class="stat-card">
        <div class="label">Total Obat</div>
        <div class="value">{len(sorted_data):,}</div>
        <div class="sub">Jenis produk tersedia</div>
    </div>
    <div class="stat-card">
        <div class="label">Total Stok</div>
        <div class="value">{total_stok:,}</div>
        <div class="sub">Unit keseluruhan</div>
    </div>
    <div class="stat-card">
        <div class="label">Harga Rata-rata</div>
        <div class="value">Rp {harga_rata:,}</div>
        <div class="sub">Per produk</div>
    </div>
    <div class="stat-card">
        <div class="label">Kategori</div>
        <div class="value">{jenis_kategori}</div>
        <div class="sub">Jenis kategori obat</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================
# MENU: CARI OBAT
# =========================
if "Cari Obat" in menu:

    st.markdown("## 🔍 Pencarian Obat")
    st.markdown("<p style='color:var(--text-soft);margin-top:-12px'>Gunakan kata kunci nama obat untuk menemukan produk yang tersedia.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_input, col_btn = st.columns([4, 1])
    with col_input:
        keyword = st.text_input(
            "Nama Obat",
            placeholder="Contoh: Paracetamol 500 mg ...",
            label_visibility="collapsed"
        )
    with col_btn:
        cari = st.button("🔍 Cari", use_container_width=True)

    if cari:
        if not keyword.strip():
            st.warning("⚠️ Silakan masukkan nama obat terlebih dahulu.")
        else:
            st.session_state.history.append(keyword.strip())

            hasil = [item for item in sorted_data if keyword.lower() in item["Nama Obat"].lower()]

            if hasil:
                st.success(f"✅ Ditemukan **{len(hasil)}** produk untuk kata kunci **'{keyword}'**")

                # Ringkasan kategori temuan
                df_hasil = pd.DataFrame(hasil)
                kat_counts = df_hasil["Kategori"].value_counts()
                pill_html = "".join(
                    f'<span class="pill">{KATEGORI_ICON.get(k,"💊")} {k} ({v})</span>'
                    for k, v in kat_counts.items()
                )
                st.markdown(f"<div style='margin:8px 0 16px'>{pill_html}</div>", unsafe_allow_html=True)

                st.dataframe(
                    df_hasil,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "Harga (Rp)": st.column_config.NumberColumn(format="Rp %d"),
                        "Stok":       st.column_config.ProgressColumn(
                                          min_value=0, max_value=200, format="%d unit"
                                      )
                    }
                )
            else:
                st.error(f"❌ Obat **'{keyword}'** tidak ditemukan dalam database.")
                st.info("💡 Coba gunakan nama umum seperti 'Paracetamol', 'Amoxicillin', atau 'Vitamin C'.")

# =========================
# MENU: DATA OBAT
# =========================
elif "Data Obat" in menu:

    st.markdown("## 📋 Data Obat")
    st.markdown("<p style='color:var(--text-soft);margin-top:-12px'>Seluruh data obat yang tersedia, terurut berdasarkan nama (Bubble Sort).</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    col_kat, col_bentuk, col_harga = st.columns(3)
    with col_kat:
        kategori = st.selectbox("Filter Kategori", ["Semua"] + kategori_list)
    with col_bentuk:
        bentuk = st.selectbox("Filter Bentuk", ["Semua"] + bentuk_list)
    with col_harga:
        harga_max = st.slider("Harga Maks (Rp)", 5000, 100000, 100000, step=5000)

    df = df_all.copy()
    if kategori != "Semua":
        df = df[df["Kategori"] == kategori]
    if bentuk != "Semua":
        df = df[df["Bentuk"] == bentuk]
    df = df[df["Harga (Rp)"] <= harga_max]

    st.markdown(f"<p style='color:var(--text-soft);font-size:.9rem'>Menampilkan <b>{len(df)}</b> dari <b>{len(sorted_data)}</b> produk</p>", unsafe_allow_html=True)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Harga (Rp)": st.column_config.NumberColumn(format="Rp %d"),
            "Stok":       st.column_config.ProgressColumn(
                              min_value=0, max_value=200, format="%d unit"
                          ),
            "Kategori":   st.column_config.TextColumn()
        }
    )

# =========================
# MENU: RIWAYAT
# =========================
elif "Riwayat" in menu:

    st.markdown("## 🕒 Riwayat Pencarian")
    st.markdown("<p style='color:var(--text-soft);margin-top:-12px'>Daftar kata kunci yang pernah dicari dalam sesi ini.</p>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    if not st.session_state.history:
        st.info("📭 Belum ada riwayat pencarian. Coba cari obat terlebih dahulu.")
    else:
        col_clear = st.columns([4, 1])[1]
        with col_clear:
            if st.button("🗑️ Hapus Semua", use_container_width=True):
                st.session_state.history = []
                st.rerun()

        for i, item in enumerate(reversed(st.session_state.history), 1):
            st.markdown(f"""
            <div class="history-item">
                <div class="idx">{i}</div>
                <span>{item}</span>
            </div>
            """, unsafe_allow_html=True)

# =========================
# MENU: TENTANG SISTEM
# =========================
elif "Tentang" in menu:

    st.markdown("## ℹ️ Tentang Sistem")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>🔃 Bubble Sort</h3>
            <p>Algoritma pengurutan yang membandingkan dua elemen bersebelahan dan menukarnya jika
            urutannya salah. Digunakan untuk <b>mengurutkan seluruh data obat</b> berdasarkan nama
            secara alfabetis sebelum ditampilkan maupun dicari.</p>
            <ul>
                <li>Kompleksitas waktu: O(n²)</li>
                <li>Mudah dipahami & diimplementasikan</li>
                <li>Cocok untuk dataset berukuran sedang</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🔎 Binary Search</h3>
            <p>Algoritma pencarian yang bekerja pada data <b>terurut</b> dengan membagi ruang pencarian
            menjadi dua pada setiap iterasi. Digunakan untuk <b>pencarian cepat</b> nama obat secara
            eksak.</p>
            <ul>
                <li>Kompleksitas waktu: O(log n)</li>
                <li>Jauh lebih cepat dari Linear Search</li>
                <li>Memerlukan data yang sudah terurut</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-card" style="border-top-color:#e8619e">  <!-- Pink medium untuk variasi kartu -->
        <h3>🛠️ Teknologi & Spesifikasi</h3>
        <p>Sistem ini dibangun menggunakan teknologi open-source modern yang ringan dan efisien.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, label, value in zip(
        [c1, c2, c3, c4],
        ["Bahasa", "Framework", "Total Data", "Algoritma"],
        ["Python 3", "Streamlit", f"{len(sorted_data):,} obat", "Sort + Search"]
    ):
        with col:
            st.metric(label, value)