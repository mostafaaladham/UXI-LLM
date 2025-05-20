# symbolic/registry.py

from typing import Callable, Dict

class SymbolicRegistry:
    """
    Registry for custom symbolic functions or rule handlers.
    Enables dynamic registration and lookup.
    """
    def __init__(self):
        self.registry: Dict[str, Callable] = {}

    def register(self, name: str, fn: Callable):
        if name in self.registry:
            raise KeyError(f"Symbolic function '{name}' already registered.")
        self.registry[name] = fn

    def get(self, name: str) -> Callable:
        if name not in self.registry:
            raise KeyError(f"Symbolic function '{name}' not found.")
        return self.registry[name]

    def list_functions(self):
        return list(self.registry.keys())


# Example usage
if __name__ == "__main__":
    registry = SymbolicRegistry()

    def is_even(n):
        return n % 2 == 0

    registry.register("is_even", is_even)

    func = registry.get("is_even")
    print("4 is even?", func(4))
