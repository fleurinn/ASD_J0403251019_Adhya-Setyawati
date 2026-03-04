# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Latihan 5 :  Melengkapi Fungsi Merge
# ==========================================================

'''
1. Lengkapi kondisi agar menjadi ascending.
'''
# jawaban
def merge(left, right):
    result = []
    i = 0
    j = 0 

    # membandingkan elemen kiri dan kanan selama keduanya masih memiliki nilai
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:                 # mengambil nilai yang lebih kecil (ascending)
            result.append(left[i])              # masukkan ke result
            i += 1                              # geser pointer ke arah kiri
        else:
            result.append(right[j])             # masukkan ke result 
            j += 1                              # geser pointer ke arah kanan

    # jika masih ada sisa elemen di kiri, tambahkan semua
    result.extend(left[i:])

    # jika masih ada sisa elemen di kanan, tambahkan semua
    result.extend(right[j:])

    return result 

# program utama
left = [8, 14, 5]           # list kiri (belum terurut)
right = [1, 7, 10, 45, 15]  # list kanan (belum terurut)
hasil = merge(left, right)  
print("Hasil Sorting: ", hasil) # tampilkan hasil


"""
2. Jelaskan fungsi result.extend()!
jawaban : result.extend() digunakan untuk menambahkan seluruh elemen yang tersisa dari list kiri atau kanan ke dalam list hasil setelah proses perbandingan selesai.
"""