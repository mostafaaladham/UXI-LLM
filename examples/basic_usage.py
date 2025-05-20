from uxi import load_model

def main():
    model = load_model("gpt2")
    prompt = "Hello, UXI-LLM!"
    output = model.run(prompt, max_tokens=20)
    print("Generated output:")
    print(output)

if __name__ == "__main__":
    main()
