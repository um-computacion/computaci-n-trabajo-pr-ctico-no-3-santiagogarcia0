import unittest
from unittest.mock import patch
from exceptions import ingrese_numero  # esta función aún no existe, por eso va a fallar

class TestCalculoNumeros(unittest.TestCase):
    @patch('builtins.input', return_value='100')
    def test_ingreso_numero_valido(self, mock_input):
        resultado = ingrese_numero()
        self.assertEqual(resultado, 100)

if __name__ == '__main__':
    unittest.main()
