#program untuk mengelompokkan generasi berdasarkan tahun lahir

#mengambil input tahun lahir dari user dan mengubah ke integer
tahun_lahir =int(input("masukkan tahun lahir anda:"))

#logika kontrol alur
if 1928 <= tahun_lahir <= 1945:
    generasi = "silent generation"
    deskripsi = "tumbuh selama depresi besar dan perang dunia II, dikenal pekerja keras, sabar, dan hemat."
elif 1946 <= tahun_lahir <= 1964:
    generasi = "baby boomers"
    deskripsi = "Lahir setelah Perang Dunia II, mengalami lonjakan kelahiran dan fokus pada pencapaian personal."
elif 1965 <= tahun_lahir <= 1980:
    generasi = "generasi X"
    deskripsi = "Dikenal mandiri, tumbuh di masa peralihan teknologi tradisional ke digital."
elif 1981 <= tahun_lahir <= 1996:
    generasi = "generasi Y / milenial"
    deskripsi = "Generasi yang melek teknologi (digital natives) dan peduli isu sosial."
elif 1997 <= tahun_lahir <= 2012:
    generasi = "generasi Z"
    deskripsi = "Tumbuh langsung di dunia internet dan teknologi canggih, sangat terhubung secara digital."
elif 2013 <= tahun_lahir <= 2024:
    generasi = "generasi alpha"
    deskripsi = "Generasi pertama yang sepenuhnya lahir di abad ke-21, sangat dipengaruhi teknologi cerdas."
elif 2025 <= tahun_lahir <= 2039:
    generasi = "generasi beta"
    deskripsi = "Generasi mendatang yang diprediksi akan melanjutkan keterhubungan digital tingkat lanjut."
else:
    generasi = "tidak ada definisi"
    deskripsi = "tahun yang dimassukan tidak dalam daftar generasi ini"

#menampilkan hasil
print(f"hasil pengelompokan:")
print(f"generasi :", generasi)
print(f"deskripsi:", deskripsi)