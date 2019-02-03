import bpy

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

bpy.ops.mesh.primitive_cone_add(vertices=64, location=(0,0,1))

bpy.ops.mesh.primitive_uv_sphere_add(segments=192, ring_count=128, size=0.81, location=(0, -0.15, 0.1))

bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cone"]

bpy.context.object.modifiers["Boolean"].operation = "DIFFERENCE"

bpy.ops.mesh.primitive_uv_sphere_add(size=0.6, location=(0.49, 0, -0.3) )

bpy.ops.object.shade_smooth()

bpy.ops.object.modifier_add(type="ARRAY")
bpy.context.object.modifiers["Array"].use_relative_offset = False
bpy.context.object.modifiers["Array"].use_constant_offset = True
bpy.context.object.modifiers["Array"].constant_offset_displace[0] = -0.98

# object = bpy.data.objects['Sphere'].select = True
# bpy.context.scene.objects.active = bpy.data.objects['Sphere']
# print(bpy.ops.object.select_pattern(pattern="Sphere")
# bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(2.23, -8.06, 0.18), "constraint_axis":(False, False, True), "contraint_orientation":'NORMAL', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap_target":'CLOSEST'})

bpy.ops.mesh.primitive_uv_sphere_add(size=0.2, location=(0.15, -0.8, 0.35))
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["Array"].use_relative_offset = False
bpy.context.object.modifiers["Array"].use_constant_offset = True
bpy.context.object.modifiers["Array"].constant_offset_displace[0] = -0.35