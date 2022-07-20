import unittest
from translator import english_to_french
from translator import french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french(0), 0)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')

class TestfrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertNotEqual(french_to_english(0), 0)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')

unittest.main()
