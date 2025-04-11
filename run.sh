#!/bin/bash

# run.sh
#
# This script is used to execute the Python application using Pipenv.
# It ensures that your application runs in the virtual environment
# managed by Pipenv, using the specified Python interpreter.
#
# How to use this script:
# 1. Ensure you have Pipenv installed and that you have already
#    created a Pipenv environment with the necessary dependencies.
# 2. Place this script in the same directory as your main.py file.
# 3. Make the script executable with:
#    chmod +x run.sh
# 4. Run the script using:
#    ./run.sh
#
# Note: You should have already set up your project with pipenv,
# including creating the Pipfile and installing dependencies.

# Ensure the script runs with Poetry
poetry run python src/main.py
