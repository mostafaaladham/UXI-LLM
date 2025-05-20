from uxi.symbolic import parse, evaluate

def main():
    expression = "True and (False or True)"
    graph = parse(expression)
    result = evaluate(graph)
    print(f"Expression: {expression}")
    print(f"Evaluation result: {result}")

if __name__ == "__main__":
    main()
