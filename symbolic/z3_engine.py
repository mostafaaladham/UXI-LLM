# symbolic/z3_engine.py

from z3 import Solver, Bool, And, Or, Not, sat

class Z3Engine:
    def __init__(self):
        self.solver = Solver()

    def add_constraints(self, constraints):
        for constraint in constraints:
            self.solver.add(constraint)

    def check(self):
        return self.solver.check()

    def model(self):
        if self.solver.check() == sat:
            return self.solver.model()
        return None

    def reset(self):
        self.solver.reset()
