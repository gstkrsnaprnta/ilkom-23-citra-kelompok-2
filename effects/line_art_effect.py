import cv2
import numpy as np

def convert_to_line_art(input_path, output_path, low_threshold=100, high_threshold=200):
    """
    Mengubah gambar menjadi gambar garis seni (line art) yang menonjolkan garis tepi.
    
    Args:
        input_path (str): Lokasi file gambar yang akan diubah (misalnya, 'foto.jpg').
        output_path (str): Lokasi untuk menyimpan hasil gambar garis seni.
        low_threshold (int): Nilai minimum untuk mendeteksi garis (default: 100).
        high_threshold (int): Nilai maksimum untuk mendeteksi garis (default: 200).
    
    Returns:
        str: Lokasi file hasil (output_path).
    
    Raises:
        ValueError: Jika gambar gagal dimuat atau ada kesalahan saat memproses.
    """
    try:
        # Membaca gambar dari lokasi yang diberikan

