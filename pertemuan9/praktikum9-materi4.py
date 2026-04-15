#--------------------------------------------------
#Nama : Adhya Setyawati
#NIM : J0403251019
#Kelas : TPL/P1
#--------------------------------------------------


#--------------------------------------------------
#pertemuan 9 
#latihan 1: Membuat Node Tree Inorder
#--------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node 
        self.left = None # child kiri
        self.right= None # child kanan

# fungsi inorder  :   Left ==> Root ==> Right
def inorder(node):                   # mendefinisikan fungsi inorder dengan parameter node
    if node is not None:             # cek apakah node tidak kosong (biar ga error)
        inorder(node.left)           # kunjungi dulu child kiri (rekursif ke kiri terus)
        print(node.data, end=" ")    # setelah kiri, baru tampilkan data node sekarang
        inorder(node.right)          # terakhir kunjungi child kanan (rekursif ke kanan)

# membuat root
root = Node("A")

#  membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat child level 2
root.left.left = Node("D")
root.right.right = Node("E")

# menjalankan traversal preorder
print("Hasil traversal preorder: ")
inorder(root)

# PENJELASAN
'''
kode ini membuat struktur binary tree menggunakan class node, di mana setiap
node menyimpan data serta memiliki child left dan child right. kemudian dibuat
fungsi inorder untuk melakukan traversal dengan urutan left → root → right
menggunakan rekursi. fungsi ini akan mengunjungi node kiri terlebih dahulu,
lalu mencetak data node saat ini, kemudian lanjut ke node kanan selama node tidak bernilai none.
setelah itu dibuat tree dengan root "A", memiliki child "B" di kiri dan "C" di kanan,
lalu "D" sebagai child left dari "B" dan "E" sebagai child right dari "C".
terakhir, fungsi inorder(root) dipanggil untuk menampilkan hasil traversal sesuai metode inorder.
'''