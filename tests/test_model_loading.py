import unittest
from uxi import load_model

class TestModelLoading(unittest.TestCase):
    def test_load_default_model(self):
        model = load_model("uxi-transformer-v1")
        self.assertIsNotNone(model, "Model should load successfully")
        output = model.run("Test input")
        self.assertIsInstance(output, str, "Output should be a string")
        self.assertTrue(len(output) > 0, "Output should not be empty")

if __name__ == "__main__":
    unittest.main()
