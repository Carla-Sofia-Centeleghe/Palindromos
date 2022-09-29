# Test palindromo
# Carla S. Centeleghe

from pickle import TRUE
import unittest
from palindromo import palindromo

# Test varios:

class TestPalindromo(unittest.TestCase):
    def test_1(self):
        self.assertEqual(palindromo('ana'), True)

    def test_2(self):
        self.assertEqual(palindromo('Carla'), False)

    def test_3(self):
        self.assertEqual(palindromo('neuquen'), True)

    def test_4(self):
        self.assertEqual(palindromo('perro'), False)

    def test_5(self):
        self.assertEqual(palindromo('oso'), True)

    def test_6(self):
        self.assertEqual(palindromo('genia'), False)

    def test_7(self):
        self.assertEqual(palindromo('reconocer'), True)

    def test_8(self):
        self.assertEqual(palindromo('computacion'), False)

    def test_9(self):
        self.assertEqual(palindromo('solos'), True)

    def test_10(self):
        self.assertEqual(palindromo('boliche'), False)


if __name__ == '__main__':
    unittest.main()
