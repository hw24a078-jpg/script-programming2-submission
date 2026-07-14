#!/usr/bin/env bash
set -e

WORK_DIR="/Users/hw24a078/Desktop/スクリプトプログラミング演習2/python-test"
VENV="/Users/hw24a078/.jenkins/venvs/web-scraping"
cd "$WORK_DIR"

if [ ! -d "$VENV" ]; then
  /usr/bin/python3 -m venv "$VENV"
  "$VENV/bin/python3" -m pip install requests urllib3
fi

"$VENV/bin/python3" web_scraping.py
ls -lh "$WORK_DIR"/last_script_03.txt
