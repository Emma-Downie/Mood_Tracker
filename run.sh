#!/bin/bash

python3 -m venv .mood_venv
source .venv/bin/activate
pip3 install colored
python3 main.py