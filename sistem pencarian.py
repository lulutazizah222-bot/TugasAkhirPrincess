"""
==========================================================
  GUI Sistem Pencarian Produk E-Commerce
  Menggunakan Tkinter — 3 Algoritma Pencarian
  Jalankan: python gui_pencarian_produk.py
==========================================================
"""

import tkinter as tk
from tkinter import ttk, messagebox
import random
import math
import time


# ============================================================
# ALGORITMA PENCARIAN
# ============================================================

def linear_search(data: list, target: int) -> tuple[int, int]:
    """O(n) — cocok untuk data tidak terurut."""
    iterasi = 0
    for i, val in enumerate(data):
        iterasi += 1
        if val == target:
            return i, iterasi
    return -1, iterasi


def binary_search(data: list, target: int) -> tuple[int, int]:
    """O(log n) — data harus terurut."""
    kiri, kanan = 0, len(data) - 1
    iterasi = 0
    while kiri <= kanan:
        iterasi += 1
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return tengah, iterasi
        elif data[tengah] < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1, iterasi


def jump_search(data: list, target: int) -> tuple[int, int]:
    """O(√n) — data terurut, cocok untuk dataset besar."""
    n = len(data)
    langkah = int(math.sqrt(n))
    sebelumnya = 0
    iterasi = 0

    while data[min(langkah, n) - 1] < target:
        iterasi += 1
        sebelumnya = langkah
        langkah += int(math.sqrt(n))
        if sebelumnya >= n:
            return -1, iterasi

    while data[sebelumnya] < target:
        iterasi += 1
        sebelumnya += 1
        if sebelumnya == min(langkah, n):
            return -1, iterasi

    iterasi += 1
    if data[sebelumnya] == target:
        return sebelumnya, iterasi
    return -1, iterasi


# ============================================================
# APLIKASI GUI
# ============================================================

class AppPencarian:
    # Palet warna — dark industrial/techy
    BG        = "#0d1117"
    PANEL     = "#161b22"
    CARD      = "#1c2128"
    BORDER    = "#30363d"
    ACCENT    = "#00b4d8"
    ACCENT2   = "#90e0ef"
    SUCCESS   = "#3fb950"
    DANGER    = "#f85149"
    WARN      = "#d29922"
    TEXT      = "#e6edf3"
    TEXT_DIM  = "#8b949e"
    BTN_ALG   = "#21262d"

    ALGO_INFO = {
        "Linear Search": {
            "icon": "⟶",
            "desc": "Telusuri satu per satu dari awal hingga akhir.",
            "complexity": "O(n)",
            "color": "#f0883e",
            "note": "Tidak perlu data terurut",
        },
        "Binary Search": {
            "icon": "⟺",
            "desc": "Bagi dua array berulang kali hingga target ditemukan.",
            "complexity": "O(log n)",
            "color": "#00b4d8",
            "note": "Data harus terurut",
        },
        "Jump Search": {
            "icon": "⤻",
            "desc": "Lompat √n elemen, lalu linear di blok yang tepat.",
            "complexity": "O(√n)",
            "color": "#3fb950",
            "note": "Data harus terurut",
        },
    }

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("🔍 Pencarian Produk E-Commerce")
        self.root.geometry("860x680")
        self.root.configure(bg=self.BG)
        self.root.resizable(False, False)

        self.algoritma_var = tk.StringVar(value="Linear Search")
        self.data_produk: list[int] = []
        self.log_riwayat: list[str] = []

        self._build_ui()
        self._generate_data()

    # ── UI Builder ──────────────────────────────────────────

    def _build_ui(self):
        # Header
        hdr = tk.Frame(self.root, bg=self.BG)
        hdr.pack(fill="x", padx=24, pady=(20, 0))

        tk.Label(hdr, text="E-COMMERCE", font=("Courier New", 10, "bold"),
                 bg=self.BG, fg=self.ACCENT).pack(anchor="w")
        tk.Label(hdr, text="Sistem Pencarian Produk",
                 font=("Courier New", 22, "bold"),
                 bg=self.BG, fg=self.TEXT).pack(anchor="w")
        tk.Frame(self.root, bg=self.BORDER, height=1).pack(fill="x", padx=24, pady=(10, 0))

        body = tk.Frame(self.root, bg=self.BG)
        body.pack(fill="both", expand=True, padx=24, pady=12)

        # Kolom kiri
        left = tk.Frame(body, bg=self.BG, width=310)
        left.pack(side="left", fill="y", padx=(0, 12))
        left.pack_propagate(False)
        self._build_left(left)

        # Kolom kanan
        right = tk.Frame(body, bg=self.BG)
        right.pack(side="left", fill="both", expand=True)
        self._build_right(right)

    def _build_left(self, parent):
        # ── Pilih Algoritma ──
        self._section_label(parent, "PILIH ALGORITMA")

        for nama, info in self.ALGO_INFO.items():
            self._algo_radio(parent, nama, info)

        # ── Info Algoritma ──
        self._section_label(parent, "INFO ALGORITMA")
        self.info_frame = tk.Frame(parent, bg=self.CARD,
                                   highlightbackground=self.BORDER,
                                   highlightthickness=1)
        self.info_frame.pack(fill="x", pady=(0, 12))
        self.lbl_icon       = tk.Label(self.info_frame, text="", font=("Courier New", 28),
                                        bg=self.CARD, fg=self.ACCENT)
        self.lbl_icon.pack(pady=(12, 2))
        self.lbl_complexity = tk.Label(self.info_frame, text="", font=("Courier New", 16, "bold"),
                                        bg=self.CARD, fg=self.ACCENT2)
        self.lbl_complexity.pack()
        self.lbl_desc       = tk.Label(self.info_frame, text="", font=("Courier New", 9),
                                        bg=self.CARD, fg=self.TEXT_DIM,
                                        wraplength=260, justify="center")
        self.lbl_desc.pack(padx=10, pady=(4, 2))
        self.lbl_note       = tk.Label(self.info_frame, text="", font=("Courier New", 9, "italic"),
                                        bg=self.CARD, fg=self.WARN)
        self.lbl_note.pack(pady=(0, 12))

        self._update_info()

        # ── Data Produk ──
        self._section_label(parent, "PENGATURAN DATA")
        ctrl = tk.Frame(parent, bg=self.BG)
        ctrl.pack(fill="x", pady=(0, 6))

        tk.Label(ctrl, text="Jumlah Produk:", font=("Courier New", 9),
                 bg=self.BG, fg=self.TEXT_DIM).pack(side="left")
        self.spin_jumlah = tk.Spinbox(ctrl, from_=10, to=500, width=6,
                                      font=("Courier New", 10),
                                      bg=self.CARD, fg=self.TEXT,
                                      buttonbackground=self.BTN_ALG,
                                      insertbackground=self.ACCENT,
                                      highlightbackground=self.BORDER,
                                      highlightthickness=1,
                                      relief="flat")
        self.spin_jumlah.delete(0, "end")
        self.spin_jumlah.insert(0, "30")
        self.spin_jumlah.pack(side="right")

        self.var_terurut = tk.BooleanVar(value=False)
        chk = tk.Checkbutton(parent, text="Data Terurut (Sorted)",
                              variable=self.var_terurut,
                              font=("Courier New", 9),
                              bg=self.BG, fg=self.TEXT_DIM,
                              selectcolor=self.CARD,
                              activebackground=self.BG,
                              activeforeground=self.ACCENT,
                              command=self._on_sorted_toggle)
        chk.pack(anchor="w")

        self._btn(parent, "⟳  Generate Data Baru", self._generate_data,
                  color=self.BTN_ALG, fg=self.TEXT)

    def _build_right(self, parent):
        # ── Input Pencarian ──
        self._section_label(parent, "CARI ID PRODUK")

        row = tk.Frame(parent, bg=self.BG)
        row.pack(fill="x", pady=(0, 10))

        self.entry_id = tk.Entry(row, font=("Courier New", 14, "bold"),
                                  bg=self.CARD, fg=self.ACCENT2,
                                  insertbackground=self.ACCENT,
                                  highlightbackground=self.ACCENT,
                                  highlightthickness=1,
                                  relief="flat", width=14)
        self.entry_id.pack(side="left", ipady=8, padx=(0, 8))
        self.entry_id.bind("<Return>", lambda e: self._cari())

        self._btn(row, "🔍  CARI", self._cari,
                  color=self.ACCENT, fg=self.BG, side="left")
        self._btn(row, "🎲 Acak ID", self._random_id,
                  color=self.BTN_ALG, fg=self.TEXT_DIM, side="left", padx=(6,0))

        # ── Hasil ──
        self._section_label(parent, "HASIL")
        self.result_frame = tk.Frame(parent, bg=self.CARD,
                                      highlightbackground=self.BORDER,
                                      highlightthickness=1, height=90)
        self.result_frame.pack(fill="x", pady=(0, 10))
        self.result_frame.pack_propagate(False)
        self.lbl_result = tk.Label(self.result_frame,
                                    text="Masukkan ID Produk lalu tekan CARI",
                                    font=("Courier New", 11),
                                    bg=self.CARD, fg=self.TEXT_DIM,
                                    wraplength=480, justify="left")
        self.lbl_result.pack(expand=True, anchor="w", padx=14)

        # ── Array Visualisasi ──
        self._section_label(parent, "VISUALISASI ARRAY")
        self.canvas = tk.Canvas(parent, bg=self.CARD, height=60,
                                 highlightbackground=self.BORDER,
                                 highlightthickness=1)
        self.canvas.pack(fill="x", pady=(0, 10))

        # ── Riwayat ──
        self._section_label(parent, "RIWAYAT PENCARIAN")
        log_frame = tk.Frame(parent, bg=self.CARD,
                              highlightbackground=self.BORDER,
                              highlightthickness=1)
        log_frame.pack(fill="both", expand=True)
        self.log_text = tk.Text(log_frame, font=("Courier New", 9),
                                 bg=self.CARD, fg=self.TEXT_DIM,
                                 insertbackground=self.ACCENT,
                                 relief="flat", state="disabled",
                                 height=7)
        sb = ttk.Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self.log_text.pack(fill="both", expand=True, padx=6, pady=4)

    # ── Widget Helpers ───────────────────────────────────────

    def _section_label(self, parent, text):
        f = tk.Frame(parent, bg=self.BG)
        f.pack(fill="x", pady=(10, 4))
        tk.Label(f, text=text, font=("Courier New", 8, "bold"),
                 bg=self.BG, fg=self.TEXT_DIM).pack(side="left")
        tk.Frame(f, bg=self.BORDER, height=1).pack(side="left",
                                                    fill="x", expand=True, padx=(6, 0))

    def _algo_radio(self, parent, nama, info):
        f = tk.Frame(parent, bg=self.BTN_ALG,
                     highlightbackground=self.BORDER, highlightthickness=1,
                     cursor="hand2")
        f.pack(fill="x", pady=2)

        rb = tk.Radiobutton(f, text=f"{info['icon']}  {nama}",
                             variable=self.algoritma_var, value=nama,
                             font=("Courier New", 10, "bold"),
                             bg=self.BTN_ALG, fg=info["color"],
                             activebackground=self.BTN_ALG,
                             activeforeground=info["color"],
                             selectcolor=self.CARD,
                             indicatoron=True,
                             command=self._update_info)
        rb.pack(side="left", padx=10, pady=8)

        tk.Label(f, text=info["complexity"],
                 font=("Courier New", 9),
                 bg=self.BTN_ALG, fg=self.TEXT_DIM).pack(side="right", padx=10)

    def _btn(self, parent, text, cmd, color=None, fg=None,
             side="top", padx=0):
        color = color or self.ACCENT
        fg    = fg    or self.BG
        b = tk.Button(parent, text=text, command=cmd,
                      font=("Courier New", 10, "bold"),
                      bg=color, fg=fg,
                      activebackground=self.ACCENT2,
                      activeforeground=self.BG,
                      relief="flat", cursor="hand2",
                      padx=12, pady=6)
        b.pack(side=side, pady=(4, 0), padx=padx, anchor="w" if side=="top" else None)

    # ── Logic ────────────────────────────────────────────────

    def _update_info(self):
        nama = self.algoritma_var.get()
        info = self.ALGO_INFO[nama]
        self.lbl_icon.config(text=info["icon"], fg=info["color"])
        self.lbl_complexity.config(text=info["complexity"], fg=info["color"])
        self.lbl_desc.config(text=info["desc"])
        self.lbl_note.config(text=f"⚠ {info['note']}")

    def _on_sorted_toggle(self):
        algo = self.algoritma_var.get()
        terurut = self.var_terurut.get()
        if not terurut and algo in ("Binary Search", "Jump Search"):
            self.algoritma_var.set("Linear Search")
            self._update_info()
        self._generate_data()

    def _generate_data(self):
        try:
            n = int(self.spin_jumlah.get())
            n = max(10, min(500, n))
        except Exception:
            n = 30

        self.data_produk = random.sample(range(1000, 9999), n)
        if self.var_terurut.get():
            self.data_produk.sort()

        self._draw_array(-1)
        self._log(f"[DATA] {n} produk di-generate {'(terurut)' if self.var_terurut.get() else '(acak)'}")
        self.lbl_result.config(
            text=f"✔ {n} produk di-load. Masukkan ID untuk dicari.",
            fg=self.TEXT_DIM)

    def _random_id(self):
        if self.data_produk:
            self.entry_id.delete(0, "end")
            self.entry_id.insert(0, str(random.choice(self.data_produk)))

    def _cari(self):
        raw = self.entry_id.get().strip()
        if not raw.isdigit():
            messagebox.showwarning("Input Salah", "Masukkan ID Produk berupa angka!")
            return

        target = int(raw)
        algo   = self.algoritma_var.get()
        terurut = self.var_terurut.get()

        # Validasi syarat
        if algo in ("Binary Search", "Jump Search") and not terurut:
            messagebox.showerror(
                "Data Tidak Terurut",
                f"{algo} membutuhkan data TERURUT!\n"
                "Centang 'Data Terurut' atau pilih Linear Search."
            )
            return

        # Eksekusi pencarian
        t0 = time.perf_counter()
        if algo == "Linear Search":
            indeks, iterasi = linear_search(self.data_produk, target)
        elif algo == "Binary Search":
            indeks, iterasi = binary_search(self.data_produk, target)
        else:
            indeks, iterasi = jump_search(self.data_produk, target)
        durasi = round((time.perf_counter() - t0) * 1_000_000, 2)

        # Tampilkan hasil
        info = self.ALGO_INFO[algo]
        if indeks != -1:
            pesan = (f"✅  DITEMUKAN!   ID: {target}   →   Rak ke-{indeks}  (indeks [{indeks}])\n"
                     f"     Algoritma: {algo} {info['complexity']}  |  "
                     f"Iterasi: {iterasi}  |  Waktu: {durasi} µs")
            self.lbl_result.config(text=pesan, fg=self.SUCCESS)
        else:
            pesan = (f"❌  TIDAK DITEMUKAN   ID: {target}\n"
                     f"     Algoritma: {algo} {info['complexity']}  |  "
                     f"Iterasi: {iterasi}  |  Waktu: {durasi} µs")
            self.lbl_result.config(text=pesan, fg=self.DANGER)

        self._draw_array(indeks)
        self._log(f"[{algo}] ID={target} → " +
                  (f"indeks[{indeks}] ✓ ({iterasi} iter, {durasi}µs)"
                   if indeks != -1 else f"tidak ditemukan ({iterasi} iter, {durasi}µs)"))

    # ── Visualisasi ──────────────────────────────────────────

    def _draw_array(self, highlight_idx: int):
        self.canvas.delete("all")
        data  = self.data_produk
        if not data:
            return

        W = self.canvas.winfo_width() or 520
        H = 60
        n = min(len(data), 60)   # tampilkan maks 60 kotak
        cell_w = max(8, (W - 10) / n)

        for i in range(n):
            x1 = 5 + i * cell_w
            x2 = x1 + cell_w - 2
            y1, y2 = 8, H - 8

            if i == highlight_idx:
                fill   = self.SUCCESS
                border = "#ffffff"
                txt_c  = "#000000"
            else:
                fill   = self.BTN_ALG
                border = self.BORDER
                txt_c  = self.TEXT_DIM

            self.canvas.create_rectangle(x1, y1, x2, y2,
                                          fill=fill, outline=border)
            if cell_w > 18:
                self.canvas.create_text((x1+x2)/2, (y1+y2)/2,
                                         text=str(i), fill=txt_c,
                                         font=("Courier New", 7))

        if highlight_idx != -1 and highlight_idx < n:
            x1 = 5 + highlight_idx * cell_w
            x2 = x1 + cell_w - 2
            self.canvas.create_text((x1+x2)/2 + 1, 4,
                                     text="▼", fill=self.SUCCESS,
                                     font=("Courier New", 8, "bold"))

    # ── Log ──────────────────────────────────────────────────

    def _log(self, msg: str):
        ts = time.strftime("%H:%M:%S")
        baris = f"[{ts}] {msg}\n"
        self.log_riwayat.append(baris)
        self.log_text.config(state="normal")
        self.log_text.insert("end", baris)
        self.log_text.see("end")
        self.log_text.config(state="disabled")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()

    # Style scrollbar
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Vertical.TScrollbar",
                    background="#21262d",
                    troughcolor="#0d1117",
                    arrowcolor="#8b949e")

    app = AppPencarian(root)
    root.mainloop()