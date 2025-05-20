import argparse
from uxi import load_model

def main():
    parser = argparse.ArgumentParser(description="Evaluate UXI-LLM model inference")
    parser.add_argument("--model", type=str, required=True, help="Model name to evaluate")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt text for inference")
    parser.add_argument("--max_tokens", type=int, default=50, help="Max tokens to generate")
    args = parser.parse_args()

    model = load_model(args.model)
    output = model.run(args.prompt, max_tokens=args.max_tokens)
    print("Inference output:\n", output)

if __name__ == "__main__":
    main()
