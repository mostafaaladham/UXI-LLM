import unittest
from uxi.symbolic import parse, evaluate

class TestSymbolic(unittest.TestCase):
    def test_parse_and_evaluate_true(self):
        expr = "True and not False"
        graph = parse(expr)
        result = evaluate(graph)
        self.assertTrue(result)

    def test_parse_and_evaluate_false(self):
        expr = "False or (False and True)"
        graph = parse(expr)
        result = evaluate(graph)
        self.assertFalse(result)

    def test_parse_invalid_expression(self):
        expr = "True and or False"
        with self.assertRaises(Exception):
            graph = parse(expr)

if __name__ == "__main__":
    unittest.main()
