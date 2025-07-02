import cv2
import numpy as np

def convert_to_grayscale(input_path, output_path):
    """
    Args:
        input_path (str): Lokasi file gambar yang akan diubah (misalnya, 'foto.jpg').
        output_path (str): Lokasi untuk menyimpan hasil gambar dengan efek Monochrome Glow.
    
    Returns:
        str: Lokasi file hasil (output_path).
    
    Raises:
        ValueError: Jika gambar gagal dimuat (misalnya, file rusak atau tidak ada).
    """
    # Membaca gambar dari lokasi yang diberikan
    image = cv2.imread(input_path)
    
    # Memeriksa apakah gambar berhasil dimuat
    if image is None:
        raise ValueError("Gagal memuat gambar. Pastikan file ada dan tidak rusak.")
    
    # Menggabungkan gambar grayscale dengan gambar yang diblur untuk efek glow
    glow_image = cv2.addWeighted(gray_image, 0.5, blurred, 0.5, 0)
    
    # Mengubah kembali ke format BGR agar kompatibel dengan efek lain
    glow_image = cv2.cvtColor(glow_image, cv2.COLOR_GRAY2BGR)
    
    # Menyimpan hasil gambar dengan efek Monochrome Glow
    cv2.imwrite(output_path, glow_image)
    
    # Mengembalikan lokasi file hasil
    return output_path
