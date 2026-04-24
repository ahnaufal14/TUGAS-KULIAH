#Program implementasi struktur data Set dan operasinya

def main():
    # 1. Inisialisasi Set
    # Set otomatis menghapus nilai duplikat
    angka = {1, 2, 3, 4, 4, 5, 1}
    print(f"Set awal : {angka}")

    # 2. Operasi Menambah Elemen (Add)
    angka.add(6)
    print(f"Setelah add(6): {angka}")

    # 4. Operasi Himpunan: Gabungan (Union)
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    gabungan = set_a.union(set_b)
    print(f"hasil union (A + B): {gabungan}")

    # 6. Operasi Himpunan: Selisih
    # Nilai yang ada di A tapi tidak ada di B
    selisih = set_a.difference(set_b)
    print(f"Hasil Difference (A - B): {selisih}")

    # 7. Operasi Menghapus Semua Elemen (Clear)
    angka.clear()
    print(f"Isi set angka setelah clear: {angka}")

main()