from uxi import load_model, FineTuner

def main():
    model = load_model("gpt2")
    finetuner = FineTuner(model)
    finetuner.load_dataset("data/sample_training_data.jsonl")
    finetuner.train(epochs=2, batch_size=4)
    finetuner.save_checkpoint("fine_tuned_example.pt")
    print("Fine-tuning completed and checkpoint saved.")

if __name__ == "__main__":
    main()
