bl_info = {
    "name": "Rigging Guide Addon",
    "blender": (3, 0, 0),
    "version": (1, 0, 0),
    "location": "View3D > Sidebar > Rigging Guide",
    "description": "Interactive step-by-step guidance for character rigging",
    "author": "Hemanth",
    "category": "Rigging",
    "support": "COMMUNITY",
    "doc_url": "https://github.com/hemanthhemanth5219-hue/blender-rigging-guide-addon",
    "tracker_url": "https://github.com/hemanthhemanth5219-hue/blender-rigging-guide-addon/issues",
}

import bpy
from bpy.props import IntProperty, StringProperty, BoolProperty
from . import ui, operators, guides

classes = [
    operators.RiggingGuideProperties,
    operators.NextStepOperator,
    operators.PreviousStepOperator,
    operators.ResetGuideOperator,
    ui.RiggingGuidePanel,
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    bpy.types.Scene.rigging_guide_index = IntProperty(
        name="Guide Index",
        description="Current step in the rigging guide",
        default=0,
        min=0
    )
    
    bpy.types.Scene.rigging_guide_type = StringProperty(
        name="Guide Type",
        description="Type of rigging guide",
        default="basic"
    )

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    if hasattr(bpy.types.Scene, 'rigging_guide_index'):
        del bpy.types.Scene.rigging_guide_index
    if hasattr(bpy.types.Scene, 'rigging_guide_type'):
        del bpy.types.Scene.rigging_guide_type

if __name__ == "__main__":
    register()
