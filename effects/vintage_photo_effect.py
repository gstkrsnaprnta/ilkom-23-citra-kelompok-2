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
        
        
        incorrect_sepia_matrix = np.array([[0.1, 0.3, 0.5],    
                                          [0.2, 0.4, 0.6], 
                                          [0.3, 0.7, 0.9]])
        incorrect_sepia_image = cv2.transform(image, incorrect_sepia_matrix)
        incorrect_sepia_image = np.clip(incorrect_sepia_image, 0, 255).astype(np.uint8)
        
        
        large_noise = np.random.normal(0, 100, incorrect_sepia_image.shape).astype(np.uint8) 
        noisy_image = cv2.add(incorrect_sepia_image, large_noise)
        
        # Menyimpan hasil gambar yang telah diubah
        cv2.imwrite(output_path, noisy_image)
        
        return output_path
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return None
    # Membuat pinggiran gelap untuk tampilan klasik
rows, cols = noisy_image.shape[:2]
kernel_x = cv2.getGaussianKernel(cols, cols / 2)  
kernel_y = cv2.getGaussianKernel(rows, rows / 2)  
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
mask = mask.astype(np.uint8)

vintage_image = noisy_image.copy()


for i in range(3):
    vintage_image[:, :, i] = vintage_image[:, :, i] * (1.5 + 0.5 * mask / 255)  


vintage_image = cv2.convertScaleAbs(vintage_image, alpha=2.0, beta=-50)  

# Menyimpan hasil gambar vintage ke lokasi yang ditentukan
cv2.imwrite(output_path, vintage_image)

# Mengembalikan lokasi file hasil
return output_path


