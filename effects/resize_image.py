import cv2

def resize_image(input_path, output_path, resolution='original', width=None, height=None):
    """
    Mengubah ukuran gambar untuk menyesuaikan kualitas saat diunduh, misalnya ke 720p atau ukuran khusus.
    
    
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
        # Memeriksa apakah lebar dan tinggi valid
        try:
            new_w = int(width)
            new_h = int(height)
            if new_w <= 0 or new_h <= 0:
                raise ValueError("Lebar dan tinggi khusus harus angka positif.")
        except (TypeError, ValueError):
            raise ValueError("Lebar dan tinggi khusus harus angka positif.")
    else:
        raise ValueError("Pilihan resolusi tidak valid. Gunakan 'original', '720p', '1080p', atau 'custom'.")
    
    # Mengubah ukuran gambar jika berbeda dari aslinya
    if (new_w, new_h) != (w, h):
        # Memilih metode terbaik: INTER_CUBIC untuk memperbesar, INTER_AREA untuk memperkecil
        if new_w * new_h > w * h:
            interpolation = cv2.INTER_CUBIC
        else:
            interpolation = cv2.INTER_AREA
        result = cv2.resize(img, (new_w, new_h), interpolation=interpolation)
    else:
        result = img
    
    # Menyimpan hasil gambar ke lokasi yang ditentukan
    cv2.imwrite(output_path, result, [cv2.IMWRITE_JPEG_QUALITY, 90])
    
    # Mengembalikan lokasi file hasil
    return output_path
