#!/bin/bash

# Check if the virtual environment already exists
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Failed to activate virtual environment"
    exit 1
fi

# Install the required packages
pip install -r requirements.txt

# Check if installation was successful
if [ $? -ne 0 ]; then
    echo "Failed to install required packages"
    exit 1
fi

# Navigate to the script directory
cd src

# Check if navigation was successful
if [ $? -ne 0 ]; then
    echo "Failed to navigate to script directory"
    exit 1
fi

# Run the script, passed as an argument
python3 main.py

# Check if script ran successfully
if [ $? -ne 0 ]; then
    echo "Failed to run script"
    exit 1
fi

# Deactivate the environment
deactivate
