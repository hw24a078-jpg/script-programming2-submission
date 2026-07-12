import bpy
import math
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
blend_path = os.path.join(project_dir, "jenkins_scene.blend")

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, 0))
floor = bpy.context.active_object
floor.name = "Floor"

bpy.ops.mesh.primitive_cube_add(location=(0, 0, 1))
cube = bpy.context.active_object
cube.name = "JenkinsCube"
cube.scale = (1.25, 1.25, 1.25)
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

bevel = cube.modifiers.new(name="SoftEdges", type="BEVEL")
bevel.width = 0.12
bevel.segments = 3

material = bpy.data.materials.new(name="CubeMaterial")
material.diffuse_color = (0.08, 0.42, 0.85, 1.0)
cube.data.materials.append(material)

bpy.ops.object.light_add(type="AREA", location=(4, -4, 6))
key_light = bpy.context.active_object
key_light.data.energy = 1100
key_light.data.shape = "DISK"
key_light.data.size = 5

bpy.ops.object.light_add(type="AREA", location=(-4, 2, 3))
fill_light = bpy.context.active_object
fill_light.data.energy = 550
fill_light.data.size = 4

bpy.ops.object.camera_add(location=(7, -7, 5), rotation=(math.radians(63), 0, math.radians(45)))
camera = bpy.context.active_object
bpy.context.scene.camera = camera

def point_camera_at(target):
    direction = target - camera.location
    camera.rotation_euler = direction.to_track_quat("-Z", "Y").to_euler()

point_camera_at(cube.location)

scene = bpy.context.scene
scene.render.engine = "BLENDER_EEVEE"
scene.render.resolution_x = 640
scene.render.resolution_y = 480
scene.render.resolution_percentage = 100
scene.render.image_settings.file_format = "PNG"
scene.world.color = (0.04, 0.04, 0.06)

bpy.ops.wm.save_as_mainfile(filepath=blend_path)
print(f"Saved scene: {blend_path}")
