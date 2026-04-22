#--------------------------------------------------
#Nama : Adhya Setyawati
#NIM : J0403251019
#Kelas : TPL/P1
#--------------------------------------------------


#--------------------------------------------------
#pertemuan 9 
#latihan 1: Membuat Node Tree PostOrder
#--------------------------------------------------

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data # menyimpan nilai node 
        self.left = None # child kiri
        self.right= None # child kanan

# fungsi postorder  : Left ==> Right ==> Root  
def postorder(node):                 # mendefinisikan fungsi postorder dengan parameter node
    if node is not None:             # cek apakah node tidak kosong
        postorder(node.left)         # kunjungi child kiri dulu (rekursif)
        postorder(node.right)        # lalu kunjungi child kanan
        print(node.data, end=" ")    # terakhir baru tampilkan data node (root)

# membuat tree
# membuat root
root = Node("A")

#  membuat child level 1
root.left = Node("B")
root.right = Node("C")

# membuat child level 2
root.left.left = Node("D")
root.right.right = Node("E")

# menjalankan traversal preorder
print("Hasil traversal postorder: ")
postorder(root)

# PENJELASAN
'''
kode ini membuat struktur binary tree menggunakan class node, di mana setiap
node menyimpan data serta memiliki child left dan child right. kemudian dibuat 
fungsi postorder untuk melakukan traversal dengan urutan left → right → root
menggunakan rekursi. fungsi ini akan mengunjungi node kiri terlebih dahulu,
lalu node kanan, dan terakhir mencetak data node selama node tidak bernilai none.
setelah itu dibuat tree dengan root "A", memiliki child "B" di kiri dan "C" di kanan,
lalu "D" sebagai child left dari "B" dan "E" sebagai child right dari "C". terakhir,
fungsi postorder(root) dipanggil untuk menampilkan hasil traversal sesuai metode postorder.
'''