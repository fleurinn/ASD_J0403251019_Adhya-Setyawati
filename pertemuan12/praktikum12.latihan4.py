#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 12
# Latihan 4. Studi Kasus Contoh: Jalur Terpendek Antar Lokasi Kampus
#--------------------------------------------------

import heapq  # mengimpor modul heapq untuk menggunakan priority queue

# Graph lokasi kampus  # mendefinisikan graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit  # menjelaskan bahwa bobot adalah waktu tempuh
graph = {  # membuat struktur graph dalam bentuk dictionary
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},  # dari Gerbang ke Perpustakaan (6 menit) dan Kantin (2 menit)
    'Perpustakaan': {'Lab': 3},  # dari Perpustakaan ke Lab (3 menit)
    'Kantin': {'Lab': 4, 'Aula': 7},  # dari Kantin ke Lab (4 menit) dan Aula (7 menit)
    'Lab': {'Aula': 1},  # dari Lab ke Aula (1 menit)
    'Aula': {}  # Aula tidak memiliki tetangga
}

def dijkstra(graph, start):  # mendefinisikan fungsi Dijkstra untuk mencari jarak terpendek
    distances = {node: float('inf') for node in graph}  # menginisialisasi semua jarak dengan tak hingga
    distances[start] = 0  # menetapkan jarak node awal menjadi 0
    priority_queue = [(0, start)]  # membuat antrian prioritas dengan node awal
    
    while priority_queue:  # melakukan perulangan selama antrian tidak kosong
        current_distance, current_node = heapq.heappop(priority_queue)  # mengambil node dengan jarak terkecil
        
        if current_distance > distances[current_node]:  # mengecek apakah jarak saat ini tidak optimal
            continue  # melewati iterasi jika kondisi terpenuhi
        
        for neighbor, weight in graph[current_node].items():  # mengiterasi semua tetangga node
            distance = current_distance + weight  # menghitung jarak baru ke tetangga
            
            if distance < distances[neighbor]:  # mengecek apakah jarak baru lebih kecil
                distances[neighbor] = distance  # memperbarui jarak terpendek
                heapq.heappush(priority_queue, (distance, neighbor))  # memasukkan ke antrian prioritas
    
    return distances  # mengembalikan hasil jarak terpendek dari node awal

hasil = dijkstra(graph, 'Gerbang')  # menjalankan fungsi Dijkstra dengan node awal 'Gerbang'
print("Jarak terpendek dari Gerbang Kampus:")  # menampilkan judul output

for lokasi, jarak in hasil.items():  # mengiterasi hasil jarak setiap lokasi
    print(lokasi, "=", jarak, "menit")  # menampilkan lokasi dan waktu tempuh


# Jawaban Analisis:
# 1. Lokasi mana yang paling dekat dari Gerbang?
# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

'''
1.  lokasi paling dekat dari gerbang adalah kantin dengan waktu tempuh 2 menit, 
    karena merupakan nilai bobot terkecil dibandingkan lokasi lainnya.
2.  waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit melalui jalur 
    Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7).
3.  tidak selalu, karena jalur langsung bisa saja memiliki bobot lebih besar dibandingkan jalur tidak langsung.
    dalam kasus ini, jalur langsung dari Kantin ke Aula adalah 7, tetapi bisa saja jalur lain lebih kecil jika melalui node lain dengan
    total bobot lebih rendah.
4.  karena semua bobot bernilai positif (waktu tempuh tidak mungkin negatif), 
    sehingga djikstra dapat bekerja secara optimal untuk mencari jalur tercepat antar lokasi.
'''
