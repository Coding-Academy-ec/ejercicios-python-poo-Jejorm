# test_ejercicio2.py
import unittest
from ejercicio2 import Perro, Gato

class TestAnimal(unittest.TestCase):
    def test_perro_hacer_sonido(self):
        perro = Perro("Bobby")
        self.assertEqual(perro.hacer_sonido(), "¡Guau!")

    def test_gato_hacer_sonido(self):
        gato = Gato("Garfield")
        self.assertEqual(gato.hacer_sonido(), "¡Miau!")

if __name__ == "__main__":
    unittest.main()
