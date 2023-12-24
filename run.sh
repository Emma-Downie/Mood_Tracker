#!/bin/bash

# check if python is installed 
    #print on screen please instal python if not installed

python3 -m venv .mood_venv
source .venv/bin/activate
pip3 install colored
pip3 install pytest
python3 main.py