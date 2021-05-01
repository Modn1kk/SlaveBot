#!/usr/bin/env bash
pkg install -y python
clear
pip install -r requirements.txt
clear
python bot.py
