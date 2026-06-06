
daftar_tugas = []

def tambah_tugas(tugas):
    daftar_tugas.append(tugas)

def tampilkan_tugas():
    print("\n===== DAFTAR TUGAS =====")
    for i, t in enumerate(daftar_tugas, start=1):
        print(f"{i}. {t}")
    print("=========================")
    print(f"Total tugas: {len(daftar_tugas)}\n")

nomor = 1
while True:
    tugas = input(f"Masukkan tugas ke-{nomor} (ketik SELESAI untuk berhenti): ")

    if tugas.lower() == "selesai":
        break

    tambah_tugas(tugas)
    nomor += 1

tampilkan_tugas()
