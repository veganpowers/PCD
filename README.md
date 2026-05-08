PROYEK UTS MATKUL PENGOLAHAN CITRA DIGITAL

# Sistem Pengolahan Citra: Kontras, Tepi, dan Segmentasi

Repositori ini berisi implementasi program pengolahan citra digital berbasis Python. Program ini mengaplikasikan tiga teknik utama pengolahan spasial untuk mengekstraksi dan memperjelas informasi visual dari sebuah gambar mentah.

## Fitur Utama

1. Perbaikan Kontras (CLAHE): Meratakan distribusi intensitas piksel secara lokal untuk memperjelas detail tekstur objek tanpa menimbulkan gangguan visual (noise) yang berlebihan.
2. Deteksi Tepi (Canny): Melacak batas fisik dan kerangka struktural objek menggunakan filter penghalusan Gaussian dan perhitungan gradien intensitas.
3. Segmentasi Biner (Adaptive Thresholding): Memisahkan objek utama dari elemen latar belakang menjadi format hitam-putih murni, dengan perhitungan nilai ambang yang menyesuaikan kondisi pencahayaan dinamis.
4. Visualisasi Terpadu: Menampilkan perbandingan langsung antara citra asli dan ketiga hasil pemrosesan dalam satu jendela antarmuka yang bersih.

## Prasyarat

Pastikan sistem Anda sudah terinstal Python versi 3.x. Program ini bergantung pada beberapa pustaka eksternal. Anda dapat menginstalnya menggunakan perintah pip berikut:

pip install opencv-python matplotlib

## Cara Menjalankan Program

Ada dua cara untuk menjalankan program ini di perangkat Anda:

Opsi 1: Melalui Terminal atau Command Prompt
1. Buka terminal dan arahkan ke dalam folder repositori ini.
2. Ketik perintah berikut lalu tekan Enter:
   python main.py
3. Sebuah jendela penjelajah file akan muncul. Pilih gambar yang ingin Anda proses.

Opsi 2: Melalui Batch File (Khusus Pengguna Windows)
1. Pastikan Anda berada di dalam folder repositori.
2. Klik ganda (double-click) pada file run.bat.
3. Program akan otomatis dieksekusi dan meminta Anda memilih gambar.

## Struktur File

- main.py : Kode sumber utama yang berisi logika pengolahan citra dan visualisasi.
- run.bat : Script eksekusi cepat untuk sistem operasi Windows.
- README.md : Dokumentasi lengkap mengenai proyek ini.

## Artikel Terkait

Penjelasan konsep teoritis mengenai eksperimen perbaikan kontras, pelacakan garis tepi, dan pemisahan objek pada proyek ini dapat dibaca selengkapnya pada publikasi Medium berikut:
[Tambahkan Link Artikel Medium Anda Di Sini]

## Penulis

Dikembangkan oleh veganpowers.
