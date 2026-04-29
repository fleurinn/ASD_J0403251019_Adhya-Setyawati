#--------------------------------------------------
# Nama : Adhya Setyawati
# NIM : J0403251019
# Kelas : TPL/P1
#--------------------------------------------------

#--------------------------------------------------
# pertemuan 11
# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)
#--------------------------------------------------

# membuat representasi graph menggunakan dictionary
# setiap key adalah node, dan value adalah list tetangganya (adjacency list)
graph = {
 'A': ['B', 'C'],   # node A terhubung ke B dan C
 'B': ['D', 'E'],   # node B terhubung ke D dan E
 'C': ['F'],        # node C terhubung ke F
 'D': [],           # node D tidak punya tetangga
 'E': [],           # node E tidak punya tetangga
 'F': []            # node F tidak punya tetangga
}

# fungsi DFS (Depth First Search)
def dfs(graph, node, visited):
    # menandai node yang sedang dikunjungi agar tidak dikunjungi lagi
    visited.add(node)
    # mencetak node yang dikunjungi
    print(node, end=" ")

    # melakukan perulangan untuk setiap tetangga dari node sekarang
    for neighbor in graph[node]:
        # jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # panggil DFS lagi (rekursif) ke tetangga tersebut
            dfs(graph, neighbor, visited)

# membuat set kosong untuk menyimpan node yang sudah dikunjungi
visited = set()

# menampilkan teks awal
print("DFS dari A:")
# memanggil fungsi DFS mulai dari node 'A'
dfs(graph, 'A', visited)

'''
Pertanyaan Analisis
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
Jawab : DFS menggunakan pendekatan rekursif yang cara kerjanya menyerupai struktur data Stack (LIFO).
        Saat mengunjungi suatu node, DFS akan memilih satu tetangga dan terus menelusuri ke dalam hingga 
        mencapai node paling dalam. Setelah mencapai ujung (node tanpa tetangga yang belum dikunjungi), 
        DFS akan melakukan backtracking untuk kembali ke node sebelumnya dan melanjutkan penelusuran ke 
        cabang lainnya.
2. Apa yang terjadi jika urutan neighbor diubah?
Jawab : Jika urutan neighbor di dalam struktur graph diubah, maka cabang yang ditelusuri terlebih dahulu juga akan 
        berubah mengikuti urutan list tersebut. Contoh: Pada aslinya graph['A'] = ['B', 'C'], maka DFS menelusuri 
        cabang 'B' sampai ujung terlebih dahulu. Namun jika diubah menjadi graph['A'] = ['C', 'B'], maka DFS akan 
        menelusuri cabang 'C' beserta seluruh turunannya hingga ujung terlebih dahulu, barulah melakukan backtrack
        untuk menelusuri cabang 'B'."
3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
Jawab : Jika kita menjalankan kedua algoritma pada graph di atas dengan titik awal A, perbedaannya adalah pada cara 
        perluasannya:
        - hasil pada DFS (A -> B -> D-> E-> C-> F): Menelusuri secara vertikal/mendalam. Ia mengunjungi A, lalu masuk ke B.
        ia menurun terus (vertikal) ke D. Karena D buntu, backtrack/mundur satu langkah ke B baru turun ke E, E tidak memiliki 
        tetangga (maka cabang dari B habis), backtrack ke A, dan menelusuri cabang di sebelahnya yaitu C, lalu turun ke F, 
        selesai. 
        - hasil pada BFS (A -> B -> C -> D -> E -> F):Menelusuri secara horinzontal/level per level. Ia mengunjungi node 
        awal A (level 0). Lalu mengunjungi semua tetangga langsung dari A, yaitu B dan C (Level 1). Setelah level 1 habis, 
        barulah BFS turun mengunjungi tetangga dari B terlabih dahulu yaitu D dan E, cabang dari B habis, lalu beralih ke 
        C, yaitu F, cabang C habis maka penelusuran pada level 2 terhenti, programpun selesai.
'''