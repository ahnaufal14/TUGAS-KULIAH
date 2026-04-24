#Program implementasi struktur data Dictionary dan operasinya

def main():
    # 1. Inisialisasi Dictionary (Menggunakan kurung kurawal {})
    # Format: {"key": "value"}
    mahasiswa = {
        "nama": "masyita",
        "jurusan": "akuntasi",
        "angkatan": 2025
    }
    print(f"dictionary awal: {mahasiswa}")

    # 2. Operasi Mengakses Nilai (Accessing Value)
    # Mengambil nilai berdasarkan kuncinya
    print(f"nama mahasiswa: {mahasiswa['nama']}")

    # 3. Operasi Menambah/Memperbarui Data (Update)
    # Menambah pasangan key-value baru
    mahasiswa["status"] = "aktif"
    # Mengubah nilai yang sudah ada
    mahasiswa["angkatan"] = 2026
    print(f"setelah update dan tambah data: {mahasiswa}")

    # 4. Operasi Menghapus Data (Pop)
    # Menghapus berdasarkan key dan mengambil nilainya
    jurusan_dihapus = mahasiswa.pop("jurusan")
    print(f"data yang dihapus: {jurusan_dihapus}")
    print(f"dictionary setelah pop: {mahasiswa}")

    # 5. Operasi Mengecek Keberadaan Key
    if "nama" in mahasiswa:
        print("key 'nama' tersedia dalam dictionary.")
    
    # 6. Operasi Mengambil Semua Keys, Values, dan Items
    print(f"daftar keys: {list(mahasiswa.keys())}")
    print(f"daftar values: {list(mahasiswa.values())}")

    # 7. Operasi Iterasi (Looping) Dictionary
    print("\nIterasi isi dictionary:")
    for kunci, nilai in mahasiswa.items():
        print(f"- {kunci}: {nilai}")

main()