# training/trainer.py

import torch
from torch.utils.data import DataLoader

class Trainer:
    def __init__(self, model, optimizer, scheduler, tokenizer, device):
        self.model = model.to(device)
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.tokenizer = tokenizer
        self.device = device

    def train_epoch(self, train_dataset, batch_size=32):
        self.model.train()
        dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        total_loss = 0
        for batch in dataloader:
            inputs = batch["input_ids"].to(self.device)
            labels = batch["labels"].to(self.device)

            self.optimizer.zero_grad()
            outputs = self.model(inputs)
            loss = torch.nn.functional.cross_entropy(outputs.view(-1, outputs.size(-1)), labels.view(-1))
            loss.backward()
            self.optimizer.step()
            self.scheduler.step()
            total_loss += loss.item()
        return total_loss / len(dataloader)

    def evaluate(self, eval_dataset, batch_size=32):
        self.model.eval()
        dataloader = DataLoader(eval_dataset, batch_size=batch_size)
        total_loss = 0
        with torch.no_grad():
            for batch in dataloader:
                inputs = batch["input_ids"].to(self.device)
                labels = batch["labels"].to(self.device)
                outputs = self.model(inputs)
                loss = torch.nn.functional.cross_entropy(outputs.view(-1, outputs.size(-1)), labels.view(-1))
                total_loss += loss.item()
        return total_loss / len(dataloader)
