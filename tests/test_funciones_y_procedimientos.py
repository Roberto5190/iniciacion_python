import unittest
import sys
import os

# Añadir el directorio raíz al path para permitir las importaciones
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from funciones_y_procedimientos import suma

class TestFuncionesYProcedimientos(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -3), -5)

    def test_suma_mixtos(self):
        self.assertEqual(suma(-2, 3), 1)

if __name__ == '__main__':
    unittest.main()