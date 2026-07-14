#!/usr/bin/env bash
set -e

WORK_DIR="/Users/hw24a078/Desktop/スクリプトプログラミング演習2/python-test"
VENV="/Users/hw24a078/.jenkins/venvs/python-weather"
cd "$WORK_DIR"

if [ ! -d "$VENV" ]; then
  /usr/bin/python3 -m venv "$VENV"
  "$VENV/bin/python3" -m pip install --upgrade pip
  "$VENV/bin/python3" -m pip install pandas matplotlib plotly
fi

export MPLCONFIGDIR="$WORK_DIR/.matplotlib"
mkdir -p "$MPLCONFIGDIR"
"$VENV/bin/python3" 01.py
"$VENV/bin/python3" 02.py
ls -lh "$WORK_DIR"/temperature.png "$WORK_DIR"/temperature.html
