import unittest
from uxi.symbolic import parse, evaluate, LogicGraph

class TestSymbolic(unittest.TestCase):

    def test_parse_creates_logic_graph(self):
        text = "True and not False"
        logic_graph = parse(text)
        self.assertIsInstance(logic_graph, LogicGraph)
        self.assertTrue(len(logic_graph.graph.nodes) > 0)

    def test_evaluate_returns_correct_value(self):
        text_true = "True"
        text_false = "False"
        lg_true = parse(text_true)
        lg_false = parse(text_false)
        self.assertTrue(evaluate(lg_true))
        self.assertFalse(evaluate(lg_false))

    def test_evaluate_no_true_false_returns_none(self):
        text = "and or not"
        lg = parse(text)
        self.assertIsNone(evaluate(lg))

if __name__ == "__main__":
    unittest.main()
