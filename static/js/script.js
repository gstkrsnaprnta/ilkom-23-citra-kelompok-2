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

    // Tangani drag-and-drop gambar
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault(); // Cegah browser membuka file
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            processFile(files[0]);
        }
    });

    // Tangani pemilihan file dari tombol atau drag
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            processFile(fileInput.files[0]);
        }
    });

     // Fungsi untuk memproses file yang diunggah
    function processFile(file) {
        // Validasi tipe file (hanya gambar)
        if (!file.type.startsWith('image/')) {
            messageText.textContent = 'Harap unggah file gambar (JPEG, PNG, dll.).';
            resultArea.classList.add('hidden');
            return;
        }

        // Siapkan data untuk dikirim ke server
        const formData = new FormData();
        formData.append('file', file);
        formData.append('conversion_type', document.getElementById('conversion-type').value);
        const resolution = resolutionSelect.value;
        formData.append('resolution', resolution);

        // Validasi dan tambahkan ukuran custom jika diperlukan
        if (resolution === 'custom') {
            const width = parseInt(widthInput.value);

      
