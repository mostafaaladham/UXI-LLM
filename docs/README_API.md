# UXI-LLM API Documentation

## Model Loading and Inference

```python
from uxi import load_model

model = load_model("uxi-transformer-v1")
output = model.run("Hello world")
print(output)
