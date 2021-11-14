from SDAMath_exemplu_meu.functii import *

import unittest

class TestSDAMath_ex_meu(unittest.TestCase):
    def test_sum(self):
        result = sum(15, 15)
        self.assertEqual(result, 30)
    def test_sub(self):
        result = sub(17, 15)
        self.assertEqual(result, 5)
    def test_mul(self):
        result = mul(3, 15)
        self.assertEqual(result, 45)
    def test_div(self):
        result = div(15, 15)
        self.assertEqual(result, 2)
    def test_mul(self):
        result = mul(4, 4)
        self.assertNotEqual(result, 2)

if __name__ == "__main__":
    unittest.main()

