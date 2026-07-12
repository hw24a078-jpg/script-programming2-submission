#!/usr/bin/env bash
set -eu

WORK_DIR="${WORK_DIR:-$(cd "$(dirname "$0")" && pwd)}"
BLENDER="${BLENDER:-/Applications/Blender.app/Contents/MacOS/Blender}"
BLEND_FILE="$WORK_DIR/jenkins_scene.blend"
OUTPUT_DIR="$WORK_DIR/output"
TIMESTAMP=$(date +%Y%m%d_%H%M)

mkdir -p "$OUTPUT_DIR"

"$BLENDER" --background --python "$WORK_DIR/create_scene.py"
"$BLENDER" --background "$BLEND_FILE" \
  --render-output "$OUTPUT_DIR/render_${TIMESTAMP}_" \
  --render-format PNG \
  --render-frame 1
"$BLENDER" --background "$BLEND_FILE" \
  --python "$WORK_DIR/export_fbx.py" -- "$OUTPUT_DIR/jenkins_scene_${TIMESTAMP}.fbx"

ls -lh "$OUTPUT_DIR"
