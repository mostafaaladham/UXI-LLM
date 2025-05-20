import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Model:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def run(self, prompt: str, max_tokens: int = 256) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            do_sample=True,
            top_p=0.95,
            temperature=0.8,
            eos_token_id=self.tokenizer.eos_token_id,
        )
        generated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated

def load_model(name: str) -> Model:
    return Model(name)
