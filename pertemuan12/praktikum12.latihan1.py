#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 12
# Latihan 1: Memahami Weighted Graph dan Shortest Path Sederhana
#--------------------------------------------------

# Representasi weighted graph menggunakan dictionary bersarang  # mendefinisikan graph berbobot dalam bentuk dictionary
graph = {  # membuat struktur graph
    'A': {'B': 4, 'C': 2},  # node A terhubung ke B (4) dan C (2)
    'B': {'D': 5},          # node B terhubung ke D (5)
    'C': {'D': 1},          # node C terhubung ke D (1)
    'D': {}                 # node D tidak memiliki tetangga
}

# Menghitung dua kemungkinan jalur dari A ke D  # menghitung total jarak dari dua rute berbeda
jalur_1 = graph['A']['B'] + graph['B']['D']  # menghitung jarak jalur A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # menghitung jarak jalur A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1)  # menampilkan hasil jarak jalur pertama
print("Jalur 2: A -> C -> D =", jalur_2)  # menampilkan hasil jarak jalur kedua

if jalur_1 < jalur_2:  # membandingkan apakah jalur 1 lebih pendek dari jalur 2
    print("Jalur terpendek adalah A -> B -> D")  # menampilkan jalur terpendek jika kondisi benar
else:  # kondisi jika jalur 2 lebih pendek atau sama
    print("Jalur terpendek adalah A -> C -> D")  # menampilkan jalur terpendek alternatif


# Jawaban Analisis:
# 1. Berapa total bobot jalur A -> B -> D?
# 2. Berapa total bobot jalur A -> C -> D?
# 3. Jalur mana yang dipilih sebagai jalur terpendek?
# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

'''
Jawaban : 
1.  total bobot dari jalur A -> B -> D adalah Jalur 1: A -> B -> D = 9
2.  total bobot dari jalur A -> C -> D adalah Jalur 2: A -> C -> D = 3
3.  jalur yang dipilih sebagai jalur terpendek adalah jalur 2 (Jalur 2: A -> C -> D = 3), 
    karena total bobot dari jalur ke 2 adalah 3, sedangkan jalur 1 total bobotnya adalah 9 
    (Jalur 1: A -> B -> D = 9).
4.  jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit
    karena setiap edge memiliki bobot yang berbeda. jalur dengan jumlah edge lebih
    sedikit belum tentu memiliki total bobot yang lebih kecil. oleh karena itu, yang menentukan
    jalur terpendek adalah total akumulasi dari setiap bobot di edge, bukan jumlah edge.
'''
