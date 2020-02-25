  
import bmesh
import bpy
import mathutils
import bgl
from bpy.types import Panel
from rna_prop_ui import PropertyPanel
from sys import float_info as fi
import os


##########################################################
# draw UI ButtonS
class realtime_archviz_ui(bpy.types.Panel):
    bl_idname = "ArchViz_Tools"
    bl_label = 'ArchViz'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    
    def __init__(self):
        pass

    @classmethod
    def poll(self, context):
        try:
            ob = context.active_object
            mode = context.mode
            return 1#(ob.type == 'MESH')
        except AttributeError:
            return 0
      
    def draw(self, context):

        layout = self.layout

        #Import
        box = self.layout.box()
        box.label(text='Import')
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator('object.sy_import_3ds_c4d', text = 'Fix: 3DS | C4D')


        #Architecture
        box = self.layout.box()
        box.label(text='Building')
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator('object.sy_building_clean', text = 'Clean')


        #Collision
        box = self.layout.box()
        box.label(text='Collision')
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator('object.sy_create_bounds', text = 'Create Bounds')
        row.operator('object.sy_split_bounds', text = 'Split Bounds')

        #Utility
        box = self.layout.box()
        box.label(text='Utility')
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator('object.sy_reduce_materials', text = "Reduce Materials")
        row.operator('object.sy_geometry_split', text = "Split by Material")
        row = col.row(align=True)
        row.operator('object.sy_clean_connections', text = "Fix FaceConnections")
        row.operator('object.sy_clean_all_connections', text = "Fix All")
        col = box.column(align=True)
        row = col.row(align=True)
        row.operator('object.sy_get_curve_length', text = "Print CurveLength")
        row.prop(context.window_manager, 'CurveLength', text = '')


        #Turn eachother on and off
        HasChanged = False
        if (not context.window_manager.OldIsland and context.window_manager.RunIslands):
            context.window_manager.RunRewrapT = False
            context.window_manager.RunRewrapL = False
            HasChanged = True
        elif (not context.window_manager.OldRewrapT and context.window_manager.RunRewrapT):
            context.window_manager.RunIslands = False
            HasChanged = True
        elif (not context.window_manager.OldRewrapL and context.window_manager.RunRewrapL):
            context.window_manager.RunIslands = False
            HasChanged = True

        #Save old bools
        if HasChanged:
            context.window_manager.OldRewrapT = context.window_manager.RunRewrapT
            context.window_manager.OldRewrapL = context.window_manager.RunRewrapL
            context.window_manager.OldIsland = context.window_manager.RunIslands


#************************************************************************************

# init properties
def init_properties():

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