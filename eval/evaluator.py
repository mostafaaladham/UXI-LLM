# eval/evaluator.py

import torch
from torch.utils.data import DataLoader
from transformers import AutoTokenizer

from data.loader import load_dataset
from data.preprocess import preprocess_text
from models.transformer import TransformerModel
from utils.file_utils import read_json
from eval.metrics import compute_accuracy, compute_loss, compute_perplexity

def collate_fn(batch, tokenizer):
    tokens = [tokenizer.encode(preprocess_text(example['text']), truncation=True, max_length=512) for example in batch]
    padded = torch.nn.utils.rnn.pad_sequence([torch.tensor(t) for t in tokens], batch_first=True)
    return padded, padded

def evaluate(config_path='configs/default.json'):
    config = read_json(config_path)
    model_cfg = config['model']
    data_cfg = config['data']

    tokenizer = AutoTokenizer.from_pretrained("gpt2")

    dataset = load_dataset(data_cfg['dataset_name'], split='validation')
    dataloader = DataLoader(dataset, batch_size=1, shuffle=False,
                            collate_fn=lambda b: collate_fn(b, tokenizer))

    model = TransformerModel(
        vocab_size=model_cfg['vocab_size'],
        d_model=model_cfg['d_model'],
        nhead=model_cfg['nhead'],
        num_layers=model_cfg['num_layers'],
        dim_feedforward=model_cfg['dim_feedforward'],
        dropout=model_cfg['dropout']
    )

    model.load_state_dict(torch.load(config['paths']['save_model']))
    model.eval()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    total_accuracy = 0
    total_loss = 0
    criterion = torch.nn.CrossEntropyLoss()

    with torch.no_grad():
        for input_ids, labels in dataloader:
            input_ids, labels = input_ids.to(device), labels.to(device)
            logits = model(input_ids)
            loss = compute_loss(logits, labels, criterion)
            acc = compute_accuracy(logits, labels)
            total_loss += loss.item()
            total_accuracy += acc.item()

    avg_loss = total_loss / len(dataloader)
    avg_acc = total_accuracy / len(dataloader)
    perplexity = compute_perplexity(torch.tensor(avg_loss))

    print(f"Validation Loss: {avg_loss:.4f}")
    print(f"Validation Accuracy: {avg_acc:.4f}")
    print(f"Validation Perplexity: {perplexity:.4f}")

if __name__ == '__main__':
    evaluate()
