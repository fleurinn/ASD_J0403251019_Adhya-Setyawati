# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: NIM	berakhiran	angka	ganjil	mengerjakan Latihan	1,3,5
#
# Nama :Adhya Setyawati
# NIM :J0403251019
# Kelas :TPL B / P1
# ==========================================================

# --- jawaban : ---

# =============================================================================
# Pertemuan 3: Linked List
# Latihan 1: Implementasikan fungsi untuk menghapus node dengan nilai tertentu.
# =============================================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def delete_node(self, key):
        temp = self.head
    
        if temp and temp.data == key:
            self.head = temp.next
            temp= None           
            return
    
        prev = None
        while temp and temp.data != key :
            prev = temp
            temp = temp.next 
    
        if temp is None:
            return
    
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
        self.tail = None
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
# Masukkan elemen ke dalam Doubly Linked List: 2, 6, 9, 14, 20
# Masukkan elemen yang ingin dicari: 9
# Elemen 9 ditemukan dalam Doubly Linked List.
dll = DoublyLinkedList()
for x in [2, 6, 9, 14, 20]:
    dll.insert_at_end(x)

dll.search(9)

# ===============================================================
# Pertemuan 3 : Linked List (Tugas 5)
# Tambahkan metode untuk membalik (reverse) sebuah single linked list tanpa membuat linked list baru
# ===============================================================
class Node:  
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan elemen ke akhir linked list (perbaiki loop traversal)
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:  
            temp = temp.next
        temp.next = new_node

    # Menampilkan linked list
    def display(self):  
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # Membalik (reverse) linked list tanpa membuat linked list baru
    def reverse(self):
        prev = None  
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Membuat linked list dari input string
    def create_from_input(self, input_str):
        elements = input_str.split(", ")
        for elem in elements:  
            self.insert_at_end(int(elem.strip()))  

def main():  
    linked_list = LinkedList()
    input_str = input("Masukkan elemen untuk Linked List: ")  
    linked_list.create_from_input(input_str)
    print("Linked List sebelum dibalik: ", end="")
    linked_list.display() 
    linked_list.reverse()
    print("Linked List setelah dibalik: ", end="")
    linked_list.display()

if __name__ == "__main__":  
    main()
