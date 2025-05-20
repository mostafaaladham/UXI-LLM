# tests/test_config_loading.py

import unittest
import json
from utils.config import load_config

class TestConfigLoading(unittest.TestCase):

    def test_load_default_config(self):
        config = load_config("configs/default.json")
        self.assertIsInstance(config, dict)
        self.assertIn("training", config)
        self.assertIn("model", config)

    def test_invalid_path_raises(self):
        with self.assertRaises(FileNotFoundError):
            load_config("configs/missing.json")

if __name__ == "__main__":
    unittest.main()
