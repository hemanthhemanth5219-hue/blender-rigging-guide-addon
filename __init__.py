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
from . import ui, operators, guides, help_system

classes = [
    operators.RiggingGuideProperties,
    operators.NextStepOperator,
    operators.PreviousStepOperator,
    operators.ResetGuideOperator,
    ui.RiggingGuidePanel,
    help_system.RiggingAddonHelpOperator,
    help_system.RiggingAddonHelpPanel,
]

# Keymap storage
addon_keymaps = []

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
    
    # Register keymap for Shift+/
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Screen', space_type='EMPTY')
    kmi = km.keymap_items.new("wm.rigging_addon_help", 'SLASH', 'PRESS', shift=True)
    addon_keymaps.append((km, kmi))
    
    print("✓ Rigging Guide Addon registered successfully!")
    print("✓ Press N to open addon panel")
    print("✓ Press Shift+/ to open help system")

def unregister():
    # Unregister keymap
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    
    if hasattr(bpy.types.Scene, 'rigging_guide_index'):
        del bpy.types.Scene.rigging_guide_index
    if hasattr(bpy.types.Scene, 'rigging_guide_type'):
        del bpy.types.Scene.rigging_guide_type
    
    print("✓ Rigging Guide Addon unregistered")

if __name__ == "__main__":
    register()
