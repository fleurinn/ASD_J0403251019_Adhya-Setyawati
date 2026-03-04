# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Latihan 1 : Memahami Kode Program (Insertion Sort)
# ==========================================================

def insertion_sort(data):
    # loop dimulai dari indeks ke-1 hingga akhir list
    # anggap elemen pertama (indeks 0) sudah terurut
    for i in range(1, len(data)):
        # key adalah elemen yang akan kita sisipkan ke posisi yang benar
        key = data[i]
        # j adalah indeks elemen di sebelah kiri 'key'
        j = i - 1

        # geser elemen yang lebih besar dari 'key' ke arah kanan
        # loop berhenti jika mencapai awal list atau menemukan angka <= key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]  # menggeser elemen ke kanan
            j -= 1      # berpindah ke indeks sebelumnya di kiri
        # letakkan key di posisi yang tepat (di depan elemen yang lebih kecil dari nilai key)
        data[j + 1] = key

    return data

'''
soal:
1. Mengapa perulangan dimulai dari indeks 1?
2. Apa fungsi variabel key?
3. Mengapa digunakan while, bukan for?
4. Operasi apa yang terjadi di dalam while?

jawaban:
1. karena pada algoritma insertion sort, elemen pertama (indeks 0) dianggap sudah terurut. oleh karena itu, perulangan dimulai dari indeks 1 untuk membandingkan dan menyisipkan elemen berikutnya ke dalam bagian list yang sudah terurut di sebelah kiri.
2. variabel key berfungsi untuk menyimpan nilai elemen yang sedang diproses dan akan disisipkan ke posisi yang benar pada bagian list yang sudah terurut.
3. karena jumlah pergeseran elemen tidak diketahui secara pasti. pergeseran bergantung pada kondisi apakah elemen di sebelah kiri lebih besar dari key. perulangan akan terus berjalan selama kondisi j >= 0 and data[j] > key terpenuhi, sehingga lebih tepat menggunakan while yang berbasis kondisi.
4. di dalam while terjadi operasi pergeseran elemen ke kanan dengan perintah :
    data[j + 1] = data[j]
    dan pengurangan indeks dengan:
    j -= 1
    operasi ini dilakukan untuk memberi ruang agar key dapat ditempatkan pada posisi yang sesuai. 
'''