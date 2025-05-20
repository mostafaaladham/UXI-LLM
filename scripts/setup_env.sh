#!/bin/bash

echo "Setting up UXI-LLM development environment..."

# Update package lists
sudo apt-get update

# Install Python3 and pip if missing
sudo apt-get install -y python3 python3-pip python3-venv

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required Python packages
pip install -r requirements.txt

echo "Environment setup complete."
