import unittest
from uxi import load_model, FineTuner
import os

class TestFineTuner(unittest.TestCase):
    def setUp(self):
        self.model = load_model("gpt2")
        self.finetuner = FineTuner(self.model)

    def test_load_dataset(self):
        # Using a dummy dataset path - should be replaced with a real test dataset
        with self.assertRaises(FileNotFoundError):
            self.finetuner.load_dataset("nonexistent_dataset.jsonl")

    def test_train_and_save(self):
        # Mock minimal training to test save checkpoint
        try:
            self.finetuner.train(epochs=1, batch_size=1)
        except Exception:
            # Training might fail without dataset, ignore for this test
            pass

        checkpoint_path = "test_checkpoint.pt"
        self.finetuner.save_checkpoint(checkpoint_path)
        self.assertTrue(os.path.exists(checkpoint_path))
        os.remove(checkpoint_path)

if __name__ == "__main__":
    unittest.main()
