import unittest
from uxi.symbolic import parse, evaluate, LogicGraph

class TestSymbolicModule(unittest.TestCase):

    def test_parse_simple_expression(self):
        expr = "A and B"
        logic_graph = parse(expr)
        self.assertIsInstance(logic_graph, LogicGraph)
        self.assertTrue(logic_graph.nodes, "Logic graph should have nodes")

    def test_evaluate_true(self):
        expr = "True and True"
        logic_graph = parse(expr)
        result = evaluate(logic_graph)
        self.assertTrue(result, "Expression should evaluate to True")

    def test_evaluate_false(self):
        expr = "True and False"
        logic_graph = parse(expr)
        result = evaluate(logic_graph)
        self.assertFalse(result, "Expression should evaluate to False")

if __name__ == "__main__":
    unittest.main()
