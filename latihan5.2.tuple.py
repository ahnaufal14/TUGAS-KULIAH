#Program implementasi struktur data Tuple dan operasinya

def main():
    # 1. Inisialisasi Tuple (Menggunakan tanda kurung biasa)
    # Tuple sering digunakan untuk data yang bersifat tetap
    koordinat = (10, -15, 20)
    print(f"tuple awal: {koordinat}")

    # 2. Operasi Akses Elemen (Indexing)
    # Mengambil nilai pertama (indeks 0)
    garis_lintang = koordinat[0]
    print(f"elemen pada indeks 0: {garis_lintang}")

    # 3. Operasi Slicing
    # Mengambil elemen dari indeks 1 sampai akhir
    bagian_tuple = koordinat[1:]
    print(f"hasil slicing: {bagian_tuple}")

    # 4. Operasi Penjumlahan Tuple (Concatenation)
    # Walaupun tuple tidak bisa diubah, kita bisa menggabungkan dua tuple menjadi tuple baru
    tambahan_data = (100, 200)
    tuple_gabungan = koordinat + tambahan_data
    print(f"hasil gabungan tuple: {tuple_gabungan}")

    #5. Operasi Count (Menghitung kemunculan nilai tertentu)
    nilai_tes = (1, 2, 3, 2, 4, 2, 5)
    jumlah_angka_dua = nilai_tes.count(2)
    print(f"angka 2 muncul sebanyak: {jumlah_angka_dua} kali")

    # 6. Operasi Index (Mencari posisi indeks dari suatu nilai
    posisi_angka_empat = nilai_tes.index(4)
    print(f"angka 4 berada pada indeks ke: {posisi_angka_empat}")

    # 7. Operasi Unpacking
    # Memecah isi tuple ke dalam variabel yang berbeda
    x, y, z = koordinat
    print(f"hasil unpacking > x: {x}, y: {y}, z: {z}")

if __name__ == "__main__":
    main()