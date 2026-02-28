# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================
def countdown(n):
    if n == 0:
        print("Selesai")
        return
    print("Masuk:", n)
    countdown(n - 1)
    print("Keluar:", n)
countdown(3)

#==============================================================
# Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
#==============================================================
'''
penjelasan code :
    fungsi countdown(n) akan:
        1. berhenti jika n == 0 (base case).
        2. mencetak "Masuk: n" sebelum memanggil dirinya sendiri.
        3. memanggil countdown(n - 1).
        4. setelah pemanggilan selesai, mencetak "Keluar: n".
penjelasan mengapa output keluar muncul terbalik :
    karena rekursi bekerja menggunakan call stack/tumpukan dengan metode LIFO/Last In, First Out.
fungsi terakhir yang dipanggil akan menjadi yang pertama selesai. countdown(1) selesai lebih dulu,
lalu countdown(2), yang terakhir countdown(3). sehingga urutan keluar menjadi : 1 -> 2 -> 3, yang 
merupakan kebalikan dari urutan masuk.
    karena menggunakan sistem stack/LIFO, proses keluar terjadi secara terbalik dari proses masuk. 
proses masuk dicetak saat fungsi dipanggil (turun), sedangkan proses keluar dicetak saat fungsi selesai (naik).
'''