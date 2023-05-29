#!/bin/bash
#
#
#
clear
echo ""
echo "Intalling env"
echo ""
python3 -m pip install env

# We create a virtual environment for python
clear
echo ""
echo "Create a venv space"
echo ""
python3 -m venv venv

# We activate the environment
clear
echo ""
echo "Activate venv virtual environment"
echo ""
source venv/bin/activate

# Install the requirements
clear
echo ""
echo "Installing pip requirements"
echo ""
pip install -r requirements.txt

# Then exec the kernel
echo ""
echo "Exec kernel bot"
echo ""

python3 kernel-bot.py 
