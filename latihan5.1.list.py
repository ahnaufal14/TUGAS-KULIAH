#Program implementasi struktur data List dan operasinya

def main():
    # 1. Inisialisasi List (Membuat list awal)
    buah = ["apel", "mangga", "jeruk"]
    print(f"list awal: {buah}")

    #2. Operasi Append (Menambah elemen ke akhir list
    buah.append("pisang")
    print(f"setelah ditambahkan: {buah}")

    # 3. Operasi Insert (Menambah elemen di indeks tertentu)
    # Menambah 'Anggur' di posisi indeks ke-1
    buah.insert(1, "anggur")
    print(f"setelah anggur ditaruh di pertama: {buah}")

    # 4. Operasi Mengubah Elemen
    # Mengubah Jeruk menjadi Leci
    buah[3] = "leci"
    print(f"setelah jeruk diganti leci:{buah}")

    # 5. Operasi Remove (Menghapus elemen berdasarkan nilai)
    buah.remove("mangga")
    print(f"setelah mangga dihapus: {buah}")

    # 6. Operasi Pop (Menghapus elemen berdasarkan indeks)
    # Menghapus elemen terakhir
    buah.pop()
    print(f"setelah dihapus yang terakhir: {buah}")

    # 7. Operasi Slicing (Mengambil sebagian isi list)
    sub_list = buah [0:2]
    print(f"hasil slicing: {sub_list}")

    # 8. Operasi Count & Sort
    print(f"Jumlah elemen dalam list: {len(buah)}")
    buah.sort()
    print(f"setelah diurutkan: {buah}")

if __name__ == "__main__":
    main()