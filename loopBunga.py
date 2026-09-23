import turtle
import time

# Inisialisasi turtle
t = turtle.Turtle()
t.speed(10)  # Kecepatan sedang agar terlihat proses menggambarnya (1=paling lambat, 10=cepat)

# Fungsi untuk menggambar satu buah bunga lengkap
def gambar_satu_bunga(x, y, warna_garis, warna_isi, warna_inti):
    # Pindah posisi tanpa meninggalkan garis
    t.penup()
    t.goto(x, y)
    t.pendown()

    jumlah_kelopak = 8
    
    # 1. Gambar Kelopak
    t.color(warna_garis, warna_isi)
    t.begin_fill()
    for _ in range(jumlah_kelopak):
        t.circle(70, 60)
        t.left(120)
        t.circle(70, 60)
        t.left(120)
        t.right(360 / jumlah_kelopak)
    t.end_fill()

    # 2. Gambar Inti Bunga di Tengah
    t.penup()
    t.goto(x, y - 18)  # Sesuaikan titik tengah lingkaran inti
    t.pendown()
    t.color("orange", warna_inti)
    t.begin_fill()
    t.circle(18)
    t.end_fill()

# Daftar koordinat dan kombinasi warna untuk 3 bunga
daftar_bunga = [
    {"x": -180, "y": 0, "garis": "red", "isi": "pink", "inti": "yellow"},
    {"x": 0,    "y": 50, "garis": "purple", "isi": "plum", "inti": "gold"},
    {"x": 180,  "y": 0, "garis": "darkblue", "isi": "skyblue", "inti": "orange"}
]

# Loop untuk menggambar 3 bunga dengan jeda waktu (timing)
for i, b in enumerate(daftar_bunga):
    print(f"Menggambar bunga ke-{i + 1}...")
    gambar_satu_bunga(b["x"], b["y"], b["garis"], b["isi"], b["inti"])
    
    # Memberi jeda waktu 1.5 detik sebelum bunga berikutnya digambar
    time.sleep(1.5)

t.hideturtle()
print("Selesai menggambar semua bunga!")
turtle.done() 