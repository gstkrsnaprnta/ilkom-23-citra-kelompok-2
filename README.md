# 🎨 ILKOM-23 Citra - Aplikasi Web Efek Gambar

Ini adalah proyek aplikasi web sederhana yang dibangun dengan **Python** menggunakan framework **Flask**, bertujuan untuk memproses gambar dengan berbagai **efek citra digital** seperti sketsa, kartun, vintage, hitam putih, dan lainnya. Aplikasi ini dapat diakses melalui browser, di mana pengguna bisa mengunggah gambar dan langsung melihat hasil efeknya.

Proyek ini merupakan bagian dari tugas mata kuliah **Pengolahan Citra Digital** pada program studi **Ilmu Komputer Universitas Halu Oleo (ILKOM-23)**.

---

## ✅ Fitur Aplikasi

- Upload gambar dari komputer pengguna.
- Pilih dan terapkan salah satu dari 7 efek citra digital.
- Lihat hasil gambar yang telah diolah langsung di halaman web.
- Struktur kode rapi dan modular, memudahkan pengembangan lanjutan.

---

## 🎨 Daftar Efek Gambar

Semua efek dibuat dalam file Python yang berbeda di folder `effects/`, berikut adalah efek-efek yang tersedia:

- `art_sketch_effect.py` → Efek sketsa artistik
- `ink_blot_effect.py` → Efek tinta atau noda
- `line_art_effect.py` → Efek garis hitam putih
- `monochrome_effect.py` → Efek hitam putih klasik
- `resize_image.py` → Mengubah ukuran gambar
- `toon_style_effect.py` → Efek gaya kartun
- `vintage_photo_effect.py` → Efek foto gaya vintage

---

## 📁 Struktur Folder Proyek
ILKOM-23-CITRA/
├── effects/                  # Folder berisi efek-efek gambar (.py)
│   ├── art_sketch_effect.py
│   ├── ink_blot_effect.py
│   ├── line_art_effect.py
│   ├── monochrome_effect.py
│   ├── resize_image.py
│   ├── toon_style_effect.py
│   └── vintage_photo_effect.py
│
├── static/                   # Folder untuk file front-end (style & script)
│   ├── css/
│   │   └── style.css         # Gaya tampilan halaman
│   └── js/
│       └── script.js         # Interaksi JavaScript (jika digunakan)
│
├── templates/
│   └── index.html            # Halaman utama HTML (template Flask)
│
├── app.py                    # File utama yang menjalankan aplikasi Flask
├── requirements.txt          # Daftar pustaka Python yang dibutuhkan
└── .gitignore                # Mengabaikan file tertentu dari Git


---

## ⚙️ Cara Menjalankan Aplikasi

Berikut langkah-langkah agar kamu bisa menjalankan aplikasi ini di laptopmu:

### 1. **Pastikan Python sudah terinstall**

Ketik perintah berikut untuk memastikan:
```bash
python --version

2. Buka Terminal dan Pindah ke Folder Proyek

cd ILKOM-23-CITRA

3. (Opsional) Buat Virtual Environment

python -m venv venv
venv\Scripts\activate       # Jika di Windows
source venv/bin/activate   # Jika di Linux/macOS

4. Install Semua Pustaka

pip install -r requirements.txt

5. Jalankan Aplikasinya

python app.py

6. Buka Browser dan Akses

http://127.0.0.1:5000
