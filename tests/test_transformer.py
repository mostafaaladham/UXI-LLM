# tests/test_transformer.py

import unittest
import torch
from models.transformer import TransformerModel

class TestTransformerModel(unittest.TestCase):

    def setUp(self):
        self.model = TransformerModel(
            vocab_size=100,
            d_model=32,
            nhead=4,
            num_layers=2,
            dim_feedforward=64,
            dropout=0.1
        )

    def test_forward_shape(self):
        input_tensor = torch.randint(0, 100, (10, 5))  # seq_len=10, batch_size=5
        output = self.model(input_tensor)
        self.assertEqual(output.shape, (10, 5, 100))

if __name__ == "__main__":
    unittest.main()
