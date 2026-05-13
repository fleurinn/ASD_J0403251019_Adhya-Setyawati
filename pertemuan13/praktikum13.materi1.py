#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
# Praktikum 13 - Graph III: Spanning Tree
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 13
# Materi 1: Algoritma Kruskal
#--------------------------------------------------

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot
edges.sort()

# mst digunakan untuk menyimpan hasil Minimum Spanning Tree
mst = []

# total_weight digunakan untuk menghitung total bobot MST
total_weight = 0

# Set sederhana untuk node yang sudah dipilih
connected = set()

# melakukan perulangan untuk setiap edge pada graph
for weight, u, v in edges:

    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # menambahkan edge ke hasil Minimum Spanning Tree
        mst.append((u, v, weight))

        # menambahkan bobot edge ke total bobot MST
        total_weight += weight

        # menambahkan node u ke set connected
        connected.add(u)

        # menambahkan node v ke set connected
        connected.add(v)

# menampilkan tulisan Minimum Spanning Tree
print("Minimum Spanning Tree:")

# melakukan perulangan untuk mencetak setiap edge MST
for edge in mst:

    # mencetak edge hasil Minimum Spanning Tree
    print(edge)

# mencetak total bobot Minimum Spanning Tree
print("Total bobot =", total_weight)