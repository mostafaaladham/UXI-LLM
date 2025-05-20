from uxi.symbolic import parse, evaluate

def main():
    expr = "not (True and False) or True"
    logic_graph = parse(expr)
    result = evaluate(logic_graph)
    print(f"Expression: {expr}")
    print(f"Evaluation result: {result}")

if __name__ == "__main__":
    main()
