<div align="center">
  <img height="150" src="https://github.com/user-attachments/assets/6fac93e9-dce1-4ab7-b8e4-1491592555f3"/>
</div>

---
<img align="right" height="300" src="https://upload.wikimedia.org/wikipedia/commons/d/d9/Edsger_Wybe_Dijkstra.jpg"  />

<p align="left">Algoritma Dijkstra adalah metode untuk menemukan jalur terpendek dalam graf berbobot non-negatif, dikembangkan oleh Edsger W. Dijkstra pada 1956. Algoritma ini termasuk kategori “greedy” karena selalu memilih solusi terbaik secara lokal dengan harapan memperoleh solusi optimal (Levitin, 2012).<br><br>Prosesnya dimulai dengan menandai simpul awal dengan jarak nol dan simpul lainnya dengan jarak tak hingga. Simpul dengan jarak terkecil dipilih, jarak tetangganya diperbarui jika ditemukan jalur lebih pendek, lalu ditandai sebagai “dikunjungi.” Proses ini berulang hingga semua simpul dikunjungi atau tujuan tercapai (Javaid, 2013).<br><br>Dijkstra banyak digunakan dalam sistem navigasi seperti Google Maps dan perutean jaringan komputer karena efisiensinya dalam menemukan jalur terpendek dengan kompleksitas waktu yang relatif rendah (Tim Penulis GeeksForGeeks, 2024).</p>

---

<br>

<h1 align="left">‣【 Contoh Kasus 】</h1> 

###

<p align="left">Diberikan beberapa stasiun yang terhubung oleh jalur perjalanan dengan waktu tempuh berbeda. Tujuannya adalah menemukan waktu tercepat dari Stasiun A ke Stasiun D.
  
<div align="center">
  <img height="200" src="https://github.com/user-attachments/assets/f6c4ee98-189f-4724-92dd-296a85139c38"/>
</div>

Graf berbobot merepresentasikan stasiun sebagai simpul dan jalur sebagai sisi dengan bobot waktu tempuh. Algoritma Dijkstra digunakan dengan menetapkan semua stasiun bernilai ∞ kecuali Stasiun A (0). Stasiun dengan jalur terpendek dieksplorasi hingga mencapai Stasiun D.</p>

###

<br>

<h1 align="left">‣【 Langkah Penyelesaian 】</h1>


| Graf | Penjelasan |
|--------|-----------|
| <img src="1" width="100"> | 1 |
| <img src="2" width="100"> | 2 |


###
