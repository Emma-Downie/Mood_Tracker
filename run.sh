#!/bin/bash

# check if python is installed 

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
pip3 install pytest
python3 main.py