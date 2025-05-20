import argparse
from uxi import load_model

def main():
    parser = argparse.ArgumentParser(description="Run inference using UXI-LLM models")
    parser.add_argument("--model", type=str, required=True, help="Model name to load")
    parser.add_argument("--prompt", type=str, required=True, help="Input prompt for the model")
    parser.add_argument("--max_tokens", type=int, default=50, help="Maximum tokens to generate")
    args = parser.parse_args()

    model = load_model(args.model)
    output = model.run(args.prompt, max_tokens=args.max_tokens)
    print(f"Output:\n{output}")

if __name__ == "__main__":
    main()
