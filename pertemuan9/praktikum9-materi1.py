#--------------------------------------------------
#Nama : Adhya Setyawati
#NIM : J0403251019
#Kelas : TPL/P1
#--------------------------------------------------


#--------------------------------------------------
#pertemuan 9 
#latihan 1: Membuat Node Tree 
#--------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node 
        self.left = None # child kiri
        self.right= None # child kanan

# membuat root 
root = Node("A")

#  menmapilkan isi node 
print("Data pada root : ", root.data)
print("Data child kiri root", root.left)
print("Data child kanan root", root.right)

# PENJELASAN
'''
kode ini merupakan struktur dasar untuk binary tree. class Node dipakai untuk menyimpan satu data dan mempunyai dua cabang, 
yaitu child left dan child right, yang diawali set None karena belum memiliki isi data. code root = Node("A"), untuk membuat node utama dengan nilai "A"
karena belum di tambah child, maka child kiri dan kanan masih kosong (none). bagian print digunakan untuk check isi node tersebut, jadi yang muncul adalah data
dari root "A" dan kedua child tersebut masih kosong.
'''