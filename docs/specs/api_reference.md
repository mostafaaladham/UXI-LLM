# API Reference

## Overview

This document provides a detailed reference of UXI-LLM's core API surface, including model loading, inference, symbolic modules, and fine-tuning interfaces.

---

## Module: uxi.model

### `load_model(name: str) -> Model`

Load a UXI-LLM model by name.

- **Parameters:**  
  - `name`: Model identifier string.

- **Returns:**  
  - `Model` instance.

---

## Module: uxi.model.Model

### `run(prompt: str, max_tokens: int = 256) -> str`

Run inference on the input prompt.

- **Parameters:**  
  - `prompt`: Input text.  
  - `max_tokens`: Maximum tokens to generate.

- **Returns:**  
  - Generated text string.

---

### `inject_symbolic(module: SymbolicModule) -> None`

Attach a symbolic reasoning module.

- **Parameters:**  
  - `module`: Instance of a symbolic reasoning module.

---

## Module: uxi.fine_tuning

### `FineTuner(model: Model)`

Create a fine-tuner for the given model.

### `train(epochs: int, batch_size: int) -> None`

Start training.

---

## Module: uxi.symbolic

### `parse(text: str) -> LogicGraph`

Parse text into a symbolic logic graph.

### `evaluate(logic_graph: LogicGraph) -> Any`

Evaluate the logic graph.

---

## Notes

- All API calls are synchronous unless noted.
- Streaming interfaces will be documented in future revisions.
