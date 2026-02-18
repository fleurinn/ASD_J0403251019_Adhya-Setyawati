# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Implementasi Dasar : Queue
# ==========================================================
class Node:
    def __init__(self, data): # konstruktor 
        self.data = data # tujuan: menyimpan nilai atau data
        self.next = None # pointer ke note berikutnya

# Queue dengan 2 pointer : front dan rear/head dan tail
class QueueLL:
    def __init__(self):
        self.front = None # node paling depan
        self.rear = None # node paling belakang

    def is_empty(self):
        # Mengembalikan True jika front adalah None (queue kosong)
        return self.front is None
    
    def enqueue(self, data):
        # menambah data di belakang (rear)
        nodeBaru = Node(data)
    
        # jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        # jika queue tidak kosong:
        # rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        # rear pindah ke node baru
        self.rear = nodeBaru

    def dequeue(self):
        # menghapus data dari depan 


        # 1. pilih/lihat data yang paling depan 
        data_terhapus = self.front.data

        # 2. geser front ke node berikutnya
        self.front = self.front.next

        # 3. jika setelah geser front menjadi none, maka queue kosong
        # rear juga harus jadi none 
        if self.front is None:
            self.rear = None 
        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front -> ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("Node - Rear di node terakhir")

# Instantiasi objek class QueueLL

q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan( )
