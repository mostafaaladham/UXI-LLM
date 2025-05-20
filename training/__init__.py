# training/__init__.py

"""
Training module for UXI-LLM.
Includes training loops, optimizer setup, scheduler, and utility functions.
"""

from .trainer import Trainer
from .optim import get_optimizer, get_scheduler
