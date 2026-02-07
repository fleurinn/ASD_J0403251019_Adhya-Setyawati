# ============================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1A : Membaca seluruh isi file
# ============================================

# Membuka file dengan mode read ("r")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #Membaca keseluruhan isi file dalam satu string
print(isi_file)

# ============================================
# Bagian A: Baca File dengan read()
# ============================================

print("===Hasil Read===")
print("Tipe Data: ", type(isi_file))
print("Jumlah Karakter: ", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)

# ============================================
# Bagian B: Baca file per baris
# ============================================

print("Membaca file perbaris")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris+1
        baris=baris.strip() #Menghilangkan karakter newline dan spasi di awal/akhir, tujuannya untuk mengambil data murni/bersih tanpa ada tambahan karakter
        print("Baris ke-", jumlah_baris)
        print("Isinya : ", baris)


# =================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 2: Parsing baris menjadi kolom data
# =================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai )

# ===================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 3: Membaca File dan Menyimpan ke List
# ===================================================

data_list = []

with open("data_mahasiswa.txt", "r", encoding="utf=8") as file:
    for baris in file:
        baris = baris.strip()
        
        nim, nama, nilai = baris.split(",")
        # simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)])

print("=== Data Mahasiswa dalam List ===")
print(data_list)

print("=== Jumlah Record dalam List ===")
print("Jumlah Record: ", len(data_list))

print("=== Menampilkan Data Record Tertentu ===")
print("Contoh Record Pertama: ", data_list[0])

# =================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 4: Membaca File dan Menyimpan ke Directoy
# =================================================

data_dict ={}
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris. strip()
        nim, nama, nilai = baris.split(",")

        # simpan data mahasiswa ke directory dengan key NIM
        data_dict[nim]={
            "nama": nama,
            "nilai": int(nilai)
        }

print("=== Data Mahasiswa dalam Directory ===")
print(data_dict)