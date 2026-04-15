# ===========================================
# Nama       :Adhya Setyawati
# NIM        :J0403251019
# Kelas      :TPL B / P1
# ===========================================

# ===========================================
# Latihan 2 : Melengkapi Potongan Kode
# ===========================================
angka = [3,7,4,2,5,10]
print("List sebelum disorting: ",angka)
'''
1. Jawaban no. 1  : Lengkapi kondisi agar menjadi sorting ascending.
'''

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        while j>=0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

print("Hasil Sorting Ascending: ", insertion_sort(angka))
'''
2. Jawaban no. 2 : Ubah agar menjadi descending.
'''
def insertion_sort_descending(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i-1

        while j>=0 and data[j] < key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data

print("Hasil Sorting Descending: ", insertion_sort_descending(angka))