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
class SY_PT_realtime_archviz_asset_pipeline_ui(Panel):
    bl_idname = "SY_PT_archviz_asset_pipeline"
    bl_label = 'ArchViz | AssetPipeline'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "SY | flow"

    @classmethod
    def poll(cls, context):
        return True

    def draw(self, context):
        layout = self.layout

        #Object
        box = layout.box()
        box.label(text='Object')
        col = box.column(align=True)
        # row = col.row(align=True)
        # row.prop(context.window_manager, 'RunAutoImport', text = '', icon = 'TRIA_DOWN')
        # row.operator('object.sy_auto_import', text = "Import")
        #row.prop(context.window_manager, 'RenameFile', text = '', icon = 'FILE_BLEND')
        row = col.row(align=True)
        row.prop(context.window_manager, 'RunMoveToCenter', text = '', icon = 'TRIA_DOWN')
        row.operator('object.sy_move_to_center', text = "Move to Center")
        row = col.row(align=True)
        row.prop(context.window_manager, 'RunUnparent', text = '', icon = 'TRIA_DOWN')
        row.operator('object.sy_unparent', text = "Unparent")
        row = col.row(align=True)
        row.prop(context.window_manager, 'RunRename', text = '', icon = 'TRIA_DOWN')
        row.operator('object.sy_fing_rename', text = "Rename")
        row = col.row(align=True)
        row.prop(context.window_manager, 'RunClean', text = '', icon = 'TRIA_DOWN')
        row.operator('object.sy_geometry_clean', text = "Clean")
        row = col.row(align=True)
        row.prop(context.window_manager, 'RunModifiers', text = '', icon = 'TRIA_DOWN')
        row.operator('object.sy_modifiers_polyred', text = "Add Modifiers")
        row.prop(context.window_manager, 'TargetDecimateCount', text = '')
        #row = col.row(align=True)
        #row.operator('object.sy_golden', text = 'We Are Golden!', icon = 'TRIA_RIGHT')

        #UV
        box = layout.box()
        box.label(text='UV')
        col = box.column(align=True)
        row = col.row(align=True)
        row.prop(context.window_manager, 'RunRewrapT', text = '', icon = 'SHADING_TEXTURE')
        row.prop(context.window_manager, 'RunRewrapL', text = '', icon = 'LIGHT_SUN')
        row.operator('object.sy_uv_full', text = 'Rewrap')
        row = col.row(align=True)
        row.prop(context.window_manager, 'RunIslands', text = '', icon = 'DOT')
        row.prop(context.window_manager, 'RunIslands', text = '', icon = 'LIGHT_SUN')
        row.operator('object.sy_uv_keep_groups', text = "UV from Islands")
        row = col.row(align=True)
        row.prop(context.window_manager, 'RunPackT', text = '', icon = 'SHADING_TEXTURE')
        row.prop(context.window_manager, 'RunPackL', text = '', icon = 'LIGHT_SUN')
        row.operator('object.sy_uv_islands', text = 'Pack')
        row.prop(context.window_manager, 'PackSize', text = '')
        row.prop(context.window_manager, 'PackRotate', text = '', icon = 'ZOOM_OUT')
        #row = col.row(align=True)
        #row.operator('object.sy_beat_so_funny', text = 'This Beat Is so Funny...', icon = 'TRIA_RIGHT')

        # #FullAuto
        # box = self.layout.box()
        # col = box.column(align=True)
        # row = col.row(align=True)
        # row.operator('object.sy_everything_awesome', text = 'Everything Is Awesome!', icon = 'TRIA_RIGHT')

        # #Export
        # box = self.layout.box()
        # box.label(text='Export')
        # col = box.column(align=True)
        # row = col.row(align=True)
        # #row.prop(context.window_manager, 'RunExportFBX', text = '', icon = 'TRIA_DOWN')
        # row.operator('object.sy_export_fbx', text = 'Export FBX')
        # row.prop(context.window_manager, 'ExportAnim', text = '', icon = 'POSE_HLT')



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

def register():
    init_properties()
    bpy.utils.register_class(SY_PT_realtime_archviz_asset_pipeline_ui)

def unregister():
    clear_properties()
    bpy.utils.unregister_class(SY_PT_realtime_archviz_asset_pipeline_ui)

if __name__ == "__main__":
    register()
