from uxi import load_model

def main():
    model = load_model("gpt2")
    prompt = "Explain the concept of symbolic reasoning."
    output = model.run(prompt, max_tokens=100)
    print("Model output:\n", output)

if __name__ == "__main__":
    main()
