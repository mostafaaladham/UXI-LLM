# inference/predict.py

import torch
from transformers import AutoTokenizer
from models.transformer import TransformerModel
from utils.file_utils import read_json
from data.preprocess import preprocess_text


def generate_response(input_text, config_path='configs/default.json'):
    config = read_json(config_path)
    model_cfg = config['model']
    tokenizer = AutoTokenizer.from_pretrained("gpt2")

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

    input_text = preprocess_text(input_text)
    input_ids = torch.tensor([tokenizer.encode(input_text)]).to(device)

    with torch.no_grad():
        logits = model(input_ids)
        predicted_token_id = torch.argmax(logits[0, -1]).item()
        output = tokenizer.decode([predicted_token_id])

    return output


if __name__ == '__main__':
    prompt = input("Enter input: ")
    response = generate_response(prompt)
    print("UXI-LLM:", response)
