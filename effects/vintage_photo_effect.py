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


