#!/bin/bash

# Check if python3 is available
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    exit 1
fi

python3 --version

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip within the virtual environment
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install -r requirements.txt

# Add any other build steps here, using python3 instead of python
