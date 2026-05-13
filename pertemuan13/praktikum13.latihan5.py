#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
# Praktikum 13 - Graph III: Spanning Tree
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 13
# Latihan 1: Algoritma Kruskal
#--------------------------------------------------

# Daftar edge graph jaringan komputer: (bobot, node1, node2)
edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()
# mst digunakan untuk menyimpan hasil Minimum Spanning Tree
mst = []
# total_weight digunakan untuk menghitung total bobot MST
total_weight = 0
# connected digunakan untuk menyimpan node yang sudah terhubung
connected = set()

# melakukan perulangan untuk setiap edge pada graph
for weight, u, v in edges:
    # memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:
        # menambahkan edge ke hasil MST
        mst.append((u, v, weight))
        # menambahkan bobot edge ke total bobot MST
        total_weight += weight
        # menambahkan node u ke set connected
        connected.add(u)
        # menambahkan node v ke set connected
        connected.add(v)

# menampilkan hasil Minimum Spanning Tree
print("Minimum Spanning Tree Jaringan Komputer:")
# melakukan perulangan untuk mencetak edge MST
for edge in mst:
    # mencetak setiap edge yang dipilih
    print(edge)
# menampilkan total bobot minimum
print("Total bobot minimum =", total_weight)

# Jawaban Analisis:
# 1. Kasus apa yang dipilih?
# 2. Algoritma apa yang digunakan?
# 3. Edge mana saja yang dipilih dalam MST?
# 4. Berapa total bobot MST?
# 5. Mengapa edge tertentu tidak dipilih?

'''
jawaban:
1.  kasus yang dipilih adalah jaringan komputer.
    pada kasus ini setiap router saling terhubung dengan biaya
    atau bobot yang berbeda-beda sehingga perlu dicari jalur
    koneksi paling efisien menggunakan minimum spanning tree.
2.  algoritma yang digunakan adalah kruskal.
    algoritma kruskal bekerja dengan cara mengurutkan semua edge
    dari bobot paling kecil ke paling besar, kemudian memilih edge
    satu per satu selama edge tersebut tidak membentuk cycle.
    cara ini membuat total bobot jaringan menjadi minimum.
3.  edge yang dipilih adalah:
    (routerc, routerd) dengan bobot 1
    (routera, routerc) dengan bobot 2
    (routera, routerb) dengan bobot 3
    edge-edge tersebut dipilih karena mampu menghubungkan semua
    router dengan total bobot paling kecil tanpa membentuk cycle.
4.  total bobot mst adalah 6.
    hasil tersebut diperoleh dari penjumlahan:
    1 + 2 + 3 = 6.
    total ini menjadi biaya minimum untuk menghubungkan semua router.
5.  karena edge tersebut memiliki bobot lebih besar dan dapat
    membentuk cycle pada graph.
    contohnya edge (routerb, routerc) dengan bobot 4 tidak dipilih
    karena router b dan router c sudah terhubung melalui jalur lain.
    begitu juga edge (routerb, routerd) dengan bobot 5 tidak dipilih
    karena sudah ada jalur dengan bobot lebih kecil yang menghubungkan
    semua router.
'''