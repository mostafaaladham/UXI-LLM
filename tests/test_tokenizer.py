# tests/test_tokenizer.py

import unittest
from utils.tokenizer import SimpleTokenizer

class TestSimpleTokenizer(unittest.TestCase):

    def setUp(self):
        self.tokenizer = SimpleTokenizer()

    def test_tokenize_basic(self):
        text = "Hello, world!"
        tokens = self.tokenizer.tokenize(text)
        self.assertEqual(tokens, ["Hello", ",", "world", "!"])

    def test_detokenize_basic(self):
        tokens = ["Hello", ",", "world", "!"]
        text = self.tokenizer.detokenize(tokens)
        self.assertEqual(text, "Hello, world!")

    def test_tokenize_empty(self):
        self.assertEqual(self.tokenizer.tokenize(""), [])

if __name__ == "__main__":
    unittest.main()
