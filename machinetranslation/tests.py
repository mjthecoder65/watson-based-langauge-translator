import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_null_input_text(self):
        self.assertRaises(ValueError, english_to_french, None)
    def test_correct_input_text(self):
        english_text="Hello"
        text = english_to_french(english_text)
        self.assertEqual(text, "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test_null_input_text(self):
        self.assertRaises(ValueError, french_to_english, None)
    def test_correct_input_text(self):
        french_text="Bonjour"
        text = french_to_english(french_text)
        self.assertEqual(text, "Hello")

if __name__ == '__main__':
    unittest.main()