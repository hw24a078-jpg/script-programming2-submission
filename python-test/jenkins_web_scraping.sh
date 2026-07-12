#!/usr/bin/env bash
set -e

WORK_DIR="/Users/hw24a078/Desktop/スクリプトプログラミング演習2/python-test"
cd "$WORK_DIR"

if [ ! -d "w-venv" ]; then
  python3 -m venv w-venv
  source w-venv/bin/activate
  pip install requests urllib3
else
  source w-venv/bin/activate
fi

python3 web_scraping.py
ls -lh "$WORK_DIR"/last_script_03.txt
deactivate
