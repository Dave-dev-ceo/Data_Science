import unittest

def suma(num1, num2):
    return num1 + num2

class CajaNegraTest(unittest.TestCase):

     def test_suma_dos_positivos(self):
         num_1 = 10
         num_2 = 3
         resultado = suma(num_1, num_2)

         self.assertEqual(resultado, 13)
    
     def test_sumar_dos_negativos(self):
        num_1 = -3
        num_2 = -3
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado,-6)
if __name__ == '__main__':
    unittest.main()