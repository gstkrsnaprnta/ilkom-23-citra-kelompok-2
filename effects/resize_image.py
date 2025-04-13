import cv2

def resize_image(input_path, output_path, resolution='original', width=None, height=None):
    """
    Mengubah ukuran gambar dan menyimpannya ke lokasi yang ditentukan.

    :param input_path: Path ke gambar input
    :param output_path: Path untuk menyimpan gambar hasil resize
    :param resolution: 'original', 'custom', atau 'half' untuk menentukan mode resize
    :param width: Lebar baru (jika menggunakan 'custom')
    :param height: Tinggi baru (jika menggunakan 'custom')
    """
    try:
        # Membaca gambar dalam mode warna
        image = cv2.imread(input_path, cv2.IMREAD_COLOR)
        if image is None:
            raise FileNotFoundError(f"Gambar tidak ditemukan: {input_path}")

        # Mendapatkan ukuran asli gambar
        original_height, original_width = image.shape[:2]

        # Menentukan ukuran baru berdasarkan parameter
        if resolution == 'original':
            resized_image = image
        elif resolution == 'half':
            resized_image = cv2.resize(image, (original_width // 2, original_height // 2))
        elif resolution == 'custom':
            if width is None or height is None:
                raise ValueError("Lebar dan tinggi harus ditentukan untuk resolusi 'custom'.")
            resized_image = cv2.resize(image, (width, height))
        else:
            raise ValueError("Resolusi tidak dikenali. Gunakan 'original', 'half', atau 'custom'.")

        # Menyimpan gambar hasil resize
        cv2.imwrite(output_path, resized_image)

        # Mengembalikan path hasil sebagai konfirmasi
        return output_path

    except Exception as error:
        raise RuntimeError(f"Gagal mengubah ukuran gambar. Detail: {str(error)}")
