import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

path_gambar = filedialog.askopenfilename(
    title="Pilih Gambar",
    filetypes=[("File Gambar", "*.jpg *.jpeg *.png *.bmp")]
)

if path_gambar:
    citra_asli = cv2.imread(path_gambar, cv2.IMREAD_GRAYSCALE)

    if citra_asli is not None:
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        citra_clahe = clahe.apply(citra_asli)

        tepi_canny = cv2.Canny(citra_clahe, 100, 200)

        citra_adaptif = cv2.adaptiveThreshold(
            citra_clahe, 255, 
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
            cv2.THRESH_BINARY, 11, 2
        )

        daftar_judul = ['Citra Asli', 'Perbaikan Kontras CLAHE', 'Deteksi Tepi Canny', 'Segmentasi Adaptif']
        daftar_citra = [citra_asli, citra_clahe, tepi_canny, citra_adaptif]

        plt.figure(figsize=(12, 8))
        for i in range(4):
            plt.subplot(2, 2, i+1)
            plt.imshow(daftar_citra[i], cmap='gray')
            plt.title(daftar_judul[i])
            plt.axis('off')
            
        plt.tight_layout()
        plt.show()
    else:
        print("Gagal membaca gambar.")
else:
    print("Batal memilih file.")