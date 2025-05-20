# utils/file_utils.py

import json
import os

def read_json(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(filepath: str, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def save_model(model, path: str):
    import torch
    os.makedirs(os.path.dirname(path), exist_ok=True)
    torch.save(model.state_dict(), path)

def load_model(model_class, path: str, *args, **kwargs):
    import torch
    model = model_class(*args, **kwargs)
    model.load_state_dict(torch.load(path))
    model.eval()
    return model
