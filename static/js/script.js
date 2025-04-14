/*
  JavaScript untuk Sketchify: Mengatur interaksi pengguna di halaman utama.
  Menangani unggah gambar, drag-and-drop, pilihan efek, resolusi, dan tampilan hasil.
*/

// Tunggu hingga halaman selesai dimuat
document.addEventListener('DOMContentLoaded', () => {
    // Ambil elemen dari halaman
    const uploadArea = document.getElementById('upload-area');
    const fileInput = document.getElementById('file-input');
    const uploadButton = document.getElementById('upload-button');
    const resultArea = document.getElementById('result-area');
    const originalImage = document.getElementById('original-image');
    const resultImage = document.getElementById('result-image');
    const downloadLink = document.getElementById('download-link');
    const messageText = document.getElementById('message-text');
    const resolutionSelect = document.getElementById('resolution');
    const customResDiv = document.getElementById('custom-res');
    const widthInput = document.getElementById('width');
    const heightInput = document.getElementById('height');

    // Tampilkan input resolusi custom saat memilih 'custom'
    resolutionSelect.addEventListener('change', () => {
        customResDiv.classList.toggle('hidden', resolutionSelect.value !== 'custom');
    });

    // Klik tombol unggah untuk memilih file
    uploadButton.addEventListener('click', () => {
        fileInput.click();
    });
