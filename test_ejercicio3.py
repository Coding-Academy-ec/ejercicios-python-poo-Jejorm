import unittest
from ejercicio3 import Circulo

class TestCirculo(unittest.TestCase):
    def test_calcular_area(self):
        circulo = Circulo(3)
        self.assertEqual(circulo.calcular_area(), 28.26)

if __name__ == "__main__":
    unittest.main()
