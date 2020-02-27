

import bmesh
import bpy
import mathutils
import bgl
from rna_prop_ui import PropertyPanel
from sys import float_info as fi
import os


#************************************************************************************
# SyGolden

class SY_OT_SyGolden(bpy.types.Operator):
    bl_idname = "object.sy_golden"
    bl_label = "We Are Golden (Sy)"

    def execute(self, context):

        if(context.window_manager.RunAutoImport):
            bpy.ops.object.sy_auto_import()
        if(context.window_manager.RunMoveToCenter):
            bpy.ops.object.sy_move_to_center()
        if(context.window_manager.RunUnparent):
            bpy.ops.object.sy_unparent()
        if(context.window_manager.RunRename):
            bpy.ops.object.sy_fing_rename()
        if(context.window_manager.RunClean):
            bpy.ops.object.sy_geometry_clean()
        if(context.window_manager.RunModifiers):
            bpy.ops.object.sy_modifiers_polyred()

        return {'FINISHED'}



#************************************************************************************
# SyBeatSoFunny

class SY_OT_SyBeatSoFunny(bpy.types.Operator):
    bl_idname = "object.sy_beat_so_funny"
    bl_label = "This Beat Is so Funny (Sy)"

    def execute(self, context):

        bpy.ops.object.sy_uv_full()
        if(context.window_manager.RunIslands):
            bpy.ops.object.sy_uv_keep_groups()
        bpy.ops.object.sy_uv_islands()

        return {'FINISHED'}



#************************************************************************************
# SyEverythingAwesome

class SY_OT_SyEverythingAwesome(bpy.types.Operator):
    bl_idname = "object.sy_everything_awesome"
    bl_label = "Everything Is Awesome (Sy)"

    def execute(self, context):

        bpy.ops.object.sy_golden()
        bpy.ops.object.sy_beat_so_funny()
        #if(context.window_manager.RunExportFBX):
        #    bpy.ops.object.sy_export_fbx()

        return {'FINISHED'}


#************************************************************************************
# SyAutoImport

class SY_OT_SyAutoImport(bpy.types.Operator):
    bl_idname = "object.sy_auto_import"
    bl_label = "Import export.fbx (Sy)"

    def execute(self, context):

        #Rename
        #if context.window_manager.RenameFile:
        #    os.path.
        #    bpy.ops.wm.save_as_mainfile(filepath = bpy.path.abspath("//hui.blend"))

        #Import
        bpy.ops.import_scene.fbx(filepath = bpy.path.abspath("//export.fbx"))

        return {'FINISHED'}


#************************************************************************************
# SyExportFBX

class SY_OT_SyExportFBX(bpy.types.Operator):
    bl_idname = "object.sy_export_fbx"
    bl_label = "Export FBX (Sy)"

    def execute(self, context):

        if context.window_manager.ExportAnim:
            bpy.ops.export_scene.fbx(filepath=bpy.data.filepath[:-6] + '.fbx', use_selection = True, object_types = {'MESH', 'ARMATURE', 'OTHER'},
                add_leaf_bones = True, bake_anim = True,
                axis_forward = '-Z', axis_up = 'Y', version = 'BIN7400', ui_tab = 'GEOMETRY', global_scale = 1.0, apply_unit_scale = True, bake_space_transform = False, use_mesh_modifiers = True, mesh_smooth_type = 'FACE', use_mesh_edges = False, use_tspace = False, use_custom_props = False, primary_bone_axis = 'Y', secondary_bone_axis = 'X', use_armature_deform_only = False, armature_nodetype = 'NULL', bake_anim_use_all_bones = True, bake_anim_use_nla_strips = True, bake_anim_use_all_actions = True, bake_anim_force_startend_keying = True, bake_anim_step = 1.0, bake_anim_simplify_factor = 1.0, use_anim = True, use_anim_action_all = True, use_default_take = True, use_anim_optimize = True, anim_optimize_precision = 6.0, path_mode = 'AUTO', embed_textures = False, batch_mode = 'OFF', use_batch_own_dir = True)
        else:
            bpy.ops.export_scene.fbx(filepath=bpy.data.filepath[:-6] + '.fbx', use_selection = True, object_types = {'MESH', 'ARMATURE', 'OTHER'},
                add_leaf_bones = False, bake_anim = False,
                axis_forward = '-Z', axis_up = 'Y', version = 'BIN7400', ui_tab = 'GEOMETRY', global_scale = 1.0, apply_unit_scale = True, bake_space_transform = False, use_mesh_modifiers = True, mesh_smooth_type = 'FACE', use_mesh_edges = False, use_tspace = False, use_custom_props = False, primary_bone_axis = 'Y', secondary_bone_axis = 'X', use_armature_deform_only = False, armature_nodetype = 'NULL', bake_anim_use_all_bones = True, bake_anim_use_nla_strips = True, bake_anim_use_all_actions = True, bake_anim_force_startend_keying = True, bake_anim_step = 1.0, bake_anim_simplify_factor = 1.0, use_anim = True, use_anim_action_all = True, use_default_take = True, use_anim_optimize = True, anim_optimize_precision = 6.0, path_mode = 'AUTO', embed_textures = False, batch_mode = 'OFF', use_batch_own_dir = True)

        bpy.ops.wm.save_mainfile()

        return {'FINISHED'}

#************************************************************************************
# SyMoveToCenter

class SY_OT_SyMoveToCenter(bpy.types.Operator):
    bl_idname = "object.sy_move_to_center"
    bl_label = "Move to Center (Sy)"

    def execute(self, context):

        if bpy.context.view_layer.objects.active == None:
            bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active


        #Deselect Children
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.parent is not None:
                    iObject.select = False;

        #Clear Location
        bpy.ops.object.location_clear()


        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}



#************************************************************************************
# SyUnparent

class SY_OT_SyUnparent(bpy.types.Operator):
    bl_idname = "object.sy_unparent"
    bl_label = "Unparent (Sy)"

    def execute(self, context):

        bpy.ops.object.mode_set(mode='OBJECT')

        #Save Selected Roots
        AllSelected = bpy.context.selected_objects

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:

                #Set Object Active
                bpy.context.view_layer.objects.active = iObject

                #Select Children, Unparent
                bpy.ops.object.select_grouped(type='CHILDREN_RECURSIVE')
                bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

                #Add to Selection
                AllSelected.extend(bpy.context.selected_objects)

            #Delete Empty
            bpy.ops.object.select_all(action='DESELECT')
            bpy.ops.object.select_by_type(type='EMPTY')
            bpy.ops.object.delete(use_global=False)

        #Restore selection
        if len(AllSelected) > 0:
            for iObject in AllSelected:
                iObject.select = True

        #Make sure something is active
        bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]

        return {'FINISHED'}


#************************************************************************************
# SyGeometryClean

class SY_OT_SyGeometryClean(bpy.types.Operator):
    bl_idname = "object.sy_geometry_clean"
    bl_label = "Clean Geometry (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active
        AlternativeSelection = SelectedAtStart

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Count Vertices
                    bpy.ops.object.mode_set(mode='EDIT')
                    Mesh = bmesh.from_edit_mesh(iObject.data)
                    SelectedVertices = [ v.index for v in Mesh.verts if v.select ]
                    CountSelectedVertices = len(SelectedVertices)
                    CountTotalVertices = len(iObject.data.vertices)

                    #Are there any vertices?
                    if CountTotalVertices == 0:
                        bpy.ops.object.mode_set(mode='OBJECT')
                        bpy.data.objects.remove(iObject, do_unlink = True)
                    else:
                        #Save Object as Alternative
                        AlternativeSelection = iObject

                        #Cleanup Geometry
                        bpy.ops.object.mode_set(mode='EDIT')
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.context.object.data.use_auto_smooth = False
                        bpy.ops.mesh.mark_sharp(clear=True)
                        bpy.ops.mesh.delete_loose()
                        bpy.ops.mesh.select_interior_faces()
                        bpy.ops.mesh.delete(type='FACE')

                        bpy.ops.object.mode_set(mode='OBJECT')
                        bpy.ops.object.shade_smooth()

                        #Clean ObjectSettings
                        bpy.context.object.data.use_auto_smooth = False

                else:
                    bpy.data.objects.remove(iObject, do_unlink = True)

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        if bpy.context.view_layer.objects.active == None:
            bpy.context.view_layer.objects.active = AlternativeSelection
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}

#************************************************************************************
# SyGeometrySplit

class SY_OT_SyGeometrySplit(bpy.types.Operator):
    bl_idname = "object.sy_geometry_split"
    bl_label = "Split Geometry (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    bpy.context.area.type = 'VIEW_3D'
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')

                    bpy.ops.mesh.separate(type='LOOSE')

                    bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}

#************************************************************************************
# SyModifiersBasic

class SY_OT_SyModifiersBasic(bpy.types.Operator):
    bl_idname = "object.sy_modifiers_basic"
    bl_label = "Apply Basic Modifiers (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Modifiers
                    if 0 == len([m for m in bpy.context.object.modifiers if m.type == "EDGE_SPLIT"]):
                        EdgeSplit = iObject.modifiers.new(name = "EdgeSplit", type='EDGE_SPLIT')
                        EdgeSplit.use_edge_angle = True
                        EdgeSplit.use_edge_sharp = True
                    if 0 == len([m for m in bpy.context.object.modifiers if m.type == "TRIANGULATE"]):
                        bpy.ops.object.modifier_add(type='TRIANGULATE')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}

#************************************************************************************
# SyModifiersPolyred

class SY_OT_SyModifiersPolyred(bpy.types.Operator):
    bl_idname = "object.sy_modifiers_polyred"
    bl_label = "Apply Polyred Modifiers (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Modifiers

                    #Split
                    if 0 == len([m for m in bpy.context.object.modifiers if m.type == "EDGE_SPLIT"]):
                        bpy.ops.object.modifier_add(type='EDGE_SPLIT')
                        bpy.context.object.modifiers["EdgeSplit"].use_edge_angle = True
                        bpy.context.object.modifiers["EdgeSplit"].use_edge_sharp = True

                    #Decimate
                    if 0 == len([m for m in bpy.context.object.modifiers if m.type == "DECIMATE"]):
                        bpy.ops.object.modifier_add(type='DECIMATE')

                    CountTotalVertices = len(iObject.data.vertices)
                    if CountTotalVertices > bpy.context.window_manager.TargetDecimateCount:
                        DecimateRatio = (bpy.context.window_manager.TargetDecimateCount / CountTotalVertices) / 2
                        bpy.context.object.modifiers["Decimate"].ratio = DecimateRatio

                    #Triangulate
                    if 0 == len([m for m in bpy.context.object.modifiers if m.type == "TRIANGULATE"]):
                        bpy.ops.object.modifier_add(type='TRIANGULATE')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}

#************************************************************************************
# SyUVFull

class SY_OT_SyUVFull(bpy.types.Operator):
    bl_idname = "object.sy_uv_full"
    bl_label = "Full UV Rewrap (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Set right Mode and select
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')

                    #Make sure at least two UVs exist
                    UVLayerCount = len(bpy.context.object.data.uv_textures)
                    if UVLayerCount < 1:
                        bpy.ops.mesh.uv_texture_add()
                    if UVLayerCount < 2:
                        bpy.ops.mesh.uv_texture_add()

                    #Go through Layers
                    if context.window_manager.RunRewrapT:
                        bpy.context.object.data.uv_textures[0].active = True
                        bpy.ops.uv.smart_project(island_margin = 0.1, stretch_to_bounds=False)
                    if context.window_manager.RunRewrapL:
                        bpy.context.object.data.uv_textures[1].active = True
                        bpy.ops.uv.smart_project(island_margin = 0.1, stretch_to_bounds=True)

                    #Return to StartMode
                    bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}

#************************************************************************************
# SyUVKeepGroups

class SY_OT_SyUVKeepGroups(bpy.types.Operator):
    bl_idname = "object.sy_uv_keep_groups"
    bl_label = "Rewrap UV by Groups (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Duplicate UV
                    if len(bpy.context.object.data.uv_textures) < 2:
                        bpy.ops.mesh.uv_texture_add()

                    #Remap
                    bpy.ops.object.mode_set(mode='EDIT')

                    bpy.context.area.type = 'IMAGE_EDITOR'
                    bpy.context.area.spaces.active.image = None
                    bpy.ops.uv.select_all(action='SELECT')
                    bpy.ops.uv.seams_from_islands()

                    bpy.context.area.type = 'VIEW_3D'
                    bpy.ops.uv.unwrap(method='CONFORMAL', margin=0.1)

                    bpy.context.area.type = 'IMAGE_EDITOR'
                    bpy.context.area.spaces.active.image = None
                    bpy.ops.uv.pack_islands(margin=0.1)
                    bpy.context.area.type = 'VIEW_3D'

                    bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}

#************************************************************************************
# SyRepackIslands

class SY_OT_SyRepackIslands(bpy.types.Operator):
    bl_idname = "object.sy_uv_islands"
    bl_label = "Pack Islands (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Set right Mode and select
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')

                    #Prepare PackIslands
                    bpy.context.area.type = 'IMAGE_EDITOR'
                    bpy.context.area.spaces.active.image = None

                    #Pack Layers
                    if context.window_manager.RunPackT:
                        bpy.context.object.data.uv_textures[0].active = True
                        bpy.ops.uv.select_all(action='SELECT')
                        bpy.ops.uv.pack_islands(rotate= not context.window_manager.PackRotate, margin=context.window_manager.PackSize)
                    if context.window_manager.RunPackL:
                        bpy.context.object.data.uv_textures[1].active = True
                        bpy.ops.uv.select_all(action='SELECT')
                        bpy.ops.uv.pack_islands(rotate= not context.window_manager.PackRotate, margin=context.window_manager.PackSize)

                    #Return to StartMode
                    bpy.context.area.type = 'VIEW_3D'
                    bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.view_layer.objects.active = SelectedAtStart

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}


#************************************************************************************
# SyFingRename

class SY_OT_SyFingRename(bpy.types.Operator):
    bl_idname = "object.sy_fing_rename"
    bl_label = "Fing Rename (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Rename
                    bpy.context.object.name = bpy.context.object.name[:3]
            bpy.context.view_layer.objects.active = SelectedAtStart

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}


#************************************************************************************
# Unparent from Empty

class SY_OT_SyCreateBounds(bpy.types.Operator):
    bl_idname = "object.sy_create_bounds"
    bl_label = "Create Bounding Boxes (Sy)"

    def execute(self, context):

        selected = bpy.context.selected_objects

        for obj in selected:
            #ensure origin is centered on bounding box center
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
            #create a cube for the bounding box
            bpy.ops.mesh.primitive_cube_add()
            #our new cube is now the active object, so we can keep track of it in a variable:
            bound_box = bpy.context.active_object

            #copy transforms
            bound_box.dimensions = obj.dimensions
            bound_box.location = obj.location
            bound_box.rotation_euler = obj.rotation_euler

            #rename
            bound_box.name = "UBX_" + bound_box.name + "_.000"

        #select old
        bpy.ops.object.select_all(action='DESELECT')
        for obj in selected:
            obj.select = True



        return {'FINISHED'}


#************************************************************************************
# Unparent from Empty

class SY_OT_SySplitBounds(bpy.types.Operator):
    bl_idname = "object.sy_split_bounds"
    bl_label = "Split along Seam (Sy)"

    def execute(self, context):

        bpy.ops.mesh.rip('INVOKE_DEFAULT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.edge_face_add()
        bpy.ops.mesh.f2()
        bpy.ops.mesh.separate(type='LOOSE')
        bpy.ops.object.mode_set(mode='OBJECT')


        return {'FINISHED'}


#************************************************************************************
# Clean All Connections

class SY_OT_SyCleanAllConnections(bpy.types.Operator):
    bl_idname = "object.sy_clean_all_connections"
    bl_label = "Cleans all Face Connections (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Mode
                    bpy.ops.object.mode_set(mode='EDIT')

                    #Clean all
                    IsDone = False;
                    while not IsDone:
                        #Hide selected faces
                        bpy.ops.mesh.hide(unselected=False)

                        #Still Polys visible?
                        Mesh = bmesh.from_edit_mesh(iObject.data)
                        UnhiddenPolys = [f for f in Mesh.faces if f.hide == False]
                        if len(UnhiddenPolys) == 0:
                            IsDone = True;
                        else:
                            #Select random face
                            UnhiddenPolys[0].select = True;

                            #Run CleanConnections
                            bpy.ops.object.sy_clean_connections()

                            #Hide Faces
                            bpy.ops.mesh.hide(unselected=False)

                    #Unhide all
                    bpy.ops.mesh.reveal()


                    #Mode
                    bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}


#************************************************************************************
# Clean Connections

class SY_OT_SyCleanConnections(bpy.types.Operator):
    bl_idname = "object.sy_clean_connections"
    bl_label = "Cleans Face Connections (Sy)"

    def execute(self, context):

        #Get Data
        iObject = bpy.context.view_layer.objects.active

        #FaceMode
        bpy.ops.mesh.select_mode(type="FACE") #VERT EDGE

        #Linked
        bpy.ops.mesh.select_linked(delimit={'SEAM'})

        #Save selected
        Mesh = bmesh.from_edit_mesh(iObject.data)
        SelectedFaces = [f for f in Mesh.faces if f.select == True]

        #Duplicate
        bpy.ops.mesh.duplicate()

        #Hide
        bpy.ops.mesh.hide(unselected=False)

        #Reselect
        for f in SelectedFaces:
            f.select = True

        #Delete
        bpy.ops.mesh.delete(type='FACE')

        #Unhide
        bpy.ops.mesh.reveal()

        return {'FINISHED'}


#************************************************************************************
# Reduce Materials

class SY_OT_SyReduceMaterials(bpy.types.Operator):
    bl_idname = "object.sy_reduce_materials"
    bl_label = "Reduce Materials (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Go through Materials
                    IsDone = False;
                    CurrentMaterialID = 0
                    while not IsDone:
                        #Mode
                        bpy.ops.object.mode_set(mode='EDIT')
                        bpy.ops.mesh.select_mode(type="FACE")

                        #Deselect Mesh
                        bpy.ops.mesh.select_all(action='DESELECT')

                        #Select Current Material
                        bpy.context.object.active_material_index = CurrentMaterialID

                        #Select Assigned
                        bpy.ops.object.material_slot_select()

                        #Mode
                        bpy.ops.object.mode_set(mode='OBJECT')

                        #Get selected
                        FoundSelectedMesh = False
                        for p in iObject.data.polygons:
                            if p.select == True:
                                FoundSelectedMesh = True
                                break

                        #Found?
                        if FoundSelectedMesh == True:
                            #Iterate
                            CurrentMaterialID += 1
                        else:
                            bpy.ops.object.material_slot_remove()

                        #Next Slot exists?
                        if CurrentMaterialID >= len(iObject.data.materials):
                            IsDone = True


        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}


#************************************************************************************
# Reduce Materials

class SY_OT_SyBuildingClean(bpy.types.Operator):
    bl_idname = "object.sy_import_3ds_c4d"
    bl_label = "Import 3DS from C4D (Sy)"

    def execute(self, context):

        bpy.ops.object.location_clear()
        bpy.ops.object.rotation_clear()
        bpy.ops.object.scale_clear()

        return {'FINISHED'}



#************************************************************************************
# Reduce Materials

class SY_OT_SyBuildingClean(bpy.types.Operator):
    bl_idname = "object.sy_building_clean"
    bl_label = "Building Clean (Sy)"

    def execute(self, context):

        ModeAtStart = bpy.context.object.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        SelectedAtStart = bpy.context.view_layer.objects.active

        #Iterate through Objects
        ObjectsToSetUp = bpy.context.selected_objects
        if len(ObjectsToSetUp) > 0:
            for iObject in ObjectsToSetUp:
                if iObject.type == 'MESH':
                    #Mode
                    bpy.ops.object.mode_set(mode='EDIT')

                    #Set Object Active
                    bpy.context.view_layer.objects.active = iObject

                    #Remove Degenerates
                    bpy.ops.mesh.dissolve_degenerate()

                    #Fix FaceConnections
                    bpy.ops.object.sy_clean_all_connections()


        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = SelectedAtStart
        bpy.ops.object.mode_set(mode = ModeAtStart)

        return {'FINISHED'}


#************************************************************************************
# GetCurveLength

class SY_OT_SyGetCurveLength(bpy.types.Operator):
    bl_idname = "object.sy_get_curve_length"
    bl_label = "Get CurveLength (Sy)"

    def execute(self, context):

        context = bpy.context
        aobj = context.active_object
        me = aobj.data
        mat = aobj.matrix_world
        scn = context.scene

        me.resolution_u = 48

        mesh = aobj.to_mesh(scene=scn,apply_modifiers=True,settings='PREVIEW')

        bm = bmesh.new()
        bm.from_mesh(mesh, face_normals=True, use_shape_key=True)

        length = 0
        for edge in bm.edges:
            length += edge.calc_length()

        print (length)
        context.window_manager.CurveLength = length;

        return {'FINISHED'}


#************************************************************************************

# init properties
def init_properties():

    bpy.types.WindowManager.RunMoveToCenter = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.RunAutoImport = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.RenameFile = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.RunUnparent = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.RunRename = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.RunClean = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.RunModifiers = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.TargetDecimateCount = bpy.props.FloatProperty(default=200000)
    bpy.types.WindowManager.RunRewrapT = bpy.props.BoolProperty(default=False)
    bpy.types.WindowManager.RunRewrapL = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.RunIslands = bpy.props.BoolProperty(default=False)
    bpy.types.WindowManager.RunPackT = bpy.props.BoolProperty(default=False)
    bpy.types.WindowManager.RunPackL = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.PackSize = bpy.props.FloatProperty(default=0.05, step=1)
    bpy.types.WindowManager.PackRotate = bpy.props.BoolProperty(default=False)
    bpy.types.WindowManager.OldRewrapT = bpy.props.BoolProperty(default=False)
    bpy.types.WindowManager.OldRewrapL = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.OldIsland = bpy.props.BoolProperty(default=False)
    bpy.types.WindowManager.RunExportFBX = bpy.props.BoolProperty(default=True)
    bpy.types.WindowManager.ExportAnim = bpy.props.BoolProperty(default=False)
    bpy.types.WindowManager.CurveLength = bpy.props.FloatProperty(default=0.00, step=1)

# clear properties
def clear_properties():
    props = ['RunAutoImport', 'RenameFile', 'RunMoveToCenter', 'RunUnparent', 'RunRename', 'RunClean', 'RunModifiers', 'TargetDecimateCount', 'RunRewrapT', 'RunRewrapL', 'RunIslands', 'RunPackT', 'RunPackL', 'PackSize', 'PackRotate', 'OldRewrapT', 'OldRewrapL', 'OldIsland', 'RunExportFBX', 'ExportAnim', 'CurveLength']
    for p in props:
        if bpy.context.window_manager.get(p) != None:
            del bpy.context.window_manager[p]
        try:
            x = getattr(bpy.types.WindowManager, p)
            del x
        except:
            pass
