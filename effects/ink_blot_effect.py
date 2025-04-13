import cv2

def convert_to_ink_blot(input_path, output_path, threshold=127):
    """
    Mengubah gambar menjadi gaya tinta hitam-putih seperti noda tinta.
    
    Args:
        input_path (str): Lokasi file gambar yang akan diubah (misalnya, 'foto.jpg').
        output_path (str): Lokasi untuk menyimpan hasil gambar tinta.
        threshold (int): Nilai batas untuk memisahkan hitam dan putih (default: 127).
    
    Returns:
        str: Lokasi file hasil (output_path).
    
    Raises:
        ValueError: Jika gambar gagal dimuat atau ada kesalahan saat memproses.
    """
