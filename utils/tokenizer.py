# utils/tokenizer.py

import re

class SimpleTokenizer:
    """
    A simple whitespace and punctuation tokenizer.
    """

    def __init__(self):
        self.pattern = re.compile(r"\w+|[^\w\s]", re.UNICODE)

    def tokenize(self, text):
        return self.pattern.findall(text)

    def detokenize(self, tokens):
        return ' '.join(tokens).replace(" .", ".").replace(" ,", ",")
