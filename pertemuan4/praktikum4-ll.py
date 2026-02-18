# ==========================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
# ==========================================================

# ==========================================================
# Implementasi Dasar : Node pada Linked List
# ==========================================================

# instantiasi adalah 
# class x
class Node:
    def __init__(self, data): # konstruktor 
        self.data = data # tujuan: menyimpan nilai atau data
        self.next = None # pointer ke note berikutnya

# proses pertama, dimana kita membuat node satu persatu, dengan cara memanggil konstruktor atau fungsi dalam kelas node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal :menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)    # menampilkan data pada node saat ini
    current = current.next # pindah ke node berikutnya 

# ==========================================================
# Implementasi Dasar : Linked List + Insert Awal
# ==========================================================

class LinkedList: # class implementasi stack
    def __init__(self):
        self.head = None # awalnya kosong

    def insert_awal(self,data): # push dalam stack
        # 1. buat node baru
        nodeBaru = Node(data) # panggil class node

        # 2. node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # 3. head pindah ke node baru
        self.head = nodeBaru
    def hapus_awal(self): # fungsi pop dalam stack
        data_terhapus = self.head.data # data yang akan dihapus/peek dalam stack = peek(melihat data yang paling depan/head tanpa menghapusnya terlebih dahulu)
        # menggeser head ke node berikutnya 
        self.head = self.head.next
        print("Node yang dihapus: ", data_terhapus)


    def tampilkan(self):    # implementasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

print("=== LIST BARU ===")
ll = LinkedList() # instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()