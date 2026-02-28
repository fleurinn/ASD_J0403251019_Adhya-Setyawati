# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================
def kombinasi(n, hasil=""):
    if len(hasil) == n:
        print(hasil)
        return
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")
kombinasi(2)

#=================================================================
# Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan
#=================================================================
'''
1.  jumlah kondisi yang dihasilkan :
        - rumus: jumlah jumlah total kombinasi yang dihasilkan adalah 2^n.
        - pada setiap pemanggilan rekursi, program memiliki 2 pilihan, yaitu menambahkan huruf "A" atau menambahkan huruf "B".
        karena proses ini diulang sebanyak n kali, maka total kombinasinya adalah 2x2x...x2.
        - untuk n = 2: jumlah kombinasinya adalah 2 pangkat 2 = 4 kombinasi ("AA", "AB", "BA", "BB").
2.  pola choose dan explore (backtracking)
        program ini menggunakan pendekatan pohon keputusan (decision tree) bercabang dua.
            - choose : di setiap langkah, fungsi memutuskan untuk menempelkan "A" ke variabel hasil, lalu di baris berikutnya memilih menempelkan "B".
            - explore : setelah memilih satu huruf (misalnya "A"), fungsi memanggil dirinya sendiri (kombinasi(n, hasil + "A")) untuk terus menggali cabang tersebut sampai mencapai panjang maksimal (base case).
            - backtrack : ketika panjang hasil sudah mencapai n (kondisi len(hasil) == n), program mencetak string tersebut lalu melakukan return. 
                          Perintah return inilah yang membuat program "mundur" ke persimpangan sebelumnya untuk mencoba pilihan huruf yang lain (yaitu cabang "B").
3.  alur eksekusi untuk kombinasi(2) :
    1. mulai dari "" (kosong).
    2. pilih "A" -> hasil = "A"
        - pilih "A" lagi -> hasil = "AA" (mencapai batas n=2, Cetak "AA", mundur).
        - pilih "B" -> hasil = "AB" (mencapai batas n=2, Cetak "AB", mundur).
    3. mundur ke awal ""
    4. pilih "B" -> hasil = "B"
        - pilih "A" lagi -> hasil = "BA" (mencapai batas n=2, Cetak "BA", mundur).
        - pilih "B" -> hasil = "BB" (mencapai batas n=2, Cetak "BB", mundur).
'''