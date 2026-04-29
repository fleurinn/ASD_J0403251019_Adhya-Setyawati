#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 11
# Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi)
#--------------------------------------------------

# membuat representasi graph menggunakan dictionary (adjacency list)
graph = {
 'Rumah': ['Sekolah', 'Toko'],  # Rumah terhubung ke Sekolah dan Toko
 'Sekolah': ['Perpustakaan'],   # Sekolah terhubung ke Perpustakaan
 'Toko': ['Pasar'],             # Toko terhubung ke Pasar
 'Perpustakaan': [],            # Perpustakaan tidak punya tetangga
 'Pasar': []                    # Pasar tidak punya tetangga
}

# mengimpor deque dari collections untuk digunakan sebagai queue (antrian)
from collections import deque

# fungsi BFS (Breadth First Search)
def bfs(graph, start):
    # set untuk menyimpan node yang sudah dikunjungi
    visited = set()
    # membuat queue dan memasukkan node awal (start)
    queue = deque([start])

    # menandai node awal sebagai sudah dikunjungi
    visited.add(start)

    # selama queue masih ada isinya
    while queue:
        # mengambil node paling depan dari queue (FIFO)
        node = queue.popleft()
        # mencetak node yang sedang dikunjungi
        print(node, end=" ")
        # mengunjungi semua tetangga dari node tersebut
        for neighbor in graph[node]:
            # jika tetangga belum dikunjungi
            if neighbor not in visited:
                # tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                # masukkan ke dalam queue untuk diproses nanti
                queue.append(neighbor)

# menampilkan teks awal
print("BFS dari Rumah:")
# memanggil fungsi BSF mulai dari node 'Rumah'
bfs(graph, 'Rumah')

'''
Pertanyaan Analisis
1. Node mana yang dikunjungi pertama?
Jawab : Node yang dikunjungi pertama adalah node Rumah, karena node tersebut ditetapkan sebagai titik awal (start node) penelusuran sebelum mengunjungi 
        node - node tetangganya. 
2. Mengapa BFS cocok untuk mencari jalur terdekat?
Jawab : karena BFS menelusuri graph secara melebar (level demi level). BFS akan mengunjungi seluruh tetangga terdekat (jarak satu edge), dan seterusnya.
        Oleh karena itu. saat BSF pertama kali menemukan titik tujuan, jalur tersebut dipastikan adalah jalur terpendek (dengan jumlah langkah paling sedikit).
        Berbeda dengan DFS yang menelusuri satu jalur sampai ujung sebelum melakukan backtrack, sehingga DFS bisa saja menemukan jalur yang lebih panjang terlebih
        dahulu.
3. Apa perbedaan urutan BFS jika struktur graph diubah?
Jawab : Jika struktur graph diubah, maka urutan BFS akan berubah secara signifikan. Hal ini karena perubahan struktur akan mengubah siapa saja tetangga/adjacent vertex 
        dari suatu node. Karena BFS bekerja dengan memasukkan tetangga terdekat ke dalam antrean/queue level demi level, maka perubahan koneksi tersebut akan membuat 
        urutan node yang dikunjungi dan dimasukkan ke dalam antrean menjadi berbeda dari graph aslinya.
'''