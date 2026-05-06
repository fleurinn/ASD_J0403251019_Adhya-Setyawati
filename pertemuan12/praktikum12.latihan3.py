#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 12
# Latihan 3. Mencoba Algoritma Bellman Ford
#--------------------------------------------------

# Weighted graph dengan bobot negatif  # mendefinisikan graph berbobot negatif
graph = {  # membuat struktur graph dalam bentuk dictionary
    'A': {'B': 5, 'C': 4},  # node A terhubung ke B (5) dan C (4)
    'B': {},                # node B tidak memiliki tetangga
    'C': {'B': -2}          # node C terhubung ke B dengan bobot -2
}

def bellman_ford(graph, start):  # mendefinisikan fungsi Bellman-Ford untuk mencari jarak terpendek
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """
    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}  # menginisialisasi semua jarak dengan tak hingga
    
    # Jarak dari start ke start adalah 0
    distances[start] = 0  # menetapkan jarak node awal menjadi 0
    
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):  # melakukan perulangan sebanyak jumlah node - 1
        
        # Periksa semua edge
        for node in graph:  # mengiterasi setiap node dalam graph
            for neighbor, weight in graph[node].items():  # mengiterasi setiap tetangga dan bobotnya
                
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:  # mengecek apakah ada jarak yang lebih pendek
                    distances[neighbor] = distances[node] + weight  # memperbarui jarak terpendek
    
    return distances  # mengembalikan hasil jarak terpendek dari node awal

hasil = bellman_ford(graph, 'A')  # menjalankan fungsi Bellman-Ford dengan node awal 'A'
print("Jarak terpendek dari node A:")  # menampilkan judul output hasil

for node, distance in hasil.items():  # mengiterasi hasil jarak setiap node
    print(node, "=", distance)  # menampilkan node dan jaraknya


# Jawaban Analisis:
# 1. Berapa bobot langsung dari A ke B?
# 2. Berapa total bobot jalur A -> C -> B?
# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
# 5. Apa yang dimaksud dengan proses relaksasi edge?
# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?

'''
Jawaban
1.  bobot langsung dari A ke B adalah 5, hal ini dikarenakan terdapat
    edge langsung dari node A ke node B dengan nilai bobot sebesar 5 tanpa
    melalui node lain.
2.  total bobot dari jalur A -> C -> B adalah 2, cara perhitungannya adalah 
    dari A ke C memiliki edge dengan nilai bobot sebesar 4, kemudian dari C ke B 
    memiliki edge dengan nilai bobot -2, sehingga totalnya adalah 4 + (-2) = 2.
3.  jalur yang menghasilkan jarak lebih kecil menuju B adalah jalur A -> C -> B, 
    karena total bobotnya adalah 2, sedangkan jalur langsung A-> B memiliki bobot 5.
    karena 2 lebih kecil dari 5, maka jalur melalui C menjadi jalur terpendek.
4.  algoritma Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena 
    algoritma ini tidak langsung menganggap jarak suatu node sudah final. Bellman-Ford
    melakukan pengecekan berulang terhadap semua edge sehingga tetap dapat menemukan jalur terpendek
    meskipun terdapat bobot negatif, selama tidak ada negative cycle.
5.  proses relaksasi edge adalah proses memperbarui jarak suatu node jika ditemukan jalur yang
    lebih pendek melalui node lain. dalam proses ini, algoritma membandingkan jarak lama dengan jarak baru hasil
    penjumlahan bobot edge, lalu memilih nilai yang lebih kecil sebagai jarak terbaru.
6.  perbedaan utama antara Bellman-Ford dengan Djikstra terletak pada kemampuan menangani bobot negatif. 
    Bellman-Ford dapat menangani graph dengan bobot negatif dan mendeteksi negative cycle, sedangkan Djikstra hanya dapat digunakan 
    pada graph dengan bobot positif karena mengasumsikan bahwa jarak yang sudah dipilih tidak akan berubah lagi.
'''