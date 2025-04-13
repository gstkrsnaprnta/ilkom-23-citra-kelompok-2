import cv2
import numpy as np

def convert_to_vintage_photo(input_path, output_path):
    """
    Mengubah gambar menjadi gaya foto lama dengan warna kecokelatan, bintik, dan pinggiran gelap.
    
    Args:
        input_path (str): Lokasi file gambar yang akan diubah (misalnya, 'foto.jpg').
        output_path (str): Lokasi untuk menyimpan hasil gambar vintage.
    
    Returns:
        str: Lokasi file hasil (output_path).
    
    Raises:
        ValueError: Jika gambar gagal dimuat atau ada kesalahan saat memproses.
    """
