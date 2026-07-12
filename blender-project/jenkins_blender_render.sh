#!/usr/bin/env bash
set -eu

WORK_DIR="/Users/hw24a078/Desktop/スクリプトプログラミング演習2/blender-project"
OUT_DIR="$WORK_DIR/output"
BLENDER_PATH="/Applications/Blender.app/Contents/MacOS/Blender"
BLEND_FILE="$WORK_DIR/jenkins_scene.blend"
TIMESTAMP=$(date +%Y%m%d_%H%M)
OUTPUT_NAME="jenkins_scene_${TIMESTAMP}"

mkdir -p "$OUT_DIR"

# 課題用の簡単なシーンをまだ保存していない場合だけ作成する。
if [ ! -f "$BLEND_FILE" ]; then
  "$BLENDER_PATH" --background --python "$WORK_DIR/create_scene.py"
fi

"$BLENDER_PATH" -b "$BLEND_FILE" \
  --python-expr "import bpy; bpy.context.scene.render.resolution_x=3840; bpy.context.scene.render.resolution_y=2160; bpy.context.scene.render.resolution_percentage=100" \
  -o "${OUT_DIR}/${OUTPUT_NAME}_" -F PNG -f 1

ls -lh "$OUT_DIR"/"${OUTPUT_NAME}"_*.png
