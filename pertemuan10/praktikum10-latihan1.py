#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------


#--------------------------------------------------
# pertemuan 10
# latihan 1: BST
#--------------------------------------------------

class Node: # class untuk node BST
    def __init__(self, data):
        self.data = data # menyimpan nilai
        self.left = None # child kiri
        self.right = None # child kanan

# fungsi insert BST
def insert(root, data):
    if root is None: # jika kosong, buat node baru
        return Node(data)
    
    # jika lebih kecil, ke kiri
    if data < root.data:
        root.left = insert(root.left, data)

    # jika lebih besar, ke kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

# mengisi data bst
root = None # root awal kosong
data_list = [50,30,70,20,40,50,80] # data input

# insert ke BST
for data in data_list:
    root = insert(root, data)

print("BST berhasil dibuat")

#--------------------------------------------------
# Latihan 2: Traversal Inorder
#--------------------------------------------------

# fungsi inorder: traversal kiri -> root -> kanan (menghasilkan urutan ascending)
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
print("Hasil inorder:")
inorder(root) # panggil fungsi

#--------------------------------------------------
# Latihan 3: Search BST
#--------------------------------------------------
def search(root, key):       # fungsi search
    if root is None:         # jika kosong
        return False         # tidak ditemukan
    if root.data == key:     # jika ketemu
        return True          # ditemukan
    elif key < root.data:    # jika lebih kecil
        return search(root.left, key) # cari kiri
    else:                    # jika lebih besar
        return search(root.right, key) # cari kanan
    
# Uji pencarian
key = 10                     # data yang dicari
if search(root, key):        # cek hasil
    print("Data ditemukan")  # jika ada
else:
    print("Data tidak ditemukan") # jika tidak ada


# PENJELASAN LATIHAN 1,2,3
'''
PENJELASAN LATIHAN 1
kode ini digunakan untuk membuat struktur binary search tree (bst) dengan aturan nilai lebih kecil 
ke kiri dan lebih besar ke kanan. data dimasukkan satu per satu menggunakan fungsi insert, 
sehingga terbentuk struktur tree yang terurut berdasarkan perbandingan nilai.
'''
'''
PENJELASAN LATIHAN 2
kode ini berfungsi untuk menampilkan isi bst menggunakan metode inorder (kiri -> root -> kanan). 
hasil traversal ini secara otomatis menghasilkan data dalam urutan terurut (ascending).
'''
'''
PENJELASAN LATIHAN 3
kode ini digunakan untuk mencari suatu nilai dalam bst secara efisien. pencarian dilakukan 
dengan membandingkan nilai target dengan root, lalu bergerak ke kiri atau kanan sampai data 
ditemukan atau tidak ada.
''' 