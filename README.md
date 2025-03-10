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
| <img src="https://github.com/user-attachments/assets/13401d81-9ac9-4df5-a8a2-84829e67c84a" width="400"> | Tetapkan Stasiun A dengan waktu tempuh 0 menit, sementara stasiun lain ∞. Dari A, Stasiun B diperbarui menjadi 4 menit dan Stasiun C menjadi 2 menit. |
| <img src="https://github.com/user-attachments/assets/421cae94-7478-4781-bba0-45d7a0f18623" width="400"> | Pilih stasiun dengan estimasi terkecil yang belum dieksplorasi, yaitu Stasiun C (2 menit). |
| <img src="https://github.com/user-attachments/assets/be8e015b-86c9-4b59-84cd-a97c51bb27b3" width="400"> | Perbarui estimasi stasiun yang terhubung langsung. Stasiun E, dengan waktu tempuh 5 menit dari Stasiun C, menjadi 7 menit. |
| <img src="https://github.com/user-attachments/assets/11800ef0-1d62-4394-81cb-8753b00b4dbb" width="400"> | Jika ditemukan jalur lebih cepat, perbarui estimasi. Misalnya, jalur dari Stasiun C ke Stasiun B (1 menit) membuat total waktu ke Stasiun B menjadi 3 menit. <br>  <br> Pilih stasiun belum dieksplorasi dengan estimasi terkecil dan lanjutkan proses. <br> <br>  Ulangi pembaruan estimasi setiap kali ada jalur lebih cepat. |
| <img src="https://github.com/user-attachments/assets/0b1e8b42-e19f-4acc-8693-b8a1b2101460" width="400"> | Jika Stasiun D menjadi stasiun berikutnya yang dieksplorasi, berarti hampir selesai. <br> <br>  Ketika Stasiun D telah dieksplorasi, jalur tercepat telah ditemukan. |


###


---

<br>

<h1 align="left">‣【 Informasi Dosen 】</h1>
<img align="left" width="160" src="https://github.com/SirGhazian/praktikum-struktur-data-UNP/assets/142916107/58bffcd0-9983-4a84-9fc6-857c625cb609">

**Randi Proska Sandra, S.Pd, M.Sc** </br>
`Lecturer in Informatics` </br></br>
Randi completed his graduate degree at the Graduate Institute of Network Learning Technology, National Central University, Taiwan. He is a lecturer in the Informatics Bachelor Program at Universitas Negeri Padang, with interests in learning analytics, UI/UX design, software engineering project management, AI-supported educational technologies, and educational data mining. He has training from Microsoft, INTEL, AWS, and the Python Institute, and is a Google Certified Educator and Adobe Creative Educator.

<br>

<h1 align="left">‣【 About and Help 】</h1>
Untuk bantuan dan pertanyaan, silahkan hubungi sosial media saya:
<img align="right" width="100" src="https://github.com/SirGhazian/praktikum-struktur-data-UNP/assets/142916107/b140fe43-3a57-4295-8493-79d929a5e3b0"> 

- [![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/ghazian_tza)
- [![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)](https://www.youtube.com/channel/UCIp_064wQ8RqNSEy1asx_4w) 
