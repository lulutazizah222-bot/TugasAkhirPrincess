from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class KasirApp(App):
    def build(self):

        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        title = Label(text="Aplikasi Kasir Sederhana", font_size=24)

        self.harga = TextInput(hint_text="Masukkan Harga Barang", input_filter='int')
        self.jumlah = TextInput(hint_text="Masukkan Jumlah Barang", input_filter='int')

        self.hasil = Label(text="Total Harga: ")

        tombol = Button(text="Hitung Total")

        tombol.bind(on_press=self.hitung_total)

        layout.add_widget(title)
        layout.add_widget(self.harga)
        layout.add_widget(self.jumlah)
        layout.add_widget(tombol)
        layout.add_widget(self.hasil)

        return layout

    def hitung_total(self, instance):
        try:
            harga = int(self.harga.text)
            jumlah = int(self.jumlah.text)

            total = harga * jumlah

            self.hasil.text = f"Total Harga: Rp {total}"

        except:
            self.hasil.text = "Input harus angka"

KasirApp().run()
