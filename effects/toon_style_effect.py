import cv2

def convert_to_toon_style(input_path, output_path):
    """
    Mengubah gambar menjadi gaya kartun seperti animasi dengan warna halus dan garis tebal.
    
    Args:
        input_path (str): Lokasi file gambar yang akan diubah (misalnya, 'foto.jpg').
        output_path (str): Lokasi untuk menyimpan hasil gambar kartun.
    
    Returns:
        str: Lokasi file hasil (output_path).
    
    Raises:
        ValueError: Jika gambar gagal dimuat atau ada kesalahan saat memproses.
    """
