📄 File: docs/usage.md  
💬 Commit message: Add basic usage guide with install, inference, fine-tuning, and symbolic reasoning examples

```markdown
# UXI-LLM Usage Guide

## Installation

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

## Loading a Model

```python
from uxi import load_model

model = load_model("gpt2")
```

## Running Inference

```python
output = model.run("Hello, world!", max_tokens=50)
print(output)
```

## Fine-Tuning

```python
from uxi import FineTuner

tuner = FineTuner(model)
tuner.load_dataset("dataset.jsonl")
tuner.train(epochs=3, batch_size=8)
tuner.save_checkpoint("fine_tuned.pt")
```

## Symbolic Reasoning

```python
from uxi.symbolic import parse, evaluate

logic_graph = parse("not (True and False)")
result = evaluate(logic_graph)
print(result)
```

## CLI Scripts

- `scripts/train.py` – Fine-tune models
- `scripts/evaluate.py` – Run inference
- `scripts/symbolic_eval.py` – Evaluate symbolic expressions

For more detailed info, see other docs and examples.
```
