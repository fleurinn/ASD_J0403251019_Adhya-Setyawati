#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 12
# Materi 1: Algoritma Dijkstra
#--------------------------------------------------

import heapq  # mengimpor modul heapq untuk membuat priority queue (antrian prioritas)

graph = {  # membuat representasi graph dalam bentuk dictionary (adjacency list)
    'A': {'B': 4, 'C': 2},  # node A terhubung ke B (jarak 4) dan C (jarak 2)
    'B': {'D': 5},          # node B terhubung ke D (jarak 5)
    'C': {'D': 1},          # node C terhubung ke D (jarak 1)
    'D': {}                 # node D tidak punya tetangga
}

def dijkstra(graph, start):  # fungsi untuk mencari jarak terpendek dari node awal
    # menyimpan jarak minimum
    distances = {node: float('inf') for node in graph}  # inisialisasi semua jarak = tak hingga
    
    # jarak node awal = 0
    distances[start] = 0  # set jarak node awal menjadi 0
    
    # priority queue
    pq = [(0, start)]  # membuat antrian prioritas berisi (jarak, node awal)
    
    while pq:  # loop selama antrian tidak kosong
        current_distance, current_node = heapq.heappop(pq)  # ambil node dengan jarak terkecil
        
        # periksa semua tetangga
        for neighbor, weight in graph[current_node].items():  # iterasi semua tetangga dari node sekarang
            distance = current_distance + weight  # hitung jarak baru ke tetangga
            
            # jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:  # bandingkan dengan jarak sebelumnya
                distances[neighbor] = distance  # update jarak terpendek
                heapq.heappush(pq, (distance, neighbor))  # masukkan ke antrian prioritas
    
    return distances  # mengembalikan hasil semua jarak terpendek dari node awal


hasil = dijkstra(graph, 'A')  # menjalankan fungsi Dijkstra dengan node awal 'A'
print(hasil)  # menampilkan hasil jarak terpendek ke semua node