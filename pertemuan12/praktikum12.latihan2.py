#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 12
# Latihan 2. Mencoba Algoritma Dijkstra
#--------------------------------------------------

import heapq  # mengimpor modul heapq untuk menggunakan priority queue

# Weighted graph dengan bobot positif  # mendefinisikan graph berbobot positif
graph = {  # membuat struktur graph dalam bentuk dictionary
    'A': {'B': 4, 'C': 2},  # node A terhubung ke B (4) dan C (2)
    'B': {'D': 5},          # node B terhubung ke D (5)
    'C': {'D': 1},          # node C terhubung ke D (1)
    'D': {}                 # node D tidak memiliki tetangga
}

def dijkstra(graph, start):  # mendefinisikan fungsi Dijkstra untuk mencari jarak terpendek
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Dijkstra.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}  # menginisialisasi semua jarak dengan tak hingga
    
    # Jarak dari start ke start adalah 0
    distances[start] = 0  # menetapkan jarak node awal menjadi 0
    
    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]  # membuat antrian prioritas dengan node awal

    while priority_queue:  # melakukan perulangan selama antrian tidak kosong
        current_distance, current_node = heapq.heappop(priority_queue)  # mengambil node dengan jarak terkecil
        
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat,
        # maka proses dilewati
        if current_distance > distances[current_node]:  # mengecek apakah jarak sudah tidak optimal
            continue  # melewati iterasi jika kondisi terpenuhi
        
        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():  # mengiterasi semua tetangga node
            distance = current_distance + weight  # menghitung jarak baru ke tetangga
            
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya
            if distance < distances[neighbor]:  # mengecek apakah jarak baru lebih kecil
                distances[neighbor] = distance  # memperbarui jarak terpendek
                heapq.heappush(priority_queue, (distance, neighbor))  # memasukkan ke antrian prioritas
    
    return distances  # mengembalikan hasil jarak terpendek dari node awal

hasil = dijkstra(graph, 'A')  # menjalankan fungsi Dijkstra dengan node awal 'A'
print("Jarak terpendek dari node A:")  # menampilkan judul output hasil

for node, distance in hasil.items():  # mengiterasi hasil jarak setiap node
    print(node, "=", distance)  # menampilkan node dan jaraknya

# Jawaban Analisis:
# 1. Berapa jarak terpendek dari A ke B?
# 2. Berapa jarak terpendek dari A ke C?
# 3. Berapa jarak terpendek dari A ke D?
# 4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
# 5. Apa fungsi priority_queue dalam algoritma Dijkstra?
# 6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?

'''
Jawaban

1.  jarak terpendekt dari A ke B adalah 4, karena terdapat edge langsung dari node A ke B dengan bobot 4, 
    dan tidak ada jalur lain yang mempunyai jarak lebih kecil dari nilai tersebut.
2.  jarak terpendek dar A ke C adalah 2, ini diperolah dari edge langsung antara node A ke C dengan bobot 2, 
    yang merupakan satu satunya jalur menuju C dan juga merupakan nilai minimum.
3.  jarak terpendek dari A ke D adalah 3, denga jalur yang dipilih adalah A -> C -> D, dengan total bobot 2 + 1 = 3.
    jalur lain yaitu A -> B -> D dengan total bobot 9 tidak dippilih karena total bobot yang dimiliki lebih besar dari total
    bobot dari jalur A -> C -> D.
4.  jarak dari A ke D melalui C lebih kecil karema total bobot yang dilalui lebih rendah. jalur A -> C -> D memiliki bobot 2 + 1 = 3,
    sedangkan jalur A -> B -> D memiliki bobot 4 + 5 = 9. Karena algoritma Djikstra selalu memilih jalur dengan total bobot yang
    paling kecil, sehingga jalur melalui C adalah pilihan yang tepat.
5.  priority queue berfungsi untuk memilih node dengan jarak terkecil secara efisien pada setiap langkah agoritma.
    dengan menggunakan struktur ini, algoritma dapat selaly memproses node yang memiliki jarak paling minimun terlebih dahulu,
    sehingga proses pencarian jalur terpendek menjadi lebih cepat dan terstruktur.
6.  algoritma Djikstra tidak cocok untuk graph dengan bobot negatif karena dapat menghasilkan perhitungan jarak yang tidak akurat,
    hal ini dikarenakan Djikstra mengasumsikan bahwa sekali node diproses dengan jarak terkecil, maka jarak tersebut sudah final. namun,
    jika terdapat bobot negatif, bisa saja ditemukan jalur yang lebih pendek setelahnya, sehingga hasil akhir menjadi salah.
'''