#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 11
# Materi 2: Implementasi BFS (FIFO)
#--------------------------------------------------

# struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque

# representasi graph
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
}

def bfs(graph, start):
    # fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimpan struktur dari graph
    # start : node awal penelusuran

    # Queue digunakan untuk menyimpan node yang akan diprose/dibaca
    queue = deque()
    
    # variabel yang digunakan untuk menyimpan node yang sudah diproses/dikunjungi
    visited = set()

    # masukkan node awal ke queue
    queue.append(start)

    # tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start)

    while queue:
        # mengambil node paling depan dari queue
        node = queue.popleft()
        
        # tampilkan node yang sedang dikunjungi 
        print(node, end=" ")

        # periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            # jika tetangga belum dikunjungi
            if neighbor not in visited:
                # sudah dibaca, pindahkan dari queue ke visited, tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

# menjalankan BFS dari node A
bfs(graph, 'A')
