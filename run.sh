#!/bin/bash

# check if python is installed 

#check if venv exists

python3 -m venv .mood_venv
source .venv/bin/activate
pip3 install colored
python3 main.py