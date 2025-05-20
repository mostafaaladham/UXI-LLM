# core/tokenizer.py

import sentencepiece as spm

class UXITokenizer:
    def __init__(self, model_file, add_special_tokens=True):
        self.sp = spm.SentencePieceProcessor()
        self.sp.load(model_file)
        self.add_special_tokens = add_special_tokens

        # Define special token IDs
        self.pad_token_id = self.sp.piece_to_id("<pad>") if self.sp.piece_to_id("<pad>") != -1 else 0
        self.unk_token_id = self.sp.piece_to_id("<unk>") if self.sp.piece_to_id("<unk>") != -1 else 1

    def encode(self, text):
        ids = self.sp.encode(text, out_type=int)
        if self.add_special_tokens:
            ids = [self.pad_token_id] + ids + [self.pad_token_id]
        return ids

    def decode(self, ids):
        return self.sp.decode(ids)

    def tokenize(self, text):
        return self.sp.encode(text, out_type=str)

    def detokenize(self, tokens):
        return self.sp.decode_pieces(tokens)

    def vocab_size(self):
        return self.sp.get_piece_size()

    def pad_id(self):
        return self.pad_token_id

    def unk_id(self):
        return self.unk_token_id
