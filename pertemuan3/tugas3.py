# ==========================================================
# TUGAS PERTEMUAN 3
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
        
    # fungsi untuk menambah node di akhir 
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    # menghapus node sesuai nilai
    def delete_node(self, key):
        temp = self.head
        
        # jika node yang ingin dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            print("Data berhasil dihapus!")
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        # jika data tidak ditemukan
        if temp is None:
            print("Data tidak ditemukan!")
            return
        
        prev.next = temp.next
        temp = None
        print("Data berhasil dihapus!")
        
    # menampilkan isi linked list
    def display(self):
        temp = self.head
        if temp is None:
            print("Linked list kosong.")
            return
        
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")
            
# program utama

ll = LinkedList()

# input jumlah data
n = int(input("Masukkan jumlah data : ")) 
for i in range(n):
    data = int(input(f"Masukkan data ke-{i+1} : "))
    ll.append(data)
print("\nIsi Linked List : ")
ll.display() 
hapus = int(input("\nMasukkan nilai yang ingin dihapus : "))
ll.delete_node(hapus)
print("\nLinked list setelah dihapus")
ll.display()
# ===============================================================
# Pertemuan 3 : Linked List (Tugas 3)
# Latihan 3: Implementasikan Pencarian pada node tertentu Double Linked List
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
    
# --- output ---
dll = DoublyLinkedList()

input_data = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")
elements = input_data.split(",")

for elem in elements:
    elem = elem.strip()
    if elem != "":
        dll.insert_at_end(int(elem))

key = int(input("Masukkan elemen yang ingin dicari: "))
dll.search(key)


# ===============================================================
# Pertemuan 3 : Linked List (Tugas 5)
# Latihan 5: Tambahkan metode untuk membalik (reverse) sebuah single linked list tanpa membuat linked list baru
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
