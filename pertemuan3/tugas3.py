# =============================================================================
# Pertemuan 3: Linked List
# Latihan 1: Implementasikan fungsi untuk menghapus node dengan nilai tertentu.
# =============================================================================
# Implementasi fungsi untuk menghapus node dengan nilai tertentu. 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def delete_node(self, key):
        temp = self.head
    
    #Jika head adalah node yang ingin dihapus
        if temp and temp.data == key:
            self.head = temp.next   #Head pindah ke elemen kedua
            temp= None              #Menghapus referensi lama
            return
    
    #Cari node yang mau dihapus dan simpan node sebelumnya
        prev = None
        while temp and temp.data != key :
            prev = temp      #Simpan node sekarang sebagai "sebelumnya"
            temp = temp.next  #Maju ke node berikutnya
    
    #Jika data tidak ditemukan sampai akhir list
        if temp is None:
            return    #fungsi langsung berhenti 
    
    #Lepaskan node dari list dengan menghubungkan prev ke temp.next
        prev.next = temp.next
        temp = None

# ===============================================================
# Pertemuan 3 : Linked List (Tugas 3)
# Implementasikan Pencarian pada node tertentu Double Linked List
# ===============================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None #simpan node terakhir untuk traversing mundur
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def search(self, key):
        if not self.head:
            print("Doubly Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return False
        
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Doubly Linked List.")
                return True
            temp = temp.next
        print(f"Elemen {key} tidak ditemukan dalam Doubly Linked List.")
        return False
    
# Contoh Tampilan 1 :
# Masukkan	elemen	ke	dalam	Doubly	Linked	List:	2,	6,	9,	14,	20
# Masukkan	elemen	yang	ingin	dicari:	9
# Elemen	9	ditemukan	dalam	Doubly	Linked	List.
dll = DoublyLinkedList()
for x in [2, 6, 9, 14, 20]:
    dll.insert_at_end(x)

dll.search(9)

# ===============================================================
# Pertemuan 3 : Linked List (Tugas 5)
# Implementasikan Pencarian pada node tertentu Double Linked List
# ===============================================================


