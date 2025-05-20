import unittest
from uxi import load_model

class TestModel(unittest.TestCase):
    def setUp(self):
        self.model_name = "gpt2"
        self.model = load_model(self.model_name)

    def test_model_load(self):
        self.assertIsNotNone(self.model)
        self.assertEqual(self.model.model_name, self.model_name)

    def test_run_inference(self):
        prompt = "Hello, world!"
        output = self.model.run(prompt, max_tokens=10)
        self.assertIsInstance(output, str)
        self.assertTrue(len(output) > 0)

if __name__ == "__main__":
    unittest.main()
