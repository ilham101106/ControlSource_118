# Tugas Praktikum 5 Soal Selesai


def task1_evaluasi_nilai():
    print("\n=== TASK 1: EVALUATE STUDENT PERFORMANCE ===")
    nilai = float(input("Masukkan persentase nilai mahasiswa (%): "))
    
    if nilai >= 90:
        print("Performance: Excellent performance")
    elif nilai >= 80:
        print("Performance: Very Good performance")
    elif nilai >= 70:
        print("Performance: Good performance")
    elif nilai >= 60:
        print("Performance: Average performance")
    else:
        print("Performance: Poor performance / Needs improvement")


def task2_angka_terbesar():
    print("\n=== TASK 2: FIND LARGEST OF THREE NUMBERS ===")
    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua  : "))
    num3 = float(input("Masukkan angka ketiga : "))
    
    # Logika mencari angka terbesar menggunakan if-elif-else
    if num1 >= num2 and num1 >= num3:
        terbesar = num1
    elif num2 >= num1 and num2 >= num3:
        terbesar = num2
    else:
        terbesar = num3
        
    print(f"Angka terbesar adalah: {terbesar}")


def task3_fibonacci():
    print("\n=== TASK 3: FIBONACCI SERIES UP TO N ===")
    n = int(input("Masukkan jumlah suku (n): "))
    
    a, b = 0, 1
    print(f"Deret Fibonacci ({n} suku pertama):")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


def task4_bilangan_ganjil():
    print("\n=== TASK 4: ODD NUMBERS UP TO N ===")
    n = int(input("Masukkan nilai batas n: "))
    
    print(f"Bilangan ganjil sampai {n}:")
    for i in range(1, n + 1):
        if i % 2 != 0:  # Jika sisa bagi dengan 2 bukan 0, maka ganjil
            print(i, end=" ")
    print()


def task5_pola_desain():
    print("\n=== TASK 5: NUMBER PATTERN DESIGN ===")
    n = int(input("Masukkan nilai n (contoh: 5): "))
    
    for i in range(1, n + 1):          # Loop luar: mengatur baris ke bawah
        for j in range(i):             # Loop dalam: mencetak angka ke samping
            print(i, end=" ")
        print()                        # Pindah ke baris baru


# Menu Utama untuk Menjalankan Program
if __name__ == "__main__":
    while True:
        print("\n" + "="*40)
        print("   TUGAS PRAKTIKUM PYTHON MULTIPLATFORM")
        print("="*40)
        print("1. Evaluasi Performa Mahasiswa")
        print("2. Cari Angka Terbesar dari 3 Angka")
        print("3. Deret Fibonacci sampai N")
        print("4. Bilangan Ganjil sampai N")
        print("5. Pola Angka Bertingkat")
        print("0. Keluar")
        print("="*40)
        
        pilihan = input("Pilih nomor soal (0-5): ")
        if pilihan == "1":
            task1_evaluasi_nilai()
        elif pilihan == "2":
            task2_angka_terbesar()
        elif pilihan == "3":
            task3_fibonacci()
        elif pilihan == "4":
            task4_bilangan_ganjil()
        elif pilihan == "5":
            task5_pola_desain()
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
