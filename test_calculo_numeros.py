import unittest
from unittest.mock import patch
from exceptions import ingrese_numero, NumeroDebeSerPositivo 

class TestCalculoNumeros(unittest.TestCase):

    @patch('builtins.input', return_value='100')
    def test_ingreso_numero_valido(self, mock_input):
        resultado = ingrese_numero()
        self.assertEqual(resultado, 100)

    @patch('builtins.input', return_value='-100')
    def test_ingreso_numero_negativo(self, mock_input):
        with self.assertRaises(NumeroDebeSerPositivo):
            ingrese_numero()

if __name__ == '__main__':
    unittest.main()
