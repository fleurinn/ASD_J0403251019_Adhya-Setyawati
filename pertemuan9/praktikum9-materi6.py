#--------------------------------------------------
#Nama : Adhya Setyawati
#NIM : J0403251019
#Kelas : TPL/P1
#--------------------------------------------------


#--------------------------------------------------
#pertemuan 9 
#latihan 6: Membuat Struktur Organisasi
#--------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node 
        self.left = None # child kiri
        self.right= None # child kanan

# fungsi preorder  : Root ==> Left ==> Right
def preorder(node):                  # mendefinisikan fungsi preorder dengan parameter node
    if node is not None:             # cek apakah node tidak kosong
        print(node.data, end=" ")    # tampilkan data node dulu (root)
        preorder(node.left)          # lanjut ke child kiri (rekursif)
        preorder(node.right)         # terakhir ke child kanan

# membuat root
root = Node("Direktur")

#  membuat child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# membuat child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

# membuat child level 3
root.right.right = Node("Staff 3")

# menjalankan traversal preorder
print("Struktur Organisasi (preorder): ")
preorder(root)

# PENJELASAN
'''
kode ini membuat struktur binary tree untuk merepresentasikan struktur organisasi.
class node digunakan untuk menyimpan data jabatan serta memiliki child left dan child right
sebagai bawahan. kemudian dibuat fungsi preorder untuk melakukan traversal dengan urutan 
root → left → right menggunakan rekursi, di mana data node dicetak terlebih dahulu lalu 
dilanjutkan ke child left dan child right selama node tidak bernilai none. setelah itu dibuat tree 
dengan root "Direktur", yang memiliki dua child yaitu "Manajer A" di kiri dan "Manajer B" di kanan. 
selanjutnya "Manajer A" memiliki dua bawahan yaitu "Staff 1" dan "Staff 2",
sedangkan "Manajer B" memiliki satu bawahan yaitu "Staff 3". terakhir, fungsi
preorder(root) dipanggil untuk menampilkan urutan struktur organisasi sesuai metode preorder.
'''