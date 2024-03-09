import unittest
from ejercicio1 import Coche

class TestCoche(unittest.TestCase):
    def test_conducir(self):
        coche = Coche("Toyota", "Corolla")
        resultado = coche.conducir()
        self.assertEqual(resultado, "Conduciendo el Toyota Corolla")

if __name__ == "__main__":
    unittest.main()