"""Despre testare"""

"""
- nucleul testatii este "assert", aci se evalueaza conditia de credibilitate
- toate asert-urile trebuie sa existe in functii, ce incep cu test_*
- toate functiile trebuie sa existe intr-o clasa ce mosteneste unittest.TestCase
- permite rularea direct din IDE
"""
import unittest
import sys


class TestExample(unittest.TestCase):

    @unittest.skypIf(sys.version_info.major < 3, "Aveti Python 3")
    def test_include1(self):
        self.assertIn("S", "SDAAcademy")

    def test_egalitate(self):
        result = 5 + 5
        self.assertEqual(result, 10)

        """sintaxa specifica Python - entry point: - se pune tot timpul la final si se foloseste doar la teste"""


if __name__ == "__main__":
    unittest.main()


class Chicken:
    def __init__(self, breed, size, colour):
        self.breed = breed
        self.size = size
        self.colour = colour
    def get_breed(self):
        return self.breed
class Benefit:
    def __init__(self, breed, max_no_eggs):
        self.breed = breed
        self.max_no_eggs = max_no_eggs
        self.eggs = []
    def get_profit(self):
        self.breed = breed
        self.max_no_eggs = max_no_eggs

class Medicine:
    def __init__(self, clasica, alternativa):
        self.clasica = clasica
        self.alternativa = alternativa
    def chirurgie(self):
        return(f"Tipul medicinei studiat este {self.alternativa}")
    def set_importance(self):
        self.alterntiva = "actuala"

incizia = Medicine("ortopedie", "kiropractor")
incizia.chirurgie()

