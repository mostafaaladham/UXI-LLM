# tokenizer/custom_tokenizer.py

from transformers import PreTrainedTokenizerFast

class CustomTokenizer:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained(model_name)

    def encode(self, text, max_length=512, truncation=True):
        return self.tokenizer.encode(text, max_length=max_length, truncation=truncation)

    def decode(self, tokens):
        return self.tokenizer.decode(tokens)

    def tokenize(self, text):
        return self.tokenizer.tokenize(text)

    def pad(self, encoded_inputs, padding=True, max_length=None):
        return self.tokenizer.pad(
            encoded_inputs,
            padding=padding,
            max_length=max_length,
            return_tensors="pt"
        )
