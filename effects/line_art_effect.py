import cv2
import numpy as np

def resize_image(input_path, output_path, resolution='original', width=None, height=None):
    """
    Mengubah ukuran gambar untuk menyesuaikan kualitas saat diunduh, misalnya ke 720p atau ukuran khusus.
    
  Args:
        input_path (str): Lokasi file gambar yang akan diubah (misalnya, 'foto.jpg').
        output_path (str): Lokasi untuk menyimpan hasil gambar.
        resolution (str): Pilihan ukuran: 'original', '720p', '1080p', atau 'custom'.
        width (str): Lebar khusus untuk resolusi 'custom' (opsional).
        height (str): Tinggi khusus untuk resolusi 'custom' (opsional).
    
   Returns:
        str: Lokasi file hasil (output_path).
    
  Raises:
        ValueError: Jika gambar gagal dimuat atau parameter ukuran tidak valid.
    """
 # Membaca gambar dari lokasi yang diberikan
    img = cv2.imread(input_path)
    
 # Memeriksa apakah gambar berhasil dimuat
        if image is None:
            raise ValueError("Gagal memuat gambar. Pastikan file ada dan tidak rusak.")
        
 # Mengubah gambar berwarna menjadi hitam-putih untuk memudahkan deteksi garis
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

 # Membuat garis seni dengan menonjolkan tepi gambar
        edges = cv2.Canny(gray, low_threshold, high_threshold)
     
 # Mengubah kembali ke format warna agar cocok dengan efek lain
        edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
 # Menyimpan hasil gambar garis seni ke lokasi yang ditentukan
        cv2.imwrite(output_path, edges_bgr)
        
