from uxi import load_model, FineTuner

def main():
    model = load_model("gpt2")
    fine_tuner = FineTuner(model)
    fine_tuner.load_dataset("path/to/dataset.jsonl")
    fine_tuner.train(epochs=2, batch_size=4)
    fine_tuner.save_checkpoint("fine_tuned_model.pt")
    print("Fine-tuning complete and checkpoint saved.")

if __name__ == "__main__":
    main()
