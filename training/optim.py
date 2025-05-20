# training/optim.py

import torch.optim as optim

def get_optimizer(model, lr=5e-5):
    return optim.AdamW(model.parameters(), lr=lr)

def get_scheduler(optimizer, num_warmup_steps, num_training_steps):
    from transformers import get_linear_schedule_with_warmup
    return get_linear_schedule_with_warmup(optimizer, num_warmup_steps=num_warmup_steps, num_training_steps=num_training_steps)
