import unittest
from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Good bye'), 'au revoir')

class TestfrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('au revoir'), 'Good bye')

unittest.main()
