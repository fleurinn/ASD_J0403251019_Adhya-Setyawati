#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 10
# Latihan 4: Membuat BST yang Tidak Seimbang
#--------------------------------------------------

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data  # nilai pada node
        self.left = None  # child kiri
        self.right = None  # child kanan

# Fungsi insert untuk BST
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data) # buat node
    
    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data) # ke kiri
    
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data) # ke kanan
    
    return root # kembalikan root

# Fungsi preorder untuk melihat bentuk tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # tampilkan data
        preorder(root.left)        # kiri
        preorder(root.right)       # kanan

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")  # tampil posisi
        tampil_struktur(root.left, level + 1, "L")     # kiri
        tampil_struktur(root.right, level + 1, "R")    # kanan

# -----------------------------
# Program utama
# -----------------------------
root = None  # root kosong

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data) # insert ke bst

print("Preorder BST:")
preorder(root) # panggil fungsi

print("\n\nStruktur BST:")
tampil_struktur(root) # tampilkan tree

'''
PENJELASAN LATIHAN 4
kode ini digunakan untuk membuat binary search tree (bst) dengan data yang
dimasukkan secara berurutan naik, yaitu 10, 20, dan 30. karena urutan data selalu
lebih besar dari sebelumnya, setiap node baru akan selalu masuk ke sisi kanan,
sehingga tree menjadi tidak seimbang dan condong ke kanan seperti linked list.
fungsi preorder digunakan untuk menampilkan isi tree, sedangkan fungsi
tampil_struktur digunakan untuk melihat bentuk struktur tree secara visual. kondisi
ini menunjukkan kelemahan bst yang tidak seimbang karena dapat membuat
proses pencarian menjadi lebih lambat.
'''