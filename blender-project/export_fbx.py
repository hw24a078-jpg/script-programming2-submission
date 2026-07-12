import bpy
import os
import sys

args = sys.argv[sys.argv.index("--") + 1:]
output_path = os.path.abspath(args[0])

bpy.ops.object.select_all(action="SELECT")
bpy.ops.export_scene.fbx(
    filepath=output_path,
    use_selection=False,
    add_leaf_bones=False,
    axis_forward="-Z",
    axis_up="Y",
)

print(f"Exported FBX: {output_path}")
