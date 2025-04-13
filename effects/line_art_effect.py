import cv2

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
    
