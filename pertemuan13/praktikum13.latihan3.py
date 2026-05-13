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

import heapq  # menggunakan library heapq untuk priority queue algoritma Prim

# graph berbentuk adjacency list beserta bobot edge
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# fungsi prim untuk mencari Minimum Spanning Tree
def prim(graph, start):

    # visited digunakan untuk menyimpan node yang sudah dikunjungi
    visited = set([start])
    # edges digunakan sebagai priority queue
    edges = []

    # memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # mst digunakan untuk menyimpan hasil MST
    mst = []
    # total_weight digunakan untuk menghitung total bobot MST
    total_weight = 0

    # selama masih ada edge di priority queue
    while edges:
        # mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)
        # jika node tujuan belum dikunjungi
        if v not in visited:
            # menambahkan node ke visited
            visited.add(v)
            # menambahkan edge ke MST
            mst.append((u, v, weight))
            # menambahkan bobot edge ke total MST
            total_weight += weight
            # melakukan perulangan pada tetangga node v
            for neighbor, w in graph[v].items():
                # jika tetangga belum dikunjungi
                if neighbor not in visited:
                    # memasukkan edge baru ke priority queue
                    heapq.heappush(edges, (w, v, neighbor))
    # mengembalikan hasil MST dan total bobot
    return mst, total_weight

# menjalankan algoritma Prim dengan node awal A
mst, total = prim(graph, 'A')
# menampilkan tulisan Minimum Spanning Tree
print("Minimum Spanning Tree:")

# melakukan perulangan untuk mencetak edge MST
for edge in mst:
    # mencetak setiap edge MST
    print(edge)

# menampilkan total bobot MST
print("Total bobot =", total)

# Jawaban Analisis:
# 1. Node awal apa yang digunakan?
# 2. Edge mana yang dipilih pertama kali?
# 3. Bagaimana Prim menentukan edge berikutnya?
# 4. Berapa total bobot MST yang dihasilkan?
# 5. Apa perbedaan pendekatan Prim dan Kruskal?

'''
jawaban:
1.  node awal yang digunakan adalah node a
    karena fungsi prim dipanggil dengan parameter 'A'.
2.  edge pertama yang dipilih adalah (a, c) dengan bobot 2
    karena memiliki bobot paling kecil dari node awal a.
3.  prim memilih edge dengan bobot terkecil yang terhubung
    ke node yang sudah dikunjungi dan tidak membentuk cycle.
4.  total bobot mst yang dihasilkan adalah 6
    dari edge (a,c)=2, (c,d)=1, dan (d,b)=3.
5.  prim membangun mst mulai dari satu node lalu memperluas graph,
    sedangkan kruskal memilih edge dengan bobot terkecil secara global
    tanpa memperhatikan node awal.
'''