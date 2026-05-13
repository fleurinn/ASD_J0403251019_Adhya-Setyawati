#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
# Praktikum 13 - Graph III: Spanning Tree
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 13
# Latihan 1: Implementasi Algoritma Prim
#--------------------------------------------------

# Daftar edge graph: (bobot, gedung1, gedung2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()
# mst digunakan untuk menyimpan hasil Minimum Spanning Tree
mst = []
# total_biaya digunakan untuk menghitung total biaya minimum
total_biaya = 0
# connected digunakan untuk menyimpan node yang sudah terhubung
connected = set()

# melakukan perulangan untuk setiap edge
for weight, u, v in edges:
    # memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        # menambahkan edge ke MST
        mst.append((u, v, weight))
        # menambahkan bobot edge ke total biaya
        total_biaya += weight
        # menambahkan node u ke set connected
        connected.add(u)
        # menambahkan node v ke set connected
        connected.add(v)

# menampilkan hasil Minimum Spanning Tree
print("Jaringan Kabel Minimum:")

# melakukan perulangan untuk mencetak edge yang dipilih
for edge in mst:
    # mencetak setiap edge MST
    print(edge)

# menampilkan total biaya minimum
print("Total biaya minimum =", total_biaya)

# Jawaban Analisis:
# 1. Algoritma apa yang digunakan?
# 2. Edge mana saja yang dipilih?
# 3. Berapa total biaya minimum?
# 4. Mengapa MST cocok digunakan pada kasus ini?

'''
jawaban:
1.  algoritma yang digunakan adalah kruskal
    karena edge diurutkan berdasarkan bobot terkecil.
2.  edge yang dipilih adalah:
    (gedungc, gedungd) = 1
    (gedunga, gedungc) = 2
    (gedungb, gedungd) = 3
3.  total biaya minimum yang dihasilkan adalah 6.
4.  karena mst dapat menghubungkan semua gedung
    dengan biaya kabel minimum tanpa membuat jalur berputar.
'''