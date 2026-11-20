const { hitungTotal } = require('./app');

test('Menghitung total belanja dengan benar (10.000 x 3 = 30.000)', () => {
  expect(hitungTotal(10000, 3)).toBe(30000);
});

test('Gagal jika jumlah barang 0 atau negatif', () => {
  expect(() => hitungTotal(10000, 0)).toThrow('Harga atau jumlah tidak valid');
});