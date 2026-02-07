# ==============================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan 1: Load data dari file ke Dictionary
# ==============================================================

nama_file = "data_mahasiswa.txt"

#membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    """
    Membaca data mahasiswa dari file.
    Format per baris: NIM,NAMA,NILAI
    Output:
    - data_dict (dictionary)
    key = NIM
    value = {"nama": NAMA, "nilai": NILAI(int)}
    """
    data_dict ={} #inialisasi data dictionary

    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #hilangkan karakter baris baru (\n)

            # Lewati baris kosong
            if baris == "":
                continue

            parts = baris.split(",")
            if len(parts) !=3:
                continue

            nim, nama, nilai_str = parts

            try:
                nilai_int = int(nilai_str)
            except ValueError:
                continue

            data_dict[nim]={"nama": nama, "nilai": nilai_int}
            nim, nama, nilai = baris.split(",") # pecah menjadi data satuan

            # simpan data mahasiswa ke directory dengan key, value
            data_dict[nim]={
                "nama": nama,
                "nilai": int(nilai)
            }
    return data_dict

# memanggil fungsi baca_data_mahasiswa
# buka_data = baca_data_mahasiswa(nama_file)
# print("Jumlah Data Terbaca: ", len(buka_data))

# ==========================================================
# Latihan 2: Tampilkan semua data mahasiswa
# ==========================================================

def tampilkan_data(data_dict):
    """
    Menampilkan semua data mahasiswa dalam format tabel.
    """
    if len(data_dict) == 0:
        print("Data Kosong!")
        return
    '''
        untuk tampilan yang rapi, atur f-string formatting :
            {'NIM' : <10} artinya : tampilkan NIM <= rata kiri dengan lebar 10 karakter
            {'Nama' : <12} artinya : tampilkan nama rata kiri, dengan lebar kolom 12 karakter
            {'Nilai' : 5} artinya : tampilkan nama rata kiri, dengan lebar kolom 12 karakter
    '''
    # membuat Header Tabel
    print("=== Daftar Mahasiswa ===")
    # membuat header tabel
    print(f"{'NIM':<10}|{'Nama':<12}| {'Nilai':>5}")
    print("-" * 32)

    for nim in sorted(data_dict.keys()):
        nama=data_dict[nim]["nama"]
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:<10}| {nama:<12}| {nilai:>5}")

# memanggil fungsi menampilkan data
# tampilkan_data(buka_data)

# ==========================================================
# Latihan 3: Cari data mahasiswa berdasarkan NIM
# ==========================================================

def cari_data(data_dict):
    nim_cari = input("Masukkan NIM yang ingin dicari:". strip())

    if nim_cari in data_dict:
        nama = data_dict [nim_cari]["nama"]
        nilai = data_dict [nim_cari]["nilai"]

        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai    : {nilai}")
    else:
        print("Data tidak ditemukan!")
# cari_data(buka_data)

# ==========================================================
# Latihan 4: Update nilai mahasiswa (ubah nilai)
# ==========================================================

def update_nilai(data_dict):
    # cari nim mahasiswa yang akan diupdate nilainya
    nim = input("Masukkan NIM mahasiswa yang ingin diperbaharui nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Pembaharuan dibatalkan!")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Pembaharuan dibatalkan!")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Pembaharuan dibatalkan!")

    nilai_lama = data_dict[nim]["nilai"]
    # memasukkan nilai update baru ke dictionary
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Pembaharuan Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

# update_nilai(buka_data)

# ==========================================================
# Latihan 5: Simpan perubahan data mahasiswa ke file (WRITE)
# ==========================================================

def simpan_data(nama_file, data_dict):
    with open (nama_file,"w", encoding ="utf-8")as file:
        for nim in sorted(data_dict.keys()):
            nama= data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

# simpan_data(nama_file, buka_data)
# print("Data berhasil disimpan!")

# ==========================================================
# Praktikum 1: ADT & File Handling (Studi Kasus: Data Mahasiswa)
# Latihan Final: Menu Interaktif
# ==========================================================

def main():

    # menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n=== MENU DATA MAHASISWA ===")
        print("1. Tampilkan Semua Data") #fs no 2
        print("2. Update Data Mahasiswa") #fs no 3
        print("3. Update Nilai Mahasiswa") #fs no 4
        print("4. Simpan Nilai ke Data") #fs no 5
        print("0. Keluar") #fs no 6

        pilihan = input("Pilihan menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)
        elif pilihan == "2":
            cari_data(buka_data)
        elif pilihan == "3":
            update_nilai(buka_data)
        elif pilihan == "4":
            simpan_data(nama_file,buka_data)
            print("Data berhasil disimpan")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
    
