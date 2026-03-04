# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Insertion Sort (Ascending)
# ==========================================================

def insertion_sort (data):
    # loop
    for i in range (1, len(data)):

        key = data[i] # simpan nilai yang disisipkan
        j = i-1 # index elemen terakhir
        
        # geser
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        # sisipkan data ke posisi yang benar
        data[j+1] = key
    return data

angka = [7,8,5,2,4,6]
print("Hasil sorting: ", insertion_sort(angka))
