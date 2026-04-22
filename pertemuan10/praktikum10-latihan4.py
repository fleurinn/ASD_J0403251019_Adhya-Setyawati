#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 10
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
#--------------------------------------------------

# Class Node
class Node:
    def __init__(self, data):
        self.data = data      # menyimpan nilai
        self.left = None      # child kiri
        self.right = None     # child kanan

# Fungsi preorder
def preorder(root):
    if root is not None:
        print(root.data, end=" ")  # tampilkan data
        preorder(root.left)        # kiri
        preorder(root.right)       # kanan

# Fungsi tampil struktur
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("   " * level + f"{posisi}: {root.data}")  # tampil posisi
        tampil_struktur(root.left, level + 1, "L")       # kiri
        tampil_struktur(root.right, level + 1, "R")      # kanan

# Fungsi rotasi kanan
def rotate_right(y):
    x = y.left        # x adalah child kiri
    T2 = x.right      # subtree kanan milik x disimpan

    # Proses rotasi
    x.right = y       # y jadi child kanan dari x
    y.left = T2       # child kiri y diganti T2

    return x          # x jadi root baru

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree tidak seimbang
# 30 -> 20 -> 10 (ke kiri)
root = Node(30)            # root awal
root.left = Node(20)       # child kiri
root.left.left = Node(10)  # child kiri lagi

print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Rotasi kanan
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)

'''
PENJELASAN LATIHAN 6
kode ini digunakan untuk melakukan rotasi kanan pada binary search tree (bst)
yang tidak seimbang dengan kondisi condong ke kiri (30 → 20 → 10). fungsi
rotate_right bekerja dengan menjadikan child kiri sebagai root baru, lalu root lama
dipindahkan ke kanan. hasilnya tree menjadi lebih seimbang, yaitu 20 sebagai root
dengan 10 di kiri dan 30 di kanan. preorder dan tampil_struktur digunakan untuk
melihat perubahan struktur tree sebelum dan sesudah rotasi.
'''