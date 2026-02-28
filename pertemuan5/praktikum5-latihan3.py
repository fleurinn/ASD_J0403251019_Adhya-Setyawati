# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================
def cari_maks(data, index=0):
    # Base case
    if index == len(data) - 1:
        return data[index]
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)
    if data[index] > maks_sisa:
        return data[index]
    else:
        return maks_sisa
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))

#==============================================================
# Diskusi : alur program serta base case dan recursive call
#==============================================================
'''
fungsi bekerja dengan cara:
    1. membandikan elemen saat ini (data[index])
    2. dengan nilai maksimum dari sis elemen setelahnya
    3. dilakukan terus sampai mencapai elemen terkahir
    - base case :
        if index == len(data) - 1:
            return data[index]
        base case terjadi ketika index sudah berada di elemen terakhir. yang artinya, tidak ada lagi elemen untuk dibandingkan, maka langsung kembalikan nilai tersebut.
    - recursive call :
        maks_sisa = cari_maks(data, index + 1)
        fungsi memanggil dirinya sendiri untuk mencari maksimum dari elemen berikutnya, lalu dibandingkan dengan elemen saat ini.
    - urutan eksekusi pada [3,7,2,9,5]
        tahap turun (menuju base case):
            cari_maks(0) → bandingkan 3 dengan maks_sisa
            cari_maks(1) → bandingkan 7 dengan maks_sisa
            cari_maks(2) → bandingkan 2 dengan maks_sisa
            cari_maks(3) → bandingkan 9 dengan maks_sisa
            cari_maks(4) → base case → return 5
        tahap naik (perbandingan nilai)
            index 3 → max(9,5) = 9
            index 2 → max(2,9) = 9
            index 1 → max(7,9) = 9
            index 0 → max(3,9) = 9
    - output akhir :
        Nilai maksimum: 9    
'''