# data/loader.py

import os
from datasets import load_dataset as hf_load_dataset

def load_dataset(name, split='train'):
    """
    Load a dataset by name using Hugging Face datasets library.
    """
    dataset = hf_load_dataset(name, split=split)
    return dataset
