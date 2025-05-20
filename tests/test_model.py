import unittest
from uxi import load_model

class TestModel(unittest.TestCase):
    def test_load_model(self):
        model = load_model("gpt2")
        self.assertIsNotNone(model)
        self.assertTrue(hasattr(model, "run"))

    def test_inference_output(self):
        model = load_model("gpt2")
        prompt = "Test prompt"
        output = model.run(prompt, max_tokens=10)
        self.assertIsInstance(output, str)
        self.assertGreater(len(output), 0)

if __name__ == "__main__":
    unittest.main()
