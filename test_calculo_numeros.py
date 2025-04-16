import unittest
from unittest.mock import patch

# Comentamos la importación que todavía no existe
# from exceptions import ingrese_numero, NumeroDebeSerPositivo

class NumeroDebeSerPositivo(Exception):
    """Excepción temporal simulada para que el código sea ejecutable (luego se reemplaza)."""
    pass

def ingrese_numero():
    """Función temporal vacía para que los tests fallen de forma controlada."""
    pass

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='-100')
    def test_ingreso_negativo(self, patch_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

    @patch('builtins.input', return_value='ABC')
    def test_ingreso_letras(self, patch_input):
        with self.assertRaises(ValueError):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()
