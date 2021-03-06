#!/bin/bash
git pull origin master

if [ -e venv/ ]; then
    rm -r venv/
fi

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python cache_scripts/main.py
gunicorn index:server -c gunicorn_config.py