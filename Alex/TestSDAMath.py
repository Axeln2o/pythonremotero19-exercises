
from SDAMath.functii import *  ## Aici importam din PythonPackage (Folder) - ul SDAMath, tot ceea ce exita in fsierul functii.py
                                ## am folosit `*` pentru a importa toate functiile din SDAMath, altfel trebuia sa scriem pentru fiecare functie in parte

import unittest  ##cred ca scriem asta tot la fel ca ceva standard


print(sum(23, 34))  ## asta am facut doar de verificare, sa vedem ca daca ii dam print chiar va da un rezultat
print(divide(23, 24))

class TestSDAMath(unittest.TestCase):  ## Acest lucru se scrie standard. Aceasta este o clasa de testare si doar de testare, de asta folosim unittest.TestCase
    def test_sum(self):
        result = sum(23, 34)
        self.assertEqual(result, 57)
    def test_divide(self):
        result = divide(45, 12)
        self.assertEqual(result, 45)
    def test_multiply(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)
    def test_substract(self):
        result = substract(4, 2)
        self.assertEqual(result, 2)
    def test_substracterror(self):
        result = substract(4, 3)
        self.assertNotEqual(result, 2)



if __name__ == "__main__":   ##Acest lucru se scrie standard cand facem aceasta testare
    unittest.main()