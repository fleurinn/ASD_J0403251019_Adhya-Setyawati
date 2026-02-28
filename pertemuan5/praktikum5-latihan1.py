# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Latihan 1: Rekursi Pangkat
# ==========================================================
def pangkat(a, n):
 # Base case
    if n == 0:
        return 1
    # Recursive case
    return a * pangkat(a, n - 1)
print(pangkat(2, 4)) # Output: 16

#==============================================================
# Diskusi : alur program serta base case dan recursive call
#==============================================================
'''
1.  base case : kondisi berhenti
    if n == 0: 
        return 1
    penjelasan : ini merupakan batas akhir rekursi agar fungsi tidak memanggil dirinya sendiri terus menerus atau bisa disebut sebagai infinite loop. secara matematis, bilangan apapun yang dipangkatkan 0 hasilnya adalah 1. jadi, ketika pangkat sudah mencapai 0, fungsi berhenti memanggil dirinya dan mengembalikan nilai 1.
2.  recursive case : pemanggilan ulang
    return a * pangkat(a, n-1)
    penjelasan : merupakan langkah di mana fungsi memecah masalah besar menjadi masalah yang lebih kecil. fungsi mengalikan nilai pokok a dengan hasil dari fungsi itu sendiri, tetapi dengan nilai pangkat n yang dikurang 1.
3.  saat baris print(pangkat(2,4)) dijalankan, program akan melakukan dua fase:
    1.  pemanggilan : menumpuk ke bawah
        1. pangkat(2, 4) menunda hasil dan memanggil -> 2 * pangkat(2, 3)
        2. pangkat(2, 3) menunda hasil dan memanggil -> 2 * pangkat(2, 2)
        3. pangkat(2, 2) menunda hasil dan memanggil -> 2 * pangkat(2, 1)
        4. pangkat(2, 1) menunda hasil dan memanggil -> 2 * pangkat(2, 0)
        5. pangkat(2, 0) mencapai base case dan tidak menunda lagi, langsung memunculkan -> 1.
    2. pengembalian : menghitung dari bawah ke atas
        1. pangkat(2, 1) mendapatkan nilai 2 x 1 = 2
        2. pangkat(2, 2) mendapatkan nilai 2 x 2 = 4
        3. pangkat(2, 3) mendapatkan nilai 2 x 4 = 8
        4. pangkat(2, 4) mendapatkan nilai 2 x 8 = 16
    hasil akhir yang dikembalikan ke perintah print adalah 16.
'''