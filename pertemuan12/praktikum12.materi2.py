#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 12
# Materi 1: Algoritma Bellman Ford
#--------------------------------------------------

# Representasi graph berbobot  # mendefinisikan graph dalam bentuk dictionary
graph = {
    'A': {'B': 4, 'C': 2},  # A ke B (4), A ke C (2)
    'B': {'D': 5},          # B ke D (5)
    'C': {'D': 1},          # C ke D (1)
    'D': {}                 # D tidak punya tetangga
}

def bellman_ford(graph, start):  # mendefinisikan fungsi Bellman-Ford untuk mencari jarak terpendek
    distances = {node: float('inf') for node in graph}  # membuat dictionary jarak awal semua node = tak hingga
    distances[start] = 0  # menetapkan jarak node awal menjadi 0
    
    # proses update jarak agar mendapatkan nilai terpendek
    for _ in range(len(graph) - 1):  # melakukan iterasi sebanyak jumlah node - 1
        for node in graph:  # mengiterasi setiap node dalam graph
            for neighbor, weight in graph[node].items():  # mengiterasi setiap tetangga dan bobotnya
                if distances[node] + weight < distances[neighbor]:  # mengecek apakah ditemukan jarak lebih pendek
                    distances[neighbor] = distances[node] + weight  # memperbarui jarak jika lebih kecil
    
    return distances  # mengembalikan hasil jarak terpendek dari node awal  

start_node = 'A'  # menentukan node awal

hasil = bellman_ford(graph, start_node)  # menjalankan fungsi Bellman-Ford

print("Jarak terpendek dari A:")  # menampilkan judul output
for node, jarak in hasil.items():  # mengiterasi hasil
    print(f"A -> {node} = {jarak}")  # menampilkan hasil jarak