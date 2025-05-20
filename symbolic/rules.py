# symbolic/rules.py

import json

def load_ruleset(filepath):
    """
    Load symbolic reasoning rules from a JSON file.
    Rules should be defined as JSON objects with conditions and actions.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        rules = json.load(f)
    return rules
