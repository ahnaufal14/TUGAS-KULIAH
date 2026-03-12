#input dari user
nama_buku = input("masukkan nama buku: ")
harga_buku = int(input("masukkan harga buku: "))
jumlah_buku = int(input("masukkan jumlah buku: "))

#menghitung total harga
total_harga = harga_buku * jumlah_buku

#menampilkan data
print("nama buku :", nama_buku)
print("harga buku :", harga_buku)
print("jumlah buku: ", jumlah_buku)
print("total buku :", total_harga)