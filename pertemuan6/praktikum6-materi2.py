# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Insertion Sort (Ascending) dengan tracing
# ==========================================================


def insertion_sort (data):
    # loop
    #melihat data awal 
    print("Data awal : ", data)
    print("="*50)
    for i in range (1, len(data)):

        key = data[i] # simpan nilai yang disisipkan
        j = i-1 # index elemen terakhir
        
        print("Iterasi ke- ", i)
        print("Nilai key = ", key)
        print("Bagian kiri (terurut) : ", data[:i])
        print("Bagian kanan (belum terurut) : ", data[i:])

        # geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        # sisipkan key ke posisi yang benar
        data[j+1] = key

        print("Setelah disisipkan : ", data )
        print("-"*50)
    return data

angka = [7,8,5,2,4,6]
print("Hasil sorting: ", insertion_sort(angka))