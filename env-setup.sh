#!/bin/bash

# Create a virtual environment
python -m venv env

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt