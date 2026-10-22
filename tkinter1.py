import tkinter as tk

# Membuat jendela aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x550")

# Label judul
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold")
)
judul.pack(pady=15)

# Daftar mata pelajaran
mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Bahasa arab",
    "Biologi",
    "Informatika",
    "Sejarah",
    "Sosiologi",
    "Geografi"
]

# Membuat input nilai
input_nilai = []

for pelajaran in mapel:
    frame = tk.Frame(root)
    frame.pack(pady=3)

    label = tk.Label(frame, text=pelajaran, width=18, anchor="w")
    label.pack(side="left")

    