#================================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
#================================================================

#================================================================
# Tugas Hands-On : Sistem Antrian Bengkel Motor
#================================================================

class Node: 
    def __init__(self, no, nama, servis): 
        self.no = no            # simpan nomor antrian
        self.nama = nama        # simpan nama pelanggan
        self.servis = servis    # simpan jenis servis
        self.next = None        # penunjuk ke pelanggan berikutnya (awalnya kosong)

# class untuk mengatur jalannya antrian
class QueueBengkel:
    def __init__(self):
        self.front = None   # penunjuk ke orang paling depan
        self.rear = None    # penunjuk ke orang paling belakang
    
    # cek apakah antrian kosong
    def is_empty(self):
        return self.front is None
    
    # fungsi tambah pelanggan baru
    def enqueue (self, no, nama, servis):
        nodeBaru = Node(no, nama, servis)
        
        # jika antrian sepi/kosong
        if self.is_empty():
            self.front = nodeBaru   # dia jadi yang pertama
            self.rear = nodeBaru    # sekaligus jadi yang terakhir
            print(f"Berhasil menambahkan pelanggan {no}. {nama} ke antrian.")
            return
    
        self.rear.next = nodeBaru   # kalau ada antrian, sambung di belakang orang terakhir
        self.rear = nodeBaru        # update status orang paling belakang
        print(f"Berhasil menambahkan pelanggan {no}. {nama} ke antrian.")
        
    # fungsi panggil atau layani pemlanggan
    def dequeue(self):
        # kl ga ada yang antri
        if self.is_empty():
            print("Antrian Kosong. Tidak ada pelanggan yang bisa dilayani.")
            return None
        
        # simpan data orang terdepan agar tidak hilang dan geser antrian (org pertama resmi keluar)
        pelangganDilayani = self.front
        self.front = self.front.next

        # tampilkan informasi pelanggan yang telah dilayani
        print(f"Selesai melayani pelanggan no {pelangganDilayani.no}. "
            f"{pelangganDilayani.nama} | Jenis servis: {pelangganDilayani.servis}")

        # jika setelah digeser antrian menjadi kosong
        if self.front is None:
            self.rear = None    # rear juga di set none

        # mengembalikan data pelanggan yang dilayani (opsional)
        return pelangganDilayani
    
    # fungsi menampilkan data antrian
    def tampilkan(self):
        # jika antrian kosong
        if self.is_empty():
            print("Antrian masih kosong.")
            return

        # tampilkan header table
        print("\n=== Daftar Antrian Pelanggan Bengkel ===")
        print(f"{'No':<10} | {'Nama':<20} | {'Servis':<15}")

        # mulai traversal dari node paling depan
        current = self.front
        
        # selama masih ada node
        while current is not None:
            # cetak data pelanggan
            print(f"{current.no:<10} | {current.nama:<20} | {current.servis:<15}")            # pindah ke node berikutnya
            current = current.next
        print("=============================")
            
def main():
    # membuat objek queuebengkel
    q = QueueBengkel()
        
    # loop utama program
    while True:
        # menampilkan menu utama
        print("\n==== Sistem Antrian Bengkel ====")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        # input pilihan user  
        pilih = input("Pilih menu : ")

        # Jika memilih menu 1 : tambah pelanggan (input no antrian, nama pelanggan dan jenis servisnya)   
        if pilih == "1":
            no = input("Masukkan no antrian : ")
            nama = input("Masukkan nama pelanggan : ")
            servis = input("Jenis servis : ")
            q.enqueue(no, nama, servis)     # panggil method enqueue
        
        # jika memilih menu 2 : layani pelanggan
        elif pilih == "2":
            q.dequeue()

        # jika memilih menu 3 : menampilkan data antrian           
        elif pilih == "3":
            q.tampilkan()
            
        # jika memilih menu 4 : keluar dari main menu
        elif pilih == "4":
            print("Terimakasih telah menggunakan sistem antrian bengkel.")
            print("=====================================================")
            break

        # jika input tidak valid  
        else:
            print("Pilihan tidak valid. Coba sekali lagi.")

# menampilkan fungsi main hanya jika file dijalankan langsung 
if __name__ == "__main__":
    main()