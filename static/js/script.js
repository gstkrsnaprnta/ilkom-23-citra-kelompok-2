/*
  JavaScript untuk Sketchify: Mengatur interaksi pengguna di halaman utama.
  Menangani unggah gambar, drag-and-drop, pilihan efek, resolusi, dan tampilan hasil.
*/

// Tunggu hingga halaman selesai dimuat
document.addEventListener('DOMContentLoaded', () => {
    // Ambil elemen dari halaman
    const uploadArea = document.getElementById('upload-area');
    const fileInput = document.getElementById('file-input');
