# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Adhya Setyawati
# NIM     : J0403251019
# Kelas   : TPL / B1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY
nama_file = "buku.txt"
# buat fungsi baca data buku
def baca_data_buku(nama_file):
    database_buku = {}
    # baca data dengan "r"
    with open(nama_file, "r", encoding="utf-8") as file:
        # pisah data dengan ,
        for baris in file:
            baris = baris.strip()
            kode_buku, judul, harga = baris.split(",")
            # simpan data buku ke dalam dictionary dengan key kode_buku
            database_buku[kode_buku] = {
                "judul": judul,
                "harga": int(harga)
            }
    return database_buku

# 2. LINKED LIST - MANAJEMEN STOK / PROMOSI
class Node:
    def __init__(self, judul):
        self.judul = judul   # setiap node menyimpan judul buku
        self.next = None

class LinkedListPromosi:
    def __init__(self):
        self.head = None

    def tambah_buku_promosi(self, judul):
        """Menambahkan judul buku ke daftar promosi"""
        node_baru = Node(judul)

        # jika list kosong
        if self.head is None:
            self.head = node_baru
            return

        # jika list sudah ada isi
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = node_baru

    def tampilkan_promosi(self):
        """Menampilkan semua buku promosi"""
        if self.head is None:
            print("Daftar promosi kosong")
            return

        temp = self.head
        print("Daftar Buku Promosi:")

        while temp:
            print("-", temp.judul)
            temp = temp.next

# 3. QUEUE - ANTREAN PELANGGAN
class AntreanKasir:
    def __init__(self): 
        self.head = None    # node paling depan 
        self.tail = None    # node paling belakang
    # jika head kosong maka :
    def is_empty(self):
        return self.head is None
    # fungsi tambah antrean dengan nama
    def tambah_antrean(self, data):
        node_baru = Node(data)

        # jika queue kosong maka head dan tail menunjuk ke node yang sama  
        if self.is_empty():
            self.head = node_baru
            self.tail = node_baru
            return

        # jika queue tidak kosong maka tail lama menunjuk ke node yang baru
        self.tail.next = node_baru
        self.tail = node_baru

    # menghapus data dari depan
    def layani_pelanggan(self):
        # jika antrean kosong maka menampilkan :
        if self.is_empty():
            print("Antrean kosong!")
            return None
        # mengambil data dari depan
        # 1. ambil data paling depan
        data_terhapus = self.head.data

        # 2. geser ke node berikutnya
        self.head = self.head.next

        # 3. jika setelah geser head menjadi none, maka queue kosong, tail juga harus jadi none
        if self.head is None:
            self.tail = None

        return data_terhapus

    def tampilkan(self): # menmapilkan isi queue dari head ke tail
        current = self.head

        print("Head", end=" -> ")

        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

# class node untuk menyimpan data
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 4. SORTING (Insertion Sort)
def urutkan_transaksi(list_harga):

    for index in range(1, len(list_harga)):
        currentvalue = list_harga[index]
        position = index

        while position > 0 and list_harga[position - 1] > currentvalue:
            list_harga[position] = list_harga[position - 1]
            position = position - 1

        list_harga[position] = currentvalue

    return list_harga

# ==============================================================================
# MAIN PROGRAM
# ==============================================================================
def main():

    nama_file = "buku.txt"
    data_buku = baca_data_buku(nama_file)

    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()

    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku")
        print("2. Kelola Daftar Promosi")
        print("3. Kelola Antrean Kasir")
        print("4. Laporan Penjualan Terurut")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\nKatalog Buku:")
            print(data_buku)

        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            list_promosi.tambah_buku_promosi(judul_baru)
            list_promosi.tampilkan_promosi()

        elif pilihan == '3':
            pil = input("Pilih [tambah/layani] antrean : ")
            if pil == 'tambah':
                nama = input("Nama pelanggan: ")
                antrean_toko.tambah_antrean(nama)
                antrean_toko.tampilkan()
            elif pil == 'layani':
                dilayani = antrean_toko.layani_pelanggan()
                if dilayani:
                    print("Melayani pelanggan:", dilayani)
                antrean_toko.tampilkan()
            else:
                print("Inputan salah, ulangi!")
            

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi)
            hasil = urutkan_transaksi(riwayat_transaksi)
            print("Harga Sesudah Urut:", hasil)

        elif pilihan == '5':
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()