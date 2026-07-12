#!/usr/bin/env bash
set -e

WORK_DIR="/Users/hw24a078/Desktop/スクリプトプログラミング演習2/python-test"
cd "$WORK_DIR"

if [ ! -d "venv" ]; then
  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade pip
  pip install pandas matplotlib plotly
else
  source venv/bin/activate
fi

export MPLCONFIGDIR="$WORK_DIR/.matplotlib"
mkdir -p "$MPLCONFIGDIR"
python3 01.py
python3 02.py
ls -lh "$WORK_DIR"/temperature.png "$WORK_DIR"/temperature.html
deactivate
