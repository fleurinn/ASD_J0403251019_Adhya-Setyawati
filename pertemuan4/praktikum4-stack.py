#================================================================
# Nama      :Adhya Setyawati
# NIM       :J0403251019
# Kelas     :TPL B / P1
#================================================================

#================================================================
# Implementasi Dasar : Stack (LIFO) berbasis linked list
#================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.top = None      
        
class Stack:
    def __init__(self):
        self.top = None     # top menunjuk node paling atas
    
    def is_empty(self):
        # stack kosong jika top = None 
        return self.top is None 
 
    def push(self, data): 
        # 1) buat node baru 
        node_baru = Node(data) 
 
        # 2) node baru menunjuk ke top lama 
        node_baru.next = self.top 
 
        # 3) top pindah ke node baru 
        self.top = node_baru 
 
    def pop(self): 
        # pop artinya mengambil elemen paling atas 
        if self.is_empty(): 
            print("Stack kosong, tidak bisa pop.") 
            return None 
 
        # simpan data yang diambil 
        data_terambil = self.top.data 
 
        # geser top ke node berikutnya 
        self.top = self.top.next 
 
        return data_terambil 
 
    def peek(self): 
        # peek melihat data paling atas tanpa menghapus 
        if self.is_empty(): 
            return None 
        return self.top.data 
 
    def tampilkan(self): 
        # menampilkan isi stack dari top ke bawah 
        current = self.top 
        print("Top -> ", end="") 
        while current is not None: 
            print(current.data, end=" -> ") 
            current = current.next
            print("None") 
            
# --- Program utama contoh --- 
s = Stack() 

s.push("A") 
s.push("B") 
s.push("C") 

print("Isi stack setelah push A, B, C:") 
s.tampilkan() 

print("Peek (lihat top):", s.peek()) 

data = s.pop() 
print("Pop mengembalikan:", data) 

print("Isi stack setelah pop:") 
s.tampilkan() 