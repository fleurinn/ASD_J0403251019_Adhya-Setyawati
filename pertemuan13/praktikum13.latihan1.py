#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
# Praktikum 13 - Graph III: Spanning Tree
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 13
# Latihan 1: Memahami Konsep Spanning Tree
#--------------------------------------------------

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# menampilkan tulisan edge pada graph
print("Edge pada graph:")
# melakukan perulangan untuk mencetak semua edge pada graph
for edge in edges:
    # mencetak setiap edge graph
    print(edge)

# menampilkan tulisan spanning tree
print("\nSpanning Tree:")
# melakukan perulangan untuk mencetak semua edge spanning tree
for edge in spanning_tree:
    # mencetak setiap edge spanning tree
    print(edge)

# menampilkan jumlah edge pada graph awal
print("\nJumlah edge graph =", len(edges))
# menampilkan jumlah edge pada spanning tree
print("Jumlah edge spanning tree =", len(spanning_tree))

# Jawaban Analisis:
# 1. Apa perbedaan graph awal dan spanning tree?
# 2. Mengapa spanning tree tidak boleh memiliki cycle?
# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

'''
Jawaban :
1.  graph awal memiliki semua edge yang tersedia pada graph,
    sedangkan spanning tree hanya mengambil beberapa edge penting
    untuk menghubungkan semua node tanpa membentuk cycle.
2.  karena tujuan spanning tree adalah menghubungkan semua node
    dengan jalur paling sederhana. jika ada cycle, maka ada jalur
    yang berputar dan edge menjadi tidak efisien atau berlebihan.
3.  karena spanning tree hanya mengambil edge minimum yang diperlukan
    untuk menghubungkan semua node. pada graph dengan n node,
    spanning tree selalu memiliki n-1 edge sehingga jumlah edge
    lebih sedikit dibanding graph awal.
'''