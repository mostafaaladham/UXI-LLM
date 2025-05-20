import torch
from torch.utils.data import DataLoader
from transformers import AdamW
from typing import Optional

class FineTuner:
    def __init__(self, model):
        self.model = model.model
        self.tokenizer = model.tokenizer
        self.optimizer = AdamW(self.model.parameters(), lr=5e-5)
        self.dataset = None
        self.dataloader = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def load_dataset(self, file_path: str):
        # Simple JSONL dataset loader, expects each line to have 'text' field
        import json
        data = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                item = json.loads(line)
                data.append(item['text'])
        self.dataset = data
        self.dataloader = DataLoader(data, batch_size=8, shuffle=True)

    def train(self, epochs: int = 1, batch_size: int = 8):
        self.model.train()
        self.dataloader = DataLoader(self.dataset, batch_size=batch_size, shuffle=True)
        for epoch in range(epochs):
            for batch in self.dataloader:
                inputs = self.tokenizer(batch, return_tensors="pt", padding=True, truncation=True)
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                outputs = self.model(**inputs, labels=inputs["input_ids"])
                loss = outputs.loss
                loss.backward()
                self.optimizer.step()
                self.optimizer.zero_grad()

    def save_checkpoint(self, path: str):
        torch.save(self.model.state_dict(), path)

    def load_checkpoint(self, path: str):
        self.model.load_state_dict(torch.load(path, map_location=self.device))
