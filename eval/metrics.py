# eval/metrics.py

import torch
import torch.nn.functional as F

def compute_accuracy(logits, labels):
    preds = torch.argmax(logits, dim=-1)
    correct = (preds == labels).float()
    return correct.sum() / correct.numel()

def compute_loss(logits, labels, criterion):
    return criterion(logits.view(-1, logits.size(-1)), labels.view(-1))

def compute_perplexity(loss):
    return torch.exp(loss)

def top_k_accuracy(logits, labels, k=5):
    top_k = torch.topk(logits, k, dim=-1).indices
    correct = top_k.eq(labels.unsqueeze(-1)).sum().float()
    return correct / labels.numel()
