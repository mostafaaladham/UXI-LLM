# trainer/train.py

import torch
from torch.utils.data import DataLoader
from models.transformer import TransformerModel
from data.preprocess import load_dataset
from utils.file_utils import save_model, read_json
import torch.nn as nn
import torch.optim as optim


def train(config_path='configs/default.json'):
    config = read_json(config_path)
    model_cfg = config['model']
    train_cfg = config['training']

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    dataset = load_dataset(train_cfg['train_data_path'])
    dataloader = DataLoader(dataset, batch_size=train_cfg['batch_size'], shuffle=True)

    model = TransformerModel(
        vocab_size=model_cfg['vocab_size'],
        d_model=model_cfg['d_model'],
        nhead=model_cfg['nhead'],
        num_layers=model_cfg['num_layers'],
        dim_feedforward=model_cfg['dim_feedforward'],
        dropout=model_cfg['dropout']
    ).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=train_cfg['learning_rate'])

    for epoch in range(train_cfg['epochs']):
        model.train()
        total_loss = 0

        for batch in dataloader:
            inputs, targets = batch
            inputs, targets = inputs.to(device), targets.to(device)

            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs.view(-1, model_cfg['vocab_size']), targets.view(-1))
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        avg_loss = total_loss / len(dataloader)
        print(f"Epoch {epoch+1}/{train_cfg['epochs']} - Loss: {avg_loss:.4f}")

        # Save model checkpoint
        if (epoch + 1) % train_cfg.get('save_every', 1) == 0:
            save_model(model, config['paths']['save_model'])

if __name__ == '__main__':
    train()
