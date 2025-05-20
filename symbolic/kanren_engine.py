# symbolic/kanren_engine.py

from kanren import run, var, Relation, facts

class MiniKanrenEngine:
    def __init__(self):
        self.relations = {}

    def create_relation(self, name):
        rel = Relation()
        self.relations[name] = rel
        return rel

    def add_facts(self, relation_name, facts_list):
        rel = self.relations.get(relation_name)
        if not rel:
            rel = self.create_relation(relation_name)
        for fact in facts_list:
            facts(rel, *fact)

    def query(self, relation_name, query_vars):
        rel = self.relations.get(relation_name)
        if not rel:
            return []
        return run(0, query_vars, rel(*query_vars))
