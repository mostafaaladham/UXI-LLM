import unittest
from uxi.utils import normalize_text, tokenize

class TestUtils(unittest.TestCase):
    def test_normalize_text(self):
        input_text = "Hello, WORLD!  "
        expected = "hello, world!"
        self.assertEqual(normalize_text(input_text), expected)

    def test_tokenize(self):
        input_text = "This is a test."
        tokens = tokenize(input_text)
        self.assertIsInstance(tokens, list)
        self.assertIn("test", tokens)

if __name__ == "__main__":
    unittest.main()
