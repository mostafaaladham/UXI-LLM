import argparse
from uxi import load_model, FineTuner

def main():
    parser = argparse.ArgumentParser(description="Fine-tune UXI-LLM model")
    parser.add_argument("--model", type=str, default="gpt2", help="Base model to fine-tune")
    parser.add_argument("--dataset", type=str, required=True, help="Path to training dataset")
    parser.add_argument("--epochs", type=int, default=3, help="Number of training epochs")
    parser.add_argument("--batch_size", type=int, default=8, help="Batch size for training")
    parser.add_argument("--output", type=str, default="fine_tuned_model.pt", help="Output checkpoint file")
    args = parser.parse_args()

    model = load_model(args.model)
    finetuner = FineTuner(model)
    finetuner.load_dataset(args.dataset)
    finetuner.train(epochs=args.epochs, batch_size=args.batch_size)
    finetuner.save_checkpoint(args.output)
    print(f"Training complete. Model saved to {args.output}")

if __name__ == "__main__":
    main()
