from flask import Flask, request, render_template, jsonify, send_file
import os
from time import time
import logging

# Impor fungsi efek dari modul yang sudah diperbarui
from effects.monochrome_effect import convert_to_grayscale
from effects.line_art_effect import convert_to_line_art
from effects.toon_style_effect import convert_to_toon_style  
from effects.ink_blot_effect import convert_to_ink_blot
from effects.art_sketch_effect import convert_to_art_sketch
from effects.vintage_photo_effect import convert_to_vintage_photo
from effects.resize_image import resize_image

"""
Aplikasi web Sketchify untuk mengubah gambar dengan efek seni seperti sketsa, komik, dan lukisan.
Menerima unggahan gambar, menerapkan efek, dan menyediakan hasil untuk diunduh.
"""
# Mengatur logging untuk membantu menemukan masalah
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Inisialisasi aplikasi Flask
app = Flask(__name__, static_folder='static', template_folder='templates')

# Menentukan folder untuk menyimpan gambar yang diunggah dan hasil efek
UPLOAD_FOLDER = 'static/uploads'
OUTPUT_FOLDER = 'static/outputs'

# Membuat folder jika belum ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Peta efek: menghubungkan jenis efek dengan fungsi yang sesuai
EFFECTS = {
    'monochrome_glow': convert_to_grayscale,
    'line_art': convert_to_line_art,
    'toon_style': convert_to_toon_style,
    'ink_blot': convert_to_ink_blot,
    'art_sketch': convert_to_art_sketch,
    'vintage_photo': convert_to_vintage_photo,
}

@app.route('/')
def index():
    """
    Menampilkan halaman utama aplikasi (index.html).
    """
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():

    """
    Menerima gambar yang diunggah, menerapkan efek seni, dan menghasilkan gambar hasil.
    Mengembalikan URL untuk menampilkan dan mengunduh hasil.
    """
    # Memeriksa apakah ada file dalam unggahan
    if 'file' not in request.files:
        return jsonify({'error': 'Tidak ada file yang diunggah'}), 400
    
    file = request.files['file']

    # Memeriksa apakah nama file tidak kosong
    if file.filename == '':
        return jsonify({'error': 'Tidak ada file yang dipilih'}), 400

    # Memeriksa jenis file yang diizinkan (jpg, jpeg, png)
    allowed_extensions = {'.jpg', '.jpeg', '.png'}
    if not os.path.splitext(file.filename)[1].lower() in allowed_extensions:
        return jsonify({'error': 'Jenis file tidak valid. Hanya JPG, JPEG, dan PNG yang diizinkan.'}), 400

    # Membuat nama file unik untuk gambar yang diunggah
    input_filename = f"input_{int(time())}_{file.filename}"
    input_path = os.path.join(UPLOAD_FOLDER, input_filename)

    # Mendapatkan jenis efek, resolusi, dan ukuran dari formulir
    conversion_type = request.form.get('conversion_type', 'monochrome_glow')
    resolution = request.form.get('resolution', 'original')
    width = request.form.get('width')
    height = request.form.get('height')