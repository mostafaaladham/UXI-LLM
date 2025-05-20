import unittest
import os
import json
from uxi import load_model, FineTuner

class TestFineTuning(unittest.TestCase):
    def setUp(self):
        self.model = load_model("gpt2")
        self.fine_tuner = FineTuner(self.model)
        # Prepare a small dummy dataset file
        self.dataset_path = "dummy_dataset.jsonl"
        with open(self.dataset_path, "w") as f:
            for i in range(5):
                json.dump({"text": f"Sample text {i}"}, f)
                f.write("\n")

    def tearDown(self):
        if os.path.exists(self.dataset_path):
            os.remove(self.dataset_path)

    def test_load_dataset(self):
        self.fine_tuner.load_dataset(self.dataset_path)
        self.assertIsNotNone(self.fine_tuner.dataset)
        self.assertEqual(len(self.fine_tuner.dataset), 5)

    def test_train_runs(self):
        self.fine_tuner.load_dataset(self.dataset_path)
        try:
            self.fine_tuner.train(epochs=1, batch_size=2)
        except Exception as e:
            self.fail(f"Training raised exception {e}")

if __name__ == "__main__":
    unittest.main()
