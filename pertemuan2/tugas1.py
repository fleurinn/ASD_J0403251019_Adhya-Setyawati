# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama :Adhya Setyawati
# NIM :J0403251019
# Kelas :TPL B / P1
# ==========================================================

# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "stokBarang.txt"

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):
    stok_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #hilangkan karakter baris baru (\n)

            # Lewati baris kosong
            if baris == "":
                continue

            parts = baris.split(",")
            if len(parts) !=3:
                continue

            kode, nama, stok_str = parts

            try:
                stok_int = int(stok_str)
            except ValueError:
                continue

            # simpan data barang ke directory dengan key, value
            stok_dict[kode]={
                "nama": nama,
                "stok": int(stok_int)
            }
    return stok_dict

# data = baca_stok(nama_file)
# print(data)

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    with open (nama_file,"w", encoding ="utf-8")as file:
        for kode in sorted(stok_dict.keys()):
            nama= stok_dict[kode]["nama"]
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------

def tampilkan_data(stok_dict):
    # menampilkan semua data barang dalam bentuk tabel.
    if len(stok_dict) == 0:
        print("Data Kosong!")
        return
    '''
        untuk tampilan yang rapi, atur f-string formatting :
            {'Kode' : <15} artinya : tampilkan kode <= rata kiri dengan lebar 15 karakter
            {'Nama' : <20} artinya : tampilkan nama rata kiri, dengan lebar kolom 20 karakter
            {'Stok' : >5} artinya : tampilkan stok rata kiri, dengan lebar kolom 5 karakter
    '''
    # membuat Header Tabel
    print("=== Daftar Stok Barang ===")
    # membuat header tabel
    print(f"{'Kode':<15}|{'Nama':<20}| {'Stok':>3}")
    print("-" * 38)

    for kode in sorted(stok_dict.keys()):
        nama=stok_dict[kode]["nama"]
        stok=stok_dict[kode]["stok"]

        # jika stok 0, ganti dengan pesan
        if stok == 0:
            stok_tampil = "Stok Kosong!"
        else:
            stok_tampil = stok
        
        print(f"{kode:<15}| {nama:<20}| {stok_tampil:>3}")

# ------------------------------------
# Fungsi: Cari barang berdasarkan kode
# ------------------------------------

def cari_barang(stok_dict):
    kode_cari = input("Masukkan barang yang ingin dicari:").strip()

    if kode_cari in stok_dict:
        nama = stok_dict [kode_cari]["nama"]
        stok = stok_dict [kode_cari]["stok"]

        print("\n=== Data Barang Ditemukan ===")
        print(f"Kode: {kode_cari}")
        print(f"Nama: {nama}")
        print(f"Stok Barang: {stok}")
    else:
        print("Barang tidak ditemukan!")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict):
    """
    Menambah barang baru ke stok_dict.
    """

    kode = input("Masukkan kode barang baru: ").strip()

    # Validasi: kode tidak boleh duplikat
    if kode in stok_dict:
        print("Kode sudah digunakan!")
        return

    nama = input("Masukkan nama barang: ").strip()

    # Input stok awal (harus integer)
    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus berupa angka!")
        return

    # Simpan ke dictionary
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan!")

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict):
    # Mengubah stok barang (ditambah atau dikurangi).
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    # cek apakah ada di distionary
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan!")
        return
    
    print("Pilih jenis update: ")
    print("1. Tambah stok barang")
    print("2. Kurangi stok barang")
    pilihan = input("Masukkan pilihan anda (1/2): ").strip()

    # input jumlah perubahan stok
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return
    
    stok_sekarang = stok_dict[kode]["stok"]

    # prosesnya:
    if pilihan == "1":
        stok_baru = stok_sekarang + jumlah

    elif pilihan == "2":
        stok_baru = stok_sekarang - jumlah

        # dicek stoknya, apakah stok tersebut negatif? (stok tidak boleh negatif)
        if stok_baru <0:
            print("Error: Stok tidak boleh negatif!")
            return
        
    else:
        print("Pilihan tidak valid")
        return
    
    # Simpan stok baru
    stok_dict[kode]["stok"] = stok_baru
    print("Stok berhasil diperbarui!")

# -------------------------------
# Program Utama
# -------------------------------
def main():
 # Membaca data dari file saat program mulai
    stok_barang = baca_stok(nama_file)
    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilihan = input("Pilih menu: ").strip()
        
        if pilihan == "1":
            tampilkan_data(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
# Menjalankan program utama
if __name__ == "__main__":
    main()