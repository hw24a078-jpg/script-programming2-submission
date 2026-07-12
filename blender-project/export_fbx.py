import bpy
import sys

input_file = sys.argv[-2]
output_file = sys.argv[-1]

# 資料の例と同じく、引数で指定した .blend を開いてから全オブジェクトを出力する。
bpy.ops.wm.open_mainfile(filepath=input_file)
bpy.ops.object.select_all(action="SELECT")
bpy.ops.export_scene.fbx(
    filepath=output_file,
    use_selection=True,
)

print(f"Exported FBX: {output_file}")
