#!/bin/bash

# Install Python (if not already installed)
# Vercel's build environment might already have Python, but it's good to ensure.
# You can specify the Python version you need.

# Check Python version
python --version

# Upgrade pip using Python's module interface to ensure it's available
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# Install dependencies
python -m pip install -r requirements.txt

# Add any other build steps here
