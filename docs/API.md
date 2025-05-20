# UXI-LLM API Reference

This document outlines the primary classes and functions provided by the UXI-LLM framework.

## Modules

### models.transformer

- **TransformerModel**  
  Core Transformer-based LLM implementation.  
  Constructor parameters: `vocab_size`, `d_model`, `nhead`, `num_layers`, `dim_feedforward`, `dropout`  
  Methods: `forward(input)`

### utils.tokenizer

- **SimpleTokenizer**  
  Basic tokenizer utility for tokenizing and detokenizing text.  
  Methods: `tokenize(text)`, `detokenize(tokens)`

### trainer.train

- **train(config_path)**  
  Main training function which loads config, data, initializes model and optimizer, and runs training epochs.

### trainer.evaluate

- **evaluate(config_path)**  
  Runs evaluation on validation data and reports loss.

## Usage

See `/scripts/` for example scripts such as `run_inference.py` and `train_from_cli.py`.

---

For detailed usage, please refer to the tutorials in `docs/Tutorials.md`.
