import argparse
from uxi.symbolic import parse, evaluate

def main():
    parser = argparse.ArgumentParser(description="Evaluate symbolic logic expressions")
    parser.add_argument("--expr", type=str, required=True, help="Logic expression to evaluate")
    args = parser.parse_args()

    logic_graph = parse(args.expr)
    result = evaluate(logic_graph)
    print(f"Expression: {args.expr}")
    print(f"Evaluation result: {result}")

if __name__ == "__main__":
    main()
