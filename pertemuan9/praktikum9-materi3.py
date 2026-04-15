#--------------------------------------------------
#Nama : Adhya Setyawati
#NIM : J0403251019
#Kelas : TPL/P1
#--------------------------------------------------


#--------------------------------------------------
#pertemuan 9 
#latihan 3: Membuat Node Tree Preorder
#--------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node 
        self.left = None # child kiri
        self.right= None # child kanan

# fungsi preorder  : Root  ==> Left ==> Right
def preorder(node):                    # definisi fungsi preorder dengan parameter node (node saat ini)
    if node is not None:               # cek apakah node tidak kosong 
        print(node.data, end=' ')      # tampilkan data node sekarang (root)
        preorder(node.left)            # panggil fungsi ke child kiri
        preorder(node.right)           # panggil fungsi ke child kanan

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
preorder(root)

# PENJELASAN
'''
kode ini membuat struktur binary tree menggunakan class node, di mana setiap
node menyimpan data serta memiliki child left dan child right. setelah itu
dibuat fungsi preorder untuk melakukan traversal dengan urutan root → left → right,
menggunakan konsep rekursif. fungsi ini akan mencetak data node terlebih dahulu,
lalu memanggil dirinya sendiri ke child left dan child right selama node tidak bernilai none.
selanjutnya dibuat tree dengan root "A", kemudian ditambahkan child "B" di kiri dan "C" di kanan,
serta node "D" sebagai child left dari "B" dan node "E" sebagai child right dari "C".
terakhir, fungsi preorder(root) dijalankan untuk menampilkan urutan traversal sesuai metode preorder.
'''