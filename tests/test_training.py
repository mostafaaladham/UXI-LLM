# tests/test_training.py

import unittest
from trainer.train import train
from trainer.evaluate import evaluate

class TestTrainingFunctions(unittest.TestCase):

    def test_train_runs(self):
        # This test just ensures the train function can be called without error on a dummy config
        try:
            train(config_path='configs/default.json')
        except Exception as e:
            self.fail(f"train() raised an exception: {e}")

    def test_evaluate_runs(self):
        # This test just ensures the evaluate function can be called without error on a dummy config
        try:
            evaluate(config_path='configs/default.json')
        except Exception as e:
            self.fail(f"evaluate() raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
