import unittest

from src.main.kata.romannumeral.Main import Roman


class TestRoman(unittest.TestCase):

    #test uniques
    def test_uniques(self):
        sut = Roman()
        self.assertEqual(sut.convert(1), "I")
        self.assertEqual(sut.convert(4), "IV")
        self.assertEqual(sut.convert(5), "V")
        self.assertEqual(sut.convert(9), "IX")
        self.assertEqual(sut.convert(10), "X")
        self.assertEqual(sut.convert(40), "XL")
        self.assertEqual(sut.convert(50), "L")
        self.assertEqual(sut.convert(90), "XC")
        self.assertEqual(sut.convert(100), "C")
        self.assertEqual(sut.convert(400), "CD")
        self.assertEqual(sut.convert(500), "D")
        self.assertEqual(sut.convert(900), "CM")
        self.assertEqual(sut.convert(1000), "M")

    def test_17(self):
        sut = Roman()
        self.assertEqual(sut.convert(17), "XVII")

    def test_285(self):
        sut = Roman()
        self.assertEqual(sut.convert(285), "CCLXXXV")

    def test_2012(self):
        sut = Roman()
        self.assertEqual(sut.convert(2012), "MMXII")

    def test_1996(self):
        sut = Roman()
        self.assertEqual(sut.convert(1996), "MCMXCVI")

    def test_negative(self):
        sut = Roman()
        self.assertEquals(sut.convert(-1), "invalid input")