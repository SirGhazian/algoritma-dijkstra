import heapq

# Algoritma Dijkstra
def algoDijkstra(graf, awal):
    jarak = {simpul: float("inf") for simpul in graf}
    jarak[awal] = 0  # Jarak dari simpul awal ke dirinya sendiri adalah 0

    # Membuat antrian prioritas untuk menyimpan simpul yang akan diproses
    antrian = [(0, awal)]

    while antrian:
        # Mengambil simpul dengan jarak terkecil dari antrian
        (jarakSaatIni, simpulSaatIni) = heapq.heappop(antrian)

        # Lewati simpul ini ika jarak saat ini lebih besar dari jarak yang sudah tercatat
        if jarakSaatIni > jarak[simpulSaatIni]:
            continue

        # Memperbarui jarak untuk setiap tetangga dari simpul saat ini
        for tetangga, bobotJarak in graf[simpulSaatIni].items():
            jarakBaru = jarakSaatIni + bobotJarak
            if jarakBaru < jarak[tetangga]:  # Jika ditemukan jalur yang lebih pendek
                jarak[tetangga] = jarakBaru
                heapq.heappush(
                    antrian, (jarakBaru, tetangga)
                )  # Masukkan ke antrian prioritas

    return jarak  # Mengembalikan hasil jarak terpendek dari simpul awal ke semua simpul lain


# Fungsi untuk cetak hasil sebagai visual
def cetakHasil(jarak, mulai):
    print(f"Mulai simpul: {mulai}")
    print("Bobot ke tujuan:")
    for simpul, bobot in jarak.items():
        if simpul != mulai:
            print(f"> {simpul}: {bobot}")


# Inisialisasi graf
graf = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 2},
    "C": {"A": 2, "B": 1, "D": 4, "E": 5},
    "D": {"B": 2, "C": 4, "E": 1},
    "E": {"C": 5, "D": 1},
}

# Contoh menjalankan algoritma Dijkstra dari simpul "A"
mulaiSimpul = "A"

hasil = algoDijkstra(graf, mulaiSimpul)
cetakHasil(hasil, mulaiSimpul)
