import bpy

bpy.ops.mesh.primitive_cone_add(vertices=64, location=(0,0,1))

bpy.ops.mesh.primitive_uv_sphere_add(segments=192, ring_count=128, size=0.81, location=(0, -0.15, 0.1))

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cone"]

bpy.context.object.modifiers["Boolean"].operation = "DIFFERENCE"
