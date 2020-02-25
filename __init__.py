
bl_info = {
    "name": "SyArchViz",
    "author": "SG at Raumgleiter AG",
    "version": (1, 1),
    "blender": (2, 7, 9),
    "location": "View3D > Toolbar",
    "description": "This addon holds tools to optimize the workflow in real time archviz.",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Sy"}

if "bpy" in locals():
    import imp
    imp.reload(SyArchViz_Commands)
    imp.reload(SyArchViz_Tools)
    imp.reload(SyArchViz_AssetPipeline)
    print("Reloaded SyArchViz")
else:
    from . import SyArchViz_Commands, SyArchViz_Tools, SyArchViz_AssetPipeline
    print("Imported SyArchViz")


import bpy
from bpy.props import *

#************************************************************************************
# Register

def register():
    bpy.utils.register_module(__name__)
    
    SyArchViz_Tools.init_properties()
    SyArchViz_AssetPipeline.init_properties()
    
def unregister():
    bpy.utils.unregister_module(__name__)

    SyArchViz_Tools.clear_properties()
    SyArchViz_AssetPipeline.clear_properties()

def draw_item(self, context):
    layout = self.layout
                
if __name__ == "__main__":
    register()

