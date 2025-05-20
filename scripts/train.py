import argparse
from uxi import load_model, FineTuner

def main():
    parser = argparse.ArgumentParser(description="Fine-tune UXI-LLM models")
    parser.add_argument("--model", type=str, required=True, help="Model name to load")
    parser.add_argument("--dataset", type=str, required=True, help="Path to dataset file")
    parser.add_argument("--epochs", type=int, default=3, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=8, help="Training batch size")
    parser.add_argument("--save_path", type=str, default="checkpoint.pt", help="Checkpoint save path")
    args = parser.parse_args()

    model = load_model(args.model)
    tuner = FineTuner(model)
    tuner.load_dataset(args.dataset)
    tuner.train(epochs=args.epochs, batch_size=args.batch_size)
    tuner.save_checkpoint(args.save_path)
    print(f"Training complete. Checkpoint saved to {args.save_path}")

if __name__ == "__main__":
    main()
