# symbolic/expression_parser.py

import re
from typing import Any, Dict

class ExpressionParser:
    """
    Parses simple logical expressions into structured form.
    Supports basic operators: AND, OR, NOT, =>.
    """

    def __init__(self):
        self.pattern = re.compile(r'\s*(\w+|\(|\)|AND|OR|NOT|=>)\s*')

    def tokenize(self, expr: str):
        return self.pattern.findall(expr)

    def parse(self, tokens):
        def parse_expr(index):
            if index >= len(tokens):
                raise ValueError("Unexpected end of expression")

            token = tokens[index]
            if token == '(':
                node, index = parse_expr(index + 1)
                if tokens[index] != ')':
                    raise ValueError("Expected ')'")
                return node, index + 1
            elif token == 'NOT':
                node, index = parse_expr(index + 1)
                return {'NOT': node}, index
            elif token.isalnum():
                return token, index + 1
            else:
                raise ValueError(f"Unexpected token: {token}")

        def parse_binary_ops(left, index):
            if index >= len(tokens):
                return left, index

            token = tokens[index]
            if token in ('AND', 'OR', '=>'):
                right, next_index = parse_expr(index + 1)
                return {token: [left, right]}, next_index
            else:
                return left, index

        node, index = parse_expr(0)
        while index < len(tokens):
            node, index = parse_binary_ops(node, index)
        return node

    def parse_expression(self, expr: str) -> Dict[str, Any]:
        tokens = self.tokenize(expr)
        return self.parse(tokens)


# Example usage
if __name__ == "__main__":
    parser = ExpressionParser()
    example = "A AND (B OR NOT C)"
    tree = parser.parse_expression(example)
    print("Parsed Tree:", tree)
