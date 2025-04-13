import cv2
import numpy as np

def convert_to_art_sketch(input_path, output_path):
    """
    Mengubah gambar menjadi gaya sketsa seni dengan garis lembut dan detail halus.
    
    Args:
        input_path (str): Lokasi file gambar yang akan diubah (misalnya, 'foto.jpg').
        output_path (str): Lokasi untuk menyimpan hasil gambar sketsa.
    
    Returns:
        str: Lokasi file hasil (output_path).
    
    Raises:
        ValueError: Jika gambar gagal dimuat atau ada kesalahan saat memproses.
    """
    try:
        # Membaca gambar dari lokasi yang diberikan
        image = cv2.imread(input_path)
        
        # Memeriksa apakah gambar berhasil dimuat
        if image is None:
            raise ValueError("Gagal memuat gambar. Pastikan file ada dan tidak rusak.")
        
        # Mengubah gambar ke hitam-putih untuk mempersiapkan sketsa
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Menghaluskan gambar untuk membuat garis lebih rapi
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
