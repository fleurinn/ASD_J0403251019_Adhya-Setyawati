# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================
def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil + angka)
buat_pin(3)

# ==============================================================================
# Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang?
# ==============================================================================
'''
    program generator pin di atas menggunakan teknik backtracking dengan pola choose dan explore untuk menghasilkan seluruh kemungkinan pin sepanjang tiga digit dari angka 0 sampai 2.
fungsi buat_pin menerima parameter panjang dan variabel hasil yang berfungsi menyimpan digit yang sudah dipilih sementara. base case terjadi ketika panjang string hasil sudah sama 
dengan nilai panjang yang ditentukan. pada kondisi tersebut, program akan mencetak pin dan menghentikan proses rekursi pada cabang itu.

    jika belum mencapai panjang yang ditentukan, program masuk ke recursive case, yaitu melakukan perulangan terhadap setiap angka dalam daftar ["0", "1", "2"].
pada setiap iterasi, fungsi memanggil dirinya sendiri dengan menambahkan satu digit ke dalam hasil. karena setiap posisi memiliki tiga tiga pilihan angka dan 
terdapat tiga posisi, maka total kombinasi yang dihasilkan adalah 3³ atau 27 kemungkinan. oleh karena itu akan muncul pin seperti 000, 001, 002 hingga 222.

    untuk mencegah angka yang sama muncul berulang dalam satu pin, perlu ditambahkan kondisi agar angka yang akan dipilih belum ada di dalam variabel hasil. 
caranya adalah dengan menambahkan pengecekan seperti berikut:
for angka in ["0", "1", "2"]:
    if angka not in hasil:
        buat_pin(panjang, hasil + angka)

    dengan kondisi tersebut, setiap digit hanya dapat digunakan satu kali dalam satu kombinasi pin. akibatnya jumlah kemungkinan tidak lagi 3³, 
melainkan menjadi 3! atau 6 kombinasi, yaitu 012, 021, 102, 120, 201, dan 210.
'''
