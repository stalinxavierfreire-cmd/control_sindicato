import unittest
from src.validators import validar_dni, validar_email, validar_telefono

class TestValidadores(unittest.TestCase):
    def test_dni(self):
        self.assertTrue(validar_dni("12345678"))
        self.assertFalse(validar_dni("1234"))
        self.assertFalse(validar_dni("abcdefgh"))

    def test_email(self):
        self.assertTrue(validar_email("test@example.com"))
        self.assertFalse(validar_email("bad@com"))
        self.assertFalse(validar_email("sinarroba.com"))

    def test_telefono(self):
        self.assertTrue(validar_telefono("987654321"))
        self.assertFalse(validar_telefono("123"))

if __name__ == '__main__':
    unittest.main()