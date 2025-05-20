# UXI-LLM API Reference

## uxi Module

### `load_model(name: str) -> Model`
Load a pre-trained model by name.

### `FineTuner(model: Model)`
Class to fine-tune models.

- `load_dataset(path: str)`
- `train(epochs: int, batch_size: int)`
- `save_checkpoint(path: str)`

## uxi.symbolic Module

### `parse(expression: str) -> LogicGraph`
Parse a symbolic logic expression into a LogicGraph.

### `evaluate(logic_graph: LogicGraph) -> bool or None`
Evaluate the logic graph and return the boolean result or None.

## Model Class

### `run(prompt: str, max_tokens: int) -> str`
Generate text based on the input prompt.

## LogicGraph Class

Represents a symbolic logic graph parsed from an expression.

---
For detailed examples, see the `/examples` directory.
