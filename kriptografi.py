import streamlit as st

# Fungsi Enkripsi Caesar Cipher
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# Fungsi Dekripsi Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Tampilan Web
st.set_page_config(page_title="Aplikasi Kriptografi Pesan", page_icon="🔐")

st.title("🔐 Aplikasi Kriptografi Berbasis Pesan")
st.write("Menggunakan Algoritma Caesar Cipher")

menu = st.radio(
    "Pilih Operasi:",
    ["Enkripsi Pesan", "Dekripsi Pesan"]
)

pesan = st.text_area("Masukkan Pesan")
shift = st.slider("Kunci Perpindahan (Shift)", 1, 25, 3)

if st.button("Proses"):
    if pesan:
        if menu == "Enkripsi Pesan":
            hasil = encrypt(pesan, shift)
            st.success("Pesan Berhasil Dienkripsi")
            st.code(hasil)
        else:
            hasil = decrypt(pesan, shift)
            st.success("Pesan Berhasil Didekripsi")
            st.code(hasil)
    else:
        st.warning("Masukkan pesan terlebih dahulu!")

st.markdown("---")
st.info("""
Algoritma yang digunakan:
- Caesar Cipher
- Kompleksitas Enkripsi: O(n)
- Kompleksitas Dekripsi: O(n)

Keterangan:
- Setiap huruf digeser sesuai nilai kunci (shift).
- Contoh: A → D jika shift = 3.
""")