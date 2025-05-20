# trainer/evaluate.py

import torch
from torch.utils.data import DataLoader
from models.transformer import TransformerModel
from data.preprocess import load_dataset
from utils.file_utils import read_json
import torch.nn as nn


def evaluate(config_path='configs/default.json'):
    config = read_json(config_path)
    model_cfg = config['model']
    eval_cfg = config['evaluation']

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    dataset = load_dataset(eval_cfg['eval_data_path'])
    dataloader = DataLoader(dataset, batch_size=eval_cfg['batch_size'], shuffle=False)

    model = TransformerModel(
        vocab_size=model_cfg['vocab_size'],
        d_model=model_cfg['d_model'],
        nhead=model_cfg['nhead'],
        num_layers=model_cfg['num_layers'],
        dim_feedforward=model_cfg['dim_feedforward'],
        dropout=model_cfg['dropout']
    ).to(device)

    model.load_state_dict(torch.load(config['paths']['save_model']))
    model.eval()

    criterion = nn.CrossEntropyLoss()
    total_loss = 0

    with torch.no_grad():
        for batch in dataloader:
            inputs, targets = batch
            inputs, targets = inputs.to(device), targets.to(device)

            outputs = model(inputs)
            loss = criterion(outputs.view(-1, model_cfg['vocab_size']), targets.view(-1))
            total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    print(f"Evaluation Loss: {avg_loss:.4f}")


if __name__ == '__main__':
    evaluate()
