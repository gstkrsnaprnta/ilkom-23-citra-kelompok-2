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
    
    # Memeriksa apakah gambar berhasil dimuat
    if img is None:
        raise ValueError("Gagal memuat gambar. Pastikan file ada dan tidak rusak.")
    
    # Mendapatkan ukuran asli gambar
    h, w = img.shape[:2]

    # Menentukan ukuran baru berdasarkan pilihan resolusi
    if resolution == 'original':
        new_w, new_h = w, h
    elif resolution == '720p':
        new_w, new_h = 1280, 720
    elif resolution == '1080p':
        new_w, new_h = 1920, 1080
    elif resolution == 'custom':
        # Validasi input lebar dan tinggi
        if width is None or height is None:
            raise ValueError("Lebar dan tinggi harus ditentukan untuk resolusi 'custom'.")
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("Lebar dan tinggi harus berupa angka bulat.")
        if width <= 0 or height <= 0:
            raise ValueError("Lebar dan tinggi harus lebih besar dari 0.")
        new_w, new_h = width, height
    else:
        raise ValueError("Pilihan resolusi tidak valid. Gunakan 'original', '720p', '1080p', atau 'custom'.")
