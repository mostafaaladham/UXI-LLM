# symbolic/logic_engine.py

from typing import Any, Dict, List, Callable

class SymbolicContext:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact: str):
        self.facts.add(fact)

    def add_rule(self, rule_func: Callable[[set], List[str]]):
        self.rules.append(rule_func)

    def infer(self):
        inferred = set()
        for rule in self.rules:
            new_facts = rule(self.facts)
            inferred.update(new_facts)
        self.facts.update(inferred)
        return inferred

    def reset(self):
        self.facts.clear()
        self.rules.clear()

def example_rule(facts: set) -> List[str]:
    if "sky_is_clear" in facts and "sun_is_up" in facts:
        return ["it_is_day"]
    return []

# Example usage
if __name__ == "__main__":
    ctx = SymbolicContext()
    ctx.add_fact("sky_is_clear")
    ctx.add_fact("sun_is_up")
    ctx.add_rule(example_rule)

    inferred = ctx.infer()
    print("Inferred:", inferred)
