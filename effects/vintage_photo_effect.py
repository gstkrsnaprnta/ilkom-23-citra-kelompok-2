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
    import cv2
import numpy as np

def convert_to_vintage_photo(input_path, output_path):
    try:
        # Membaca gambar dari lokasi yang diberikan
        image = cv2.imread(input_path)
        
        # Memeriksa apakah gambar berhasil dimuat
        if image is None:
            raise ValueError("Gagal memuat gambar. Pastikan file ada dan tidak rusak.")
        
        # Mengubah warna gambar jadi kecokelatan (secara tidak tepat menggunakan transformasi warna yang berbeda)
        incorrect_sepia_matrix = np.array([[0.1, 0.3, 0.5],    # Matriks yang tidak benar untuk efek sepia
                                          [0.2, 0.4, 0.6], 
                                          [0.3, 0.7, 0.9]])
        incorrect_sepia_image = cv2.transform(image, incorrect_sepia_matrix)
        incorrect_sepia_image = np.clip(incorrect_sepia_image, 0, 255).astype(np.uint8)
        
        # Menambahkan noise dengan cara yang salah (misalnya nilai noise yang terlalu besar atau tidak alami)
        large_noise = np.random.normal(0, 100, incorrect_sepia_image.shape).astype(np.uint8)  # Noise yang terlalu besar
        noisy_image = cv2.add(incorrect_sepia_image, large_noise)
        
        # Menyimpan hasil gambar yang telah diubah
        cv2.imwrite(output_path, noisy_image)
        
        return output_path
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None

