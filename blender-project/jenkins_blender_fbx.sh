#!/usr/bin/env bash
set -eu

WORK_DIR="/Users/hw24a078/Desktop/スクリプトプログラミング演習2/blender-project"
OUT_DIR="$WORK_DIR/output"
BLENDER_PATH="/Applications/Blender.app/Contents/MacOS/Blender"
INPUT="$WORK_DIR/jenkins_scene.blend"
OUTPUT="$OUT_DIR/jenkins_scene_$(date +%Y%m%d_%H%M).fbx"
SCRIPT="$WORK_DIR/export_fbx.py"

mkdir -p "$OUT_DIR"

if [ ! -f "$INPUT" ]; then
  "$BLENDER_PATH" --background --python "$WORK_DIR/create_scene.py"
fi

"$BLENDER_PATH" \
  --background \
  --python "$SCRIPT" -- "$INPUT" "$OUTPUT"

ls -lh "$OUTPUT"
