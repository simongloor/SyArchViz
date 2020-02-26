bl_info = {
    "name": "SyArchViz",
    "author": "SG at Raumgleiter AG",
    "category": "Pillars of SY",
    "version": (1, 1, 0),
    "blender": (2, 80, 0),
    "description": "This addon holds tools to optimize the workflow in real time archviz."
    }

if "bpy" in locals():
    import imp
    imp.reload(SyArchViz_Commands)
    imp.reload(SyArchViz_Tools)
    imp.reload(SyArchViz_AssetPipeline)
    print("Reloaded SyArchViz")
else:
    from . import (SyArchViz_Commands,
    SyArchViz_Tools,
    SyArchViz_AssetPipeline)
    print("Imported SyArchViz")


import bpy
from bpy.props import *

#************************************************************************************
# Register

classes = (
    SyArchViz_Commands.SY_OT_SyGolden,
    SyArchViz_Commands.SY_OT_SyBeatSoFunny,
    SyArchViz_Commands.SY_OT_SyEverythingAwesome,
    SyArchViz_Commands.SY_OT_SyAutoImport,
    SyArchViz_Commands.SY_OT_SyExportFBX,
    SyArchViz_Commands.SY_OT_SyMoveToCenter,
    SyArchViz_Commands.SY_OT_SyUnparent,
    SyArchViz_Commands.SY_OT_SyGeometryClean,
    SyArchViz_Commands.SY_OT_SyGeometrySplit,
    SyArchViz_Commands.SY_OT_SyModifiersBasic,
    SyArchViz_Commands.SY_OT_SyModifiersPolyred,
    SyArchViz_Commands.SY_OT_SyUVFull,
    SyArchViz_Commands.SY_OT_SyUVKeepGroups,
    SyArchViz_Commands.SY_OT_SyRepackIslands,
    SyArchViz_Commands.SY_OT_SyFingRename,
    SyArchViz_Commands.SY_OT_SyCreateBounds,
    SyArchViz_Commands.SY_OT_SySplitBounds,
    SyArchViz_Commands.SY_OT_SyCleanAllConnections,
    SyArchViz_Commands.SY_OT_SyCleanConnections,
    SyArchViz_Commands.SY_OT_SyReduceMaterials,
    SyArchViz_Commands.SY_OT_SyBuildingClean,
    SyArchViz_Commands.SY_OT_SyGetCurveLength,
    SyArchViz_Tools.SY_PT_realtime_archviz_ui,
    SyArchViz_AssetPipeline.SY_PT_realtime_archviz_asset_pipeline_ui,
    )

# register, unregister = bpy.utils.register_classes_factory(classes)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    SyArchViz_Tools.init_properties()
    SyArchViz_AssetPipeline.init_properties()

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    SyArchViz_Tools.clear_properties()
    SyArchViz_AssetPipeline.clear_properties()


def draw_item(self, context):
    layout = self.layout

# if __name__ == "__main__":
#     register()
