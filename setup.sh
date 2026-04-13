#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install PyQt6

gcc menu.c -o menu

chmod +x menu
chmod +x run-cli-oneline.sh
chmod +x mc-converter-oneline-cli.py

echo "Setup finished. Run ./menu to start."
