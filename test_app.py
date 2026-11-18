import unittest

def cek_status_versi():
    return "v1.0"

class TestAplikasi(unittest.TestCase):
    def test_versi(self):
        self.assertEqual(cek_status_versi(), "v1.0")

if __name__ == "__main__":
    unittest.main()