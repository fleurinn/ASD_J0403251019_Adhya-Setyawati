#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 10
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
#--------------------------------------------------

# Class Node
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai
        self.left = None      # child kiri
        self.right = None     # child kanan

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # tampilkan data
        preorder(root.left)        # kiri
        preorder(root.right)       # kanan

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print(" " * level + f"{posisi}: {root.data}")  # tampil posisi
        tampil_struktur(root.left, level + 1, "L")     # kiri
        tampil_struktur(root.right, level + 1, "R")    # kanan

# Fungsi rotasi kiri
def rotate_left(x):
    # x adalah root lama
    y = x.right  # y adalah child kanan x
    T2 = y.left  # subtree kiri milik y disimpan sementara

    # Proses rotasi
    y.left = x   # x menjadi child kiri dari y
    x.right = T2 # child kanan x diganti dengan T2

    # y menjadi root baru
    return y

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)            # root awal
root.right = Node(20)      # child kanan
root.right.right = Node(30) # child kanan lagi

print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)

'''
PENJELASAN LATIHAN 5
kode ini digunakan untuk melakukan rotasi kiri pada binary search tree (bst) yang
tidak seimbang dengan kondisi condong ke kanan (10 → 20 → 30). fungsi
rotate_left bekerja dengan menjadikan child kanan sebagai root baru, lalu root
lama dipindahkan ke kiri. hasilnya tree menjadi lebih seimbang, yaitu 20 sebagai
root dengan 10 di kiri dan 30 di kanan. preorder dan tampil_struktur digunakan
untuk membandingkan kondisi tree sebelum dan sesudah rotasi.
'''