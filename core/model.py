# core/model.py

import torch
import torch.nn as nn
from .layers import MultiHeadAttention, FeedForwardNetwork

class UXIHybridModel(nn.Module):
    def __init__(self, config):
        super(UXIHybridModel, self).__init__()
        self.vocab_size = config["model"]["vocab_size"]
        self.hidden_size = config["model"]["hidden_size"]
        self.max_pos = config["model"]["max_position_embeddings"]
        self.num_layers = config["model"]["num_layers"]
        self.dropout_rate = config["model"]["dropout"]

        self.token_embeddings = nn.Embedding(self.vocab_size, self.hidden_size)
        self.position_embeddings = nn.Embedding(self.max_pos, self.hidden_size)
        self.dropout = nn.Dropout(self.dropout_rate)

        self.encoder_layers = nn.ModuleList([
            nn.TransformerEncoderLayer(
                d_model=self.hidden_size,
                nhead=config["model"]["num_heads"],
                dim_feedforward=self.hidden_size * 4,
                dropout=self.dropout_rate,
                activation='gelu',
                batch_first=True
            ) for _ in range(self.num_layers)
        ])

        self.norm = nn.LayerNorm(self.hidden_size)
        self.output_layer = nn.Linear(self.hidden_size, self.vocab_size)

    def forward(self, input_ids):
        seq_length = input_ids.size(1)
        position_ids = torch.arange(0, seq_length, dtype=torch.long, device=input_ids.device)
        position_ids = position_ids.unsqueeze(0).expand_as(input_ids)

        token_embed = self.token_embeddings(input_ids)
        position_embed = self.position_embeddings(position_ids)

        x = self.dropout(token_embed + position_embed)

        for layer in self.encoder_layers:
            x = layer(x)

        x = self.norm(x)
        logits = self.output_layer(x)
        return logits
