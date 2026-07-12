#!/usr/bin/env bash
set -eu

WORK_DIR="${WORK_DIR:-$(cd "$(dirname "$0")" && pwd)}"
VENV_DIR="${VENV_DIR:-.venv-submit}"
cd "$WORK_DIR"

export MPLCONFIGDIR="${MPLCONFIGDIR:-$WORK_DIR/.matplotlib}"
mkdir -p "$MPLCONFIGDIR"

if [ ! -x "$VENV_DIR/bin/python" ]; then
  python3 -m venv "$VENV_DIR"
fi

"$VENV_DIR/bin/python" -m pip install --disable-pip-version-check -r requirements.txt

"$VENV_DIR/bin/python" 01.py
"$VENV_DIR/bin/python" 02.py
"$VENV_DIR/bin/python" web_scraping.py

ls -l temperature.png temperature.html last_script_03.txt
