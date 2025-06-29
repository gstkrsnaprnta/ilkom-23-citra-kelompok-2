# effects/art_sketch_effect.py
import numpy as np
import cv2 # Diperlukan hanya untuk membaca dan menyimpan gambar (I/O)

def convert_to_art_sketch(input_path, output_path):
    """
    Mengubah gambar menjadi gaya sketsa seni dengan garis lembut dan detail halus.
    Ini adalah versi yang sangat detail untuk tujuan penjelasan perhitungan matematis
    pada papan tulis, menggunakan loop Python eksplisit untuk setiap operasi piksel.

    Args:
        input_path (str): Lokasi file gambar yang akan diubah (misalnya, 'foto.jpg').
        output_path (str): Lokasi untuk menyimpan hasil gambar sketsa.

    Returns:
        str: Lokasi file hasil (output_path).

    Raises:
        ValueError: Jika gambar gagal dimuat atau ada kesalahan saat memproses.
    """
    try:
        # --- 1. Membaca Gambar (Input/Output menggunakan OpenCV) ---
        # Gambar dibaca sebagai array NumPy 3D (Tinggi x Lebar x Saluran), BGR.
        image = cv2.imread(input_path)
        
        if image is None:
            raise ValueError("Gagal memuat gambar. Pastikan file ada dan tidak rusak.")
        
        rows, cols, _ = image.shape # Dapatkan dimensi gambar (tinggi dan lebar)

        # --- 2. Mengubah Gambar ke Skala Abu-abu (Grayscale) ---
        # Konsep: Rata-rata berbobot dari saluran BGR.
        # Rumus: Gray = 0.299 * R + 0.587 * G + 0.114 * B
        # Setiap piksel [B, G, R] diubah menjadi 1 nilai Gray.
        
        gray = np.zeros((rows, cols), dtype=np.uint8) # Inisialisasi matriks abu-abu kosong (hanya 2D)
        
        for r in range(rows):
            for c in range(cols):
                b = image[r, c, 0] # Ambil nilai Biru dari piksel (r, c)
                g = image[r, c, 1] # Ambil nilai Hijau
                red = image[r, c, 2] # Ambil nilai Merah
                
                # Perhitungan Gray Scale (detail): Perkalian dan Penjumlahan
                gray_val = (0.299 * red) + (0.587 * g) + (0.114 * b)
                
                # Pembatasan (Clipping) nilai ke rentang 0-255 dan konversi ke integer (uint8)
                if gray_val < 0:
                    gray[r, c] = 0
                elif gray_val > 255:
                    gray[r, c] = 255
                else:
                    gray[r, c] = int(gray_val) # Pembulatan otomatis saat konversi int

        # --- 3. Menghaluskan Gambar dengan Gaussian Blur ---
        # Konsep: Konvolusi dengan Kernel Gaussian (matriks bobot berbentuk lonceng).
        # Setiap piksel baru adalah rata-rata berbobot dari tetangganya.
        
        # Mendefinisikan Kernel Gaussian 5x5 secara manual (nilai perkiraan untuk ilustrasi).
        # Kernel ini dinormalisasi sehingga jumlah semua elemennya adalah 1.
        gaussian_kernel = np.array([
            [1,  4,  7,  4, 1],
            [4, 16, 26, 16, 4],
            [7, 26, 41, 26, 7],
            [4, 16, 26, 16, 4],
            [1,  4,  7,  4, 1]
        ], dtype=np.float32)
        gaussian_kernel_sum = np.sum(gaussian_kernel)
        
        k_size = gaussian_kernel.shape[0] # Ukuran kernel (misal 5)
        pad_amount = k_size // 2 # Jumlah padding yang diperlukan di setiap sisi (2 untuk 5x5)

        # Menambahkan padding ke gambar abu-abu.
        # Mode 'reflect' merefleksikan nilai piksel di tepi (umum di pemrosesan gambar).
        padded_gray_for_blur = np.pad(gray, pad_amount, mode='reflect')
        
        blurred = np.zeros_like(gray, dtype=np.float32) # Inisialisasi matriks hasil blur (float untuk perhitungan)

        # Lakukan Konvolusi (looping eksplisit piksel demi piksel):
        for r in range(rows):
            for c in range(cols):
                # Ekstrak 'jendela' piksel (area yang ditutupi kernel) dari gambar yang dipad.
                # Ukuran jendela = ukuran kernel (misal 5x5).
                window = padded_gray_for_blur[r : r + k_size, c : c + k_size]
                
                # Lakukan perkalian elemen-demi-elemen antara jendela dan kernel, lalu jumlahkan.
                # Inilah inti dari operasi konvolusi.
                sum_weighted_pixels = 0.0
                for i in range(k_size):
                    for j in range(k_size):
                        sum_weighted_pixels += window[i, j] * (gaussian_kernel[i, j] / gaussian_kernel_sum)
                
                blurred[r, c] = sum_weighted_pixels
        
        # Pembatasan (Clipping) nilai ke rentang 0-255 dan konversi ke integer (uint8)
        blurred_final = np.zeros_like(gray, dtype=np.uint8)
        for r in range(rows):
            for c in range(cols):
                if blurred[r, c] < 0:
                    blurred_final[r, c] = 0
                elif blurred[r, c] > 255:
                    blurred_final[r, c] = 255
                else:
                    blurred_final[r, c] = int(blurred[r, c]) # Pembulatan

        # --- 4. Membuat Garis Sketsa dengan Deteksi Tepi Sobel ---
        # Konsep: Konvolusi dengan Kernel Sobel X dan Y untuk menghitung gradien (perubahan intensitas).
        # Gradien mengukur 'kemiringan' atau 'perubahan' intensitas di gambar.
        
        # Mendefinisikan Kernel Sobel X dan Y (3x3)
        sobel_x_kernel = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ], dtype=np.float32)

        sobel_y_kernel = np.array([
            [-1, -2, -1],
            [ 0,  0,  0],
            [ 1,  2,  1]
        ], dtype=np.float32)

        k_sobel_size = 3 # Ukuran kernel Sobel
        pad_sobel = k_sobel_size // 2

        # Menambahkan padding ke gambar 'blurred_final' untuk operasi Sobel.
        padded_blurred_for_sobel = np.pad(blurred_final, pad_sobel, mode='reflect')
        
        sobelx = np.zeros_like(blurred_final, dtype=np.float32) # Untuk menyimpan gradien X
        sobely = np.zeros_like(blurred_final, dtype=np.float32) # Untuk menyimpan gradien Y

        # Lakukan Konvolusi untuk Sobel X dan Y (looping eksplisit piksel demi piksel):
        for r in range(rows):
            for c in range(cols):
                window_sobel = padded_blurred_for_sobel[r : r + k_sobel_size, c : c + k_sobel_size]
                
                # Perhitungan sobelx (detail):
                sum_sobelx = 0.0
                for i in range(k_sobel_size):
                    for j in range(k_sobel_size):
                        sum_sobelx += window_sobel[i, j] * sobel_x_kernel[i, j]
                sobelx[r, c] = sum_sobelx

                # Perhitungan sobely (detail):
                sum_sobely = 0.0
                for i in range(k_sobel_size):
                    for j in range(k_sobel_size):
                        sum_sobely += window_sobel[i, j] * sobel_y_kernel[i, j]
                sobely[r, c] = sum_sobely

        # Menghitung Magnitudo Gradien (Kekuatan Tepi)
        # Konsep Matematika: Menggunakan Teorema Pythagoras: edges = sqrt(sobelx^2 + sobely^2)
        edges = np.zeros_like(blurred_final, dtype=np.float32) # Hasil edges bisa float
        for r in range(rows):
            for c in range(cols):
                # Perhitungan magnitudo (detail): Kuadrat, Penjumlahan, Akar Kuadrat
                edges[r, c] = np.sqrt(sobelx[r, c]**2 + sobely[r, c]**2)

        # --- 5. Normalisasi Tepi ---
        # Konsep: Penskalaan nilai 'edges' (yang bisa sangat bervariasi) ke rentang 0-255.
        
        min_val_edges = float('inf') # Inisialisasi min dengan nilai sangat besar
        max_val_edges = float('-inf') # Inisialisasi max dengan nilai sangat kecil

        # Mencari nilai min dan max secara eksplisit
        for r in range(rows):
            for c in range(cols):
                if edges[r, c] < min_val_edges:
                    min_val_edges = edges[r, c]
                if edges[r, c] > max_val_edges:
                    max_val_edges = edges[r, c]

        edges_normalized = np.zeros_like(edges, dtype=np.uint8)

        if (max_val_edges - min_val_edges) == 0: # Hindari pembagian dengan nol
            # Jika semua nilai sama, jadikan hitam (atau 0)
            for r in range(rows):
                for c in range(cols):
                    edges_normalized[r, c] = 0
        else:
            # Rumus Normalisasi Min-Max (detail):
            # Output = (Input - Min) / (Max - Min) * (NewMax - NewMin) + NewMin
            new_min = 0
            new_max = 255
            range_input = max_val_edges - min_val_edges
            range_output = new_max - new_min

            for r in range(rows):
                for c in range(cols):
                    # Perhitungan normalisasi (detail): Pengurangan, Pembagian, Perkalian, Penjumlahan
                    val_normalized_float = ((edges[r, c] - min_val_edges) / range_input) * range_output + new_min
                    
                    # Pembatasan (Clipping) dan konversi ke integer (uint8)
                    if val_normalized_float < 0:
                        edges_normalized[r, c] = 0
                    elif val_normalized_float > 255:
                        edges_normalized[r, c] = 255
                    else:
                        edges_normalized[r, c] = int(val_normalized_float)


        # --- 6. Membalik Garis (Inversi) ---
        # Konsep: Mengubah intensitas piksel. Piksel terang jadi gelap, gelap jadi terang.
        # Ini membuat garis sketsa terlihat 'terang' atau 'putih' (karena 255 - gelap = terang).
        
        inverted_edges = np.zeros_like(edges_normalized, dtype=np.uint8)
        for r in range(rows):
            for c in range(cols):
                # Perhitungan inversi (detail): Pengurangan dari 255
                inverted_edges[r, c] = 255 - edges_normalized[r, c]

        # --- 7. Menggabungkan Garis Sketsa dengan Detail Gambar Asli ---
        # Konsep: Penjumlahan Berbobot Linear (Weighted Sum).
        # sketch = alpha * inverted_edges + beta * gray + gamma
        
        alpha = 0.8 # Bobot untuk garis yang diinvert (lebih dominan)
        beta = 0.2  # Bobot untuk gambar abu-abu asli (untuk detail halus)
        gamma = 0   # Offset konstan (tidak ada di sini)

        sketch_float = np.zeros_like(gray, dtype=np.float32) # Hasil bisa float
        
        for r in range(rows):
            for c in range(cols):
                # Perhitungan penjumlahan berbobot (detail): Perkalian dan Penjumlahan
                weighted_val = (inverted_edges[r, c].astype(np.float32) * alpha) + \
                               (gray[r, c].astype(np.float32) * beta) + \
                               gamma
                sketch_float[r, c] = weighted_val
        
        # Pembatasan (Clipping) nilai ke rentang 0-255 dan konversi ke uint8
        sketch = np.zeros_like(gray, dtype=np.uint8)
        for r in range(rows):
            for c in range(cols):
                if sketch_float[r, c] < 0:
                    sketch[r, c] = 0
                elif sketch_float[r, c] > 255:
                    sketch[r, c] = 255
                else:
                    sketch[r, c] = int(sketch_float[r, c])

        # --- 8. Mengubah Format ke BGR (untuk penyimpanan) ---
        # Konsep: Replikasi saluran tunggal (abu-abu) ke tiga saluran BGR.
        # Setiap nilai piksel abu-abu disalin ke saluran Biru, Hijau, dan Merah.
        
        sketch_bgr = np.zeros((rows, cols, 3), dtype=np.uint8)
        for r in range(rows):
            for c in range(cols):
                # Perhitungan replikasi (detail): Menetapkan nilai yang sama ke semua saluran
                sketch_bgr[r, c, 0] = sketch[r, c] # Saluran Biru
                sketch_bgr[r, c, 1] = sketch[r, c] # Saluran Hijau
                sketch_bgr[r, c, 2] = sketch[r, c] # Saluran Merah

        # --- 9. Menyimpan Hasil Gambar Sketsa (Output menggunakan OpenCV) ---
        cv2.imwrite(output_path, sketch_bgr)
        
        return output_path
    
    except Exception as e:
        raise ValueError(f"Kesalahan saat membuat sketsa seni: {str(e)}")

