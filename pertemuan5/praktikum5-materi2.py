# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# masuk 3-2-1
# keluar 1-2-3 
# ==========================================================

def hitung(n):
    # base case 
    if n == 0:
        print("Selesai.")
        return
    
    print("Masuk: ", n)
    hitung(n-1) # recursive case
    print("Keluar.", n)

print ("--- Program Tracing ---")
hitung (100)