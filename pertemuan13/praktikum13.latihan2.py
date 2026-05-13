#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
# Praktikum 13 - Graph III: Spanning Tree
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 13
# Latihan 1: Implementasi Algoritma Kruskal
#--------------------------------------------------

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()
# mst digunakan untuk menyimpan hasil Minimum Spanning Tree
mst = []
# total_weight digunakan untuk menghitung total bobot MST
total_weight = 0
# connected digunakan untuk menyimpan node yang sudah terhubung
connected = set()

# melakukan perulangan untuk setiap edge
for weight, u, v in edges:
    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        # menambahkan edge ke hasil MST
        mst.append((u, v, weight))
        # menambahkan bobot edge ke total bobot MST
        total_weight += weight
        # menambahkan node u ke set connected
        connected.add(u)
        # menambahkan node v ke set connected
        connected.add(v)

# menampilkan tulisan Minimum Spanning Tree
print("Minimum Spanning Tree:")
# melakukan perulangan untuk mencetak edge MST
for edge in mst:
    # mencetak setiap edge MST
    print(edge)
# menampilkan total bobot MST
print("Total bobot =", total_weight)

# Jawaban Analisis:
# 1. Edge mana yang dipilih pertama kali?
# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
# 3. Berapa total bobot MST yang dihasilkan?
# 4. Mengapa edge tertentu tidak dipilih?

'''
jawaban :
1.  edge pertama yang dipilih adalah ('c', 'd') dengan bobot 1
    karena memiliki bobot paling kecil setelah diurutkan.
2.  karena algoritma minimum spanning tree bekerja dengan memilih
    edge berbobot paling kecil agar total bobot graph menjadi minimum.
3.  total bobot mst yang dihasilkan adalah 6
    dari edge (c,d)=1, (a,c)=2, dan (b,d)=3.
4.  karena edge tersebut dapat membentuk cycle atau memiliki bobot
    lebih besar sehingga tidak diperlukan dalam mst.
'''