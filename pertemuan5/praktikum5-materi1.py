# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Materi Rekursif : Faktorial
# recursif case => 3! = 3 x 2 x 1
# base case => 0 berhenti
# ==========================================================

def faktorial(n):
    # base case
    if n == 0:
        return 1
    # recursive case
    return n*faktorial(n-1)    # untuk menggantikan n-1*n-2*x   n-3...... n? dengan dirinya sendiri dan dikurang 1
print("=== PROGRAM FAKTORIAL ===")
print("Hasil Faktorial : ", faktorial(3))