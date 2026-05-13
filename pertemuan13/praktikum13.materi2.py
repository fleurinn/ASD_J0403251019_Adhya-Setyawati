#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
# Praktikum 13 - Graph III: Spanning Tree
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 13
# Materi 2: Algoritma Prim
#--------------------------------------------------

import heapq  # menggunakan library heapq untuk priority queue pada algoritma Prim

# graph berbentuk adjacency list dengan bobot setiap edge
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# fungsi prim untuk mencari Minimum Spanning Tree
def prim(graph, start):

    # visited digunakan untuk menyimpan node yang sudah dikunjungi algoritma Prim
    visited = set([start])

    # edges digunakan sebagai priority queue untuk menyimpan edge
    edges = []

    # melakukan perulangan pada semua tetangga node awal
    for neighbor, weight in graph[start].items():

        # memasukkan edge ke priority queue berdasarkan bobot terkecil algoritma Prim
        heapq.heappush(edges, (weight, start, neighbor))

    # mst digunakan untuk menyimpan hasil Minimum Spanning Tree
    mst = []

    # total_weight digunakan untuk menghitung total bobot MST
    total_weight = 0

    # selama masih ada edge di priority queue maka algoritma Prim berjalan
    while edges:

        # mengambil edge dengan bobot paling kecil dari priority queue
        weight, u, v = heapq.heappop(edges)

        # jika node tujuan belum dikunjungi
        if v not in visited:

            # menambahkan node ke visited algoritma Prim
            visited.add(v)

            # menambahkan edge ke hasil MST
            mst.append((u, v, weight))

            # menambahkan bobot edge ke total bobot MST
            total_weight += weight

            # melakukan perulangan ke semua tetangga node v
            for neighbor, w in graph[v].items():

                # jika tetangga belum dikunjungi
                if neighbor not in visited:

                    # memasukkan edge baru ke priority queue algoritma Prim
                    heapq.heappush(edges, (w, v, neighbor))

    # mengembalikan hasil MST dan total bobot
    return mst, total_weight

# menjalankan fungsi prim dengan node awal A
mst, total = prim(graph, 'A')

# menampilkan tulisan Minimum Spanning Tree
print("Minimum Spanning Tree:")

# melakukan perulangan untuk mencetak setiap edge MST
for edge in mst:

    # mencetak edge hasil algoritma Prim
    print(edge)

# mencetak total bobot Minimum Spanning Tree
print("Total bobot =", total)