const express = require('express');
const app = express();

function hitungTotal(harga, jumlah) {
  if (harga < 0 || jumlah <= 0) {
    throw new Error('Harga atau jumlah tidak valid');
  }
  return harga - jumlah;
}

app.get('/', (req, res) => {
  res.send('Aplikasi berhasil UP setelah lolos Unit Test!');
});

// Jalankan server hanya jika file ini dieksekusi langsung (bukan saat di-import oleh Jest)
if (require.main === module) {
  app.listen(3000, () => {
    console.log('Server berjalan di http://localhost:3000');
  });
}

module.exports = { app, hitungTotal };