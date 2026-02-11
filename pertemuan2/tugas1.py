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
nama_file = "stokBarang.txt" # nama file penyimpanan data stok

# -------------------------------
# Fungsi: Membaca data dari file
# -------------------------------
def baca_stok(nama_file):   # fungsi untuk membaca data stok dari file
    stok_dict = {} # dictionary untuk menyimpan data stok

    # buka file stokBarang.txt, dengan read r
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file: # looping membaca baca setiap baris dalam file
            baris = baris.strip() # hilangkan karakter baris baru (\n)

            if baris == "":     # cek apakah baris kosong
                continue        # melewati baris kosong

            parts = baris.split(",") # pisah data berdasarkan koma
            if len(parts) !=3: #jika format tidak sesuai, lewati
                continue    # melewati baris yang formatnya salah

            kode, nama, stok_str = parts # mengambil kode, nama, dan stok

            try:    # mencoba mengubah stok ke integer
                stok_int = int(stok_str) # mengubah stok menjadi integer
            except ValueError: # jika gagal mengubah
                continue # jika gagal, lewati baris

            # simpan data barang ke directory dengan key & value
            stok_dict[kode]={
                "nama": nama,   # menyimpan nama barang
                "stok": int(stok_int)   # menyimpan stok barang
            }
    return stok_dict # mengembalikan dictionary stok

# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------
def simpan_stok(nama_file, stok_dict):  # fungsi untuk menyimpan data stok ke file
    """
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    """
    # buka file dengan mode write w
    with open (nama_file,"w", encoding ="utf-8")as file:
        for kode in sorted(stok_dict.keys()): # menulis data secara terurut
            nama= stok_dict[kode]["nama"]   # mengambil nama barang
            stok = stok_dict[kode]["stok"]  # mengambil srok barang
            file.write(f"{kode},{nama},{stok}\n") # tulis ke file

# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------

def tampilkan_data(stok_dict): # fungsi untuk menampilkan data stok
    # menampilkan semua data barang dalam bentuk tabel.
    if len(stok_dict) == 0: # mengecek apakah data kosong
        print("Data Kosong!")   # menampilkan pesan data kosong
        return  # menghentikan fungsi
    '''
        untuk tampilan yang rapi, atur f-string formatting :
            {'Kode' : <15} artinya : tampilkan kode <= rata kiri dengan lebar 15 karakter
            {'Nama' : <20} artinya : tampilkan nama rata kiri, dengan lebar kolom 20 karakter
            {'Stok' : >10} artinya : tampilkan stok rata kiri, dengan lebar kolom 10 karakter
    '''
    # membuat Header Tabel
    print("=== Daftar Stok Barang ===")
    print(f"{'Kode':<15}|{'Nama':<20}| {'Stok':>5}")    # menampilkan header tabel
    print("-" * 45) # menampilkan garis pemisah tabel

    for kode in sorted(stok_dict.keys()):   # looping data berdasarkan kode
        nama=stok_dict[kode]["nama"]    # mengambil nama barang
        stok=stok_dict[kode]["stok"]    # mengambil stok barang

        # jika stok 0, ganti dengan pesan "kosong"
        if stok == 0:
            stok_tampil = "Kosong"  # mengganti tampilan stok menjadi tulisan
        else:
            stok_tampil = stok # jika stok tidak 0, menampilkan stok asli
        
        print(f"{kode:<15}| {nama:<20}| {stok_tampil:>5}")  # menampilkan data per baris

# ------------------------------------
# Fungsi: Cari barang berdasarkan kode
# ------------------------------------

def cari_barang(stok_dict): # fungsi untuk mencari barang
    kode_cari = input("Masukkan barang yang ingin dicari:").strip() # input kode barang

    # jika kode ditemukan, maka: 
    if kode_cari in stok_dict:
        nama = stok_dict [kode_cari]["nama"]    # ambil nama barang
        stok = stok_dict [kode_cari]["stok"]    # ambil stok barang

        # menampilkan kode, nama, dan stok barang yang dicari
        print("\n=== Data Barang Ditemukan ===")
        print(f"Kode: {kode_cari}")
        print(f"Nama: {nama}")
        print(f"Stok Barang: {stok}")
    else:   #kl tidak ada maka menampilkan pesan berikut: 
        print("Barang tidak ditemukan!")

# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------
def tambah_barang(stok_dict): # fungsi untuk menambah barang
    """
    Menambah barang baru ke stok_dict.
    """

    kode = input("Masukkan kode barang baru: ").strip() # input kode barang

    # validasi kode tidak boleh duplikat
    if kode in stok_dict:
        print("Kode sudah digunakan!") # menampilkan pesan error
        return #lalu memnghentikan fungsi

    nama = input("Masukkan nama barang: ").strip()  #input nama barang

    # input stok awal (harus integer), jika input bukan angka maka akan menampilkan pesan error dan langsung menghentikan fungsi menggunakan return
    try:
        stok_awal = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus berupa angka!")
        return

    # simpan data ke dictionary
    stok_dict[kode] = {
        "nama": nama,
        "stok": stok_awal
    }

    print("Barang berhasil ditambahkan!")   #   menampilkan pesan suksues

# -------------------------------
# Fungsi: Update stok barang
# -------------------------------
def update_stok(stok_dict): # fungsi untuk mengubah stok barang

    # Mengubah stok barang (ditambah atau dikurangi).
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()  # input kode barang

    # cek apakah ada di distionary, kalau ga ada akan menampilkan pesan berikut
    if kode not in stok_dict:
        print("Kode barang tidak ditemukan!")
        return
    
    # menampilkan pilihan update (opsi tambah dan kurangi stok)
    print("Pilih jenis update: ")
    print("1. Tambah stok barang")
    print("2. Kurangi stok barang")
    pilihan = input("Masukkan pilihan anda (1/2): ").strip() # input pilihan user

    # input jumlah perubahan stok, jika bukan angka maka akan menampilkan pesan error
    try:
        jumlah = int(input("Masukkan jumlah: "))
    except ValueError:
        print("Jumlah harus berupa angka!")
        return
    
    # mengambil stok saat ini 
    stok_sekarang = stok_dict[kode]["stok"]

    # prosesnya:
    # jika memilih angka satu, maka akan menambah jumlah stok yang ada
    if pilihan == "1": 
        stok_baru = stok_sekarang + jumlah

    # jika memilih angka dua, maka akan mengurangi jumlah stok yang ada
    elif pilihan == "2":
        stok_baru = stok_sekarang - jumlah

        # dicek stoknya, apakah stok tersebut negatif? (stok tidak boleh negatif, kl negatif akan memunculkan pesan error)
        if stok_baru <0:
            print("Error: Stok tidak boleh negatif!")
            return
        
    # inputan selain angka maka dianggap tidak valid 
    else:
        print("Pilihan tidak valid")
        return
    
    # Simpan stok baru dan menampilkan pesan sukses
    stok_dict[kode]["stok"] = stok_baru
    print("Stok berhasil diperbarui!")

# -------------------------------
# Program Utama
# -------------------------------
def main(): # fungsi utama program
    stok_barang = baca_stok(nama_file)   # Membaca data dari file saat program mulai
    while True: # looping menu utama
        print("\n=== MENU STOK KANTIN ===") # menampilkan judul menu
        print("1. Tampilkan semua barang")  # menu tampilkan data
        print("2. Cari barang berdasarkan kode")    # menu cari barang
        print("3. Tambah barang baru") # menu tambah barang
        print("4. Update stok barang")  # menu update stok
        print("5. Simpan ke file")  # menu simpan data
        print("0. Keluar")  # menu keluar
        
        pilihan = input("Pilih menu: ").strip() # input pilihan menu
        
        # fitur dari inputan yang dipilih user, jika tidak valid maka akan menampilkan pesan error dan user diharuskan untuk memilih kembali menunya
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

if __name__ == "__main__":  # cek apakah file dijalankan langsung
    main()  # menjalankan fungsi utama