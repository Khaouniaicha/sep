#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if python3 is available
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found"
    exit 1
fi

# Display Python version
python3 --version

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install -r requirements.txt

# Run Django migrations (optional, if needed)
python3 manage.py migrate

# Collect static files
python3 manage.py collectstatic --noinput

# Add any other build steps here
