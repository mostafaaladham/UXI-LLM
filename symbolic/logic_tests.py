# symbolic/logic_tests.py

import unittest
from symbolic.logic_engine import SymbolicContext, example_rule
from symbolic.expression_parser import ExpressionParser
from symbolic.registry import SymbolicRegistry


class TestSymbolicLogic(unittest.TestCase):

    def test_logic_engine_inference(self):
        ctx = SymbolicContext()
        ctx.add_fact("sky_is_clear")
        ctx.add_fact("sun_is_up")
        ctx.add_rule(example_rule)

        inferred = ctx.infer()
        self.assertIn("it_is_day", inferred)

    def test_expression_parser(self):
        parser = ExpressionParser()
        expr = "A AND (B OR NOT C)"
        parsed = parser.parse_expression(expr)
        self.assertIsInstance(parsed, dict)
        self.assertIn("AND", parsed)

    def test_symbolic_registry(self):
        registry = SymbolicRegistry()

        def is_odd(n): return n % 2 == 1

        registry.register("is_odd", is_odd)
        fn = registry.get("is_odd")
        self.assertTrue(fn(3))
        self.assertFalse(fn(4))

        with self.assertRaises(KeyError):
            registry.register("is_odd", is_odd)

        with self.assertRaises(KeyError):
            registry.get("nonexistent")

if __name__ == '__main__':
    unittest.main()
