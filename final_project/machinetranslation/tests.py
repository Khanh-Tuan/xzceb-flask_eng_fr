import unittest
from translator import english_to_french
from translator import french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Null'), 'Null')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Good bye'), 'Au revoir')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestfrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('Null'), 'Null')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Good bye')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()