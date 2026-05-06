#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 12
# Latihan 5. Studi Kasus dengan Program Shortest Path 
#--------------------------------------------------

import heapq  # mengimpor modul heapq untuk menggunakan priority queue

# Representasi graph berbobot menggunakan dictionary  # mendefinisikan graph kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},   # dari Bogor ke Jakarta (5) dan Depok (2)
    'Depok': {'Jakarta': 2, 'Bandung': 6}, # dari Depok ke Jakarta (2) dan Bandung (6)
    'Jakarta': {'Bandung': 7},             # dari Jakarta ke Bandung (7)
    'Bandung': {}                          # Bandung tidak memiliki tetangga
}

def dijkstra(graph, start):  # mendefinisikan fungsi Dijkstra untuk mencari jarak terpendek
    distances = {node: float('inf') for node in graph}  # inisialisasi semua jarak = tak hingga
    distances[start] = 0  # jarak dari node awal ke dirinya sendiri = 0
    
    priority_queue = [(0, start)]  # membuat antrian prioritas (jarak, node)
    
    while priority_queue:  # loop selama antrian tidak kosong
        current_distance, current_node = heapq.heappop(priority_queue)  # ambil node dengan jarak terkecil
        
        if current_distance > distances[current_node]:  # jika jarak tidak optimal
            continue  # lewati
        
        for neighbor, weight in graph[current_node].items():  # cek semua tetangga
            distance = current_distance + weight  # hitung jarak baru
            
            if distance < distances[neighbor]:  # jika lebih kecil
                distances[neighbor] = distance  # update jarak
                heapq.heappush(priority_queue, (distance, neighbor))  # masukkan ke antrian
    
    return distances  # mengembalikan hasil jarak terpendek

# Menentukan node awal
start_node = 'Bogor'  # menetapkan node awal adalah Bogor

hasil = dijkstra(graph, start_node)  # menjalankan fungsi Dijkstra

print("Jarak terpendek dari Bogor:")  # menampilkan judul output

# Menampilkan hasil sesuai format
for kota, jarak in hasil.items():  # iterasi setiap kota
    print(f"Bogor -> {kota} = {jarak}")  # menampilkan jarak dari Bogor ke setiap kota


# Jawaban Analisis:
# 1. Node awal yang digunakan apa?
# 2. Node mana yang memiliki jarak paling kecil dari node awal?
# 3. Node mana yang memiliki jarak paling besar dari node awal?
# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
'''
Jawaban
1.  node awal yang digunakan adalah Bogor, karena perhitungan jarak dimulai dari kota Bogor ke kota lainnya.
2.  node yang memiliki jarak paling kecil selain Bogor adalah Depok dengan jarak 2,
    karena merupakan nilai bobot paling kecil dari hasil perhitungan.
3.  node yang memiliki jarak paling besar adalah Bandung dengan jarak 8,
    karena merupakan hasil akumulasi bobot terbesar dari jalur terpendek yang ditemukan.
4.  algoritma Dijkstra bekerja dengan memilih node dengan jarak paling kecil terlebih dahulu,
    kemudian memperbarui jarak ke node tetangganya jika ditemukan jalur yang lebih pendek.
    proses ini dilakukan berulang hingga semua node memiliki jarak terpendek dari node awal.
'''