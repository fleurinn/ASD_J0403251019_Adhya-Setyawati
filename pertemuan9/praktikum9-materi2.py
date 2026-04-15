#--------------------------------------------------
#Nama : Adhya Setyawati
#NIM : J0403251019
#Kelas : TPL/P1
#--------------------------------------------------


#--------------------------------------------------
#pertemuan 9 
#latihan 2: Membuat Binary Search Tree sederhana 
#--------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node 
        self.left = None # child kiri
        self.right= None # child kanan

# membuat root 
root = Node("A")

#  membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# membuat child level 3
root.right.left = Node("F")
root.right.right = Node("G")

# menampilkan isi node 
print("Data pada root : ", root.data)
print("Data child kiri root : ", root.left.data)
print("Data child kanan root : ", root.right.data)
print("Data child kiri dari B : ", root.left.left.data)
print("Data child kanan dari B : ", root.left.right.data)
print("Data child kiri dari C : ", root.right.left.data)
print("Data child kanan dari C : ", root.right.right.data)

# PENJELASAN
'''
kode ini membuat struktur binary tree menggunakan class node, yang di mana 
setiap node menyimpan data serta memiliki dua atribut yaitu left dan right sebagai
child kiri dan kanan. pertama dibuat root dengan nilai "A", lalu ditambahkan child 
level 1 yaitu "B" di sebelah kiri dan "C" di sebelah kanan. selanjutnya ditambahkan child
level 2, di mana "B" memiliki child left "D" dan child right "E", serta "C" memiliki child left "F" dan child right "G". 
di bagian akhir kode, digunakan untuk menampilkan isi setiap node denhgan mengakses atribut data 
dari masing-masing node melalui relasi parent-child yang sudah dibentuk sebelumnya.
'''