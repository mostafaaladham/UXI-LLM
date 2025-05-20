import unittest
from uxi.fine_tuning import FineTuner
from uxi import load_model
import os

class TestFineTuning(unittest.TestCase):

    def setUp(self):
        self.model = load_model("uxi-transformer-v1")
        self.tuner = FineTuner(model=self.model)

    def test_load_dataset_and_train(self):
        # Assuming a small dummy dataset in-memory or mocked
        self.tuner.load_dataset("tests/dummy_data.jsonl")
        self.tuner.train(epochs=1, batch_size=2)
        self.assertTrue(True, "Training completed without error")

    def test_save_and_load_checkpoint(self):
        checkpoint_path = "tests/checkpoint_test.pt"
        self.tuner.save_checkpoint(checkpoint_path)
        self.assertTrue(os.path.exists(checkpoint_path), "Checkpoint file should exist")
        # Cleanup after test
        os.remove(checkpoint_path)

if __name__ == "__main__":
    unittest.main()
