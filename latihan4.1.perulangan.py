#Perulangan Python Kelipatan Bulan

#meminta input bulan lahir
bulan_lahir = int(input("bulan lahir saya:"))

# Melakukan perulangan menggunakan range dari 1 hingga 100
for i in range(1, 101):
    # Mengecek apakah angka saat ini (i) adalah kelipatan bulan lahir
    # Menggunakan operator modulus (%) untuk mengecek sisa bagi
    if i % bulan_lahir == 0:
        print("bulan")

    else:
        ## Jika bukan kelipatan, cetak angkanya
        print(i)