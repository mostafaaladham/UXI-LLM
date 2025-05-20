# train/train.py

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from transformers import AutoTokenizer

from models.transformer import TransformerModel
from data.loader import load_dataset
from data.preprocess import preprocess_text
from utils.file_utils import read_json

def collate_fn(batch, tokenizer):
    tokens = [tokenizer.encode(preprocess_text(example['text']), truncation=True, max_length=512) for example in batch]
    padded = torch.nn.utils.rnn.pad_sequence([torch.tensor(t) for t in tokens], batch_first=True)
    return padded, padded

def main(config_path='configs/default.json'):
    config = read_json(config_path)
    model_cfg = config['model']
    train_cfg = config['training']
    data_cfg = config['data']

    tokenizer = AutoTokenizer.from_pretrained("gpt2")

    dataset = load_dataset(data_cfg['dataset_name'], split=data_cfg['split'])
    dataloader = DataLoader(dataset, batch_size=train_cfg['batch_size'], shuffle=True,
                            collate_fn=lambda b: collate_fn(b, tokenizer))

    model = TransformerModel(
        vocab_size=model_cfg['vocab_size'],
        d_model=model_cfg['d_model'],
        nhead=model_cfg['nhead'],
        num_layers=model_cfg['num_layers'],
        dim_feedforward=model_cfg['dim_feedforward'],
        dropout=model_cfg['dropout']
    )

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    optimizer = optim.AdamW(model.parameters(), lr=train_cfg['learning_rate'], weight_decay=train_cfg['weight_decay'])
    criterion = nn.CrossEntropyLoss()

    for epoch in range(train_cfg['epochs']):
        model.train()
        total_loss = 0
        for i, (input_ids, targets) in enumerate(dataloader):
            input_ids, targets = input_ids.to(device), targets.to(device)
            optimizer.zero_grad()
            output = model(input_ids)
            loss = criterion(output.view(-1, model_cfg['vocab_size']), targets.view(-1))
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        avg_loss = total_loss / len(dataloader)
        print(f"Epoch {epoch + 1}: Loss = {avg_loss:.4f}")

    torch.save(model.state_dict(), config['paths']['save_model'])

if __name__ == '__main__':
    main()
