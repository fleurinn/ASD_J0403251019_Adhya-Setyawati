def selection_sort(daftar_angka):
    total_elemen = len(daftar_angka)

    for indeks_awal in range(total_elemen - 1):
        indeks_minimum = indeks_awal

        for indeks_pencarian in range(indeks_awal + 1, total_elemen):
            if daftar_angka[indeks_pencarian] < daftar_angka[indeks_minimum]:
                indeks_minimum = indeks_pencarian


        sementara = daftar_angka[indeks_awal]
        daftar_angka[indeks_awal] = daftar_angka[indeks_minimum]
        daftar_angka[indeks_minimum] = sementara

data= [20, 12, 10, 15, 2]
print("Data Acak : ", data)

selection_sort(data)
print("Output list menggunakan selection sort : ", data)