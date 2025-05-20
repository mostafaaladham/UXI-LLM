# scripts/train_from_cli.py

import argparse
from trainer.train import train

def main():
    parser = argparse.ArgumentParser(description="Train UXI-LLM from command line.")
    parser.add_argument('--config', type=str, default='configs/default.json', help='Path to config JSON file')
    args = parser.parse_args()
    train(config_path=args.config)

if __name__ == "__main__":
    main()
