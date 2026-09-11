"""
Help System for Blender Rigging Guide Addon
Displays comprehensive rigging information and keyboard shortcuts when triggered
"""

import bpy
from bpy.types import Operator, Panel
from bpy.props import StringProperty

# Help Text Database
HELP_CONTENT = {
    "QUICK_START": """
╔════════════════════════════════════════════════════════════╗
║     BLENDER RIGGING GUIDE ADDON - QUICK START            ║
╚════════════════════════════════════════════════════════════╝

ESSENTIAL KEYS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Press N          → Open/Close Addon Panel
Press Tab        → Enter/Exit Edit Mode
Press Ctrl+Tab   → Enter Pose Mode
Press G          → Move/Grab
Press R          → Rotate
Press S          → Scale

ADDON FEATURES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ Basic Rigging Guide (8 steps)
✓ Advanced Rigging Guide (5 steps)
✓ Facial Rigging Guide (6 steps)
✓ One-Click Armature Creation
✓ Automatic Mesh Parenting
✓ Weight Paint Guidance
✓ Constraint Tips & Tricks
✓ Complete Keyboard Reference

TYPE '/help' in console for full reference...
""",

    "NAVIGATION": """
╔════════════════════════════════════════════════════════════╗
║              NAVIGATION & VIEW SHORTCUTS                   ║
╚════════════════════════════════════════════════════════════╝

MOUSE & VIEW:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Middle Mouse Drag     → Rotate View
Scroll Wheel          → Zoom In/Out
Shift + Scroll        → Pan View
Numpad 7              → Top View
Numpad 1              → Front View
Numpad 3              → Side View
Numpad 0              → Camera View
. (Period)            → Frame Selected
Home                  → Frame All

SELECTION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Right Click           → Select Single
A                     → Select All
Alt+A                 → Deselect All
B                     → Box Select
C                     → Circle Select
Shift+F               → Lasso Select
Shift+Click           → Add to Selection
Alt+Click             → Select Edge Loops
""",

    "TRANSFORM": """
╔════════════════════════════════════════════════════════════╗
║            TRANSFORM & MODIFY SHORTCUTS                    ║
╚════════════════════════════════════════════════════════════╝

TRANSFORMATION:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
G                     → Grab/Move
R                     → Rotate
S                     → Scale
X                     → Constrain to X-axis
Y                     → Constrain to Y-axis
Z                     → Constrain to Z-axis
Shift+Z               → Constrain to XY-plane

CLEAR TRANSFORMS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Alt+R                 → Clear Rotation
Alt+G                 → Clear Location
Alt+S                 → Clear Scale
Ctrl+A                → Apply Transforms

EDIT MODE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
E                     → Extrude
Shift+D               → Duplicate
X                     → Delete
F                     → Create Face/Edge
Alt+M                 → Merge
1,2,3                 → Change Bone Width
""",

    "MODES": """
╔════════════════════════════════════════════════════════════╗
║                   MODE SWITCHING                           ║
╚════════════════════════════════════════════════════════════╝

MODE CONTROLS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tab                   → Toggle Edit/Object Mode
Ctrl+Tab              → Toggle Pose Mode
Z                     → Shade Mode Menu
Z + Z                 → Wireframe Toggle
Z + S                 → Solid Mode
Z + M                 → Material Preview

RIGGING WORKFLOW:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Object Mode           → Select & Organize
Edit Mode (Tab)       → Modify Bone Structure
Pose Mode (Ctrl+Tab)  → Test & Animate
Weight Paint          → Paint Bone Influence
Sculpt Mode           → Optional Shape Adjustment
""",

    "RIGGING": """
╔════════════════════════════════════════════════════════════╗
║                 RIGGING SPECIFIC KEYS                      ║
╚════════════════════════════════════════════════════════════╝

BONE OPERATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
E                     → Extrude Bone
Shift+D               → Duplicate Bone
Ctrl+J                → Join Bones
Alt+Click             → Select Bone Chain
L                     → Select Linked

PARENTING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ctrl+P                → Set Parent
Alt+P                 → Clear Parent
Shift+Ctrl+C          → Set Origin

CONSTRAINTS & POSE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
I                     → Insert Keyframe
Alt+I                 → Delete Keyframe
Ctrl+H                → Create Pole Target

WEIGHT PAINT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
F                     → Brush Size
Shift+F               → Brush Strength
Ctrl+F                → Brush Falloff
X                     → Flip Weight
W + A                 → Average Weights
W + G                 → Gradient Weights
W + C                 → Clean Weights
""",

    "ADDON": """
╔════════════════════════════════════════════════════════════╗
║            RIGGING ADDON CAPABILITIES                      ║
╚════════════════════════════════════════════════════════════╝

QUICK ACCESS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
N                     → Open/Close Addon Panel
Shift+/               → Show This Help System

ADDON GUIDES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━��━━━━━━━━━━━━━━━━━━━━━━━━━

📚 BASIC RIGGING GUIDE (8 Steps)
   Step 1: Import/Create Model
   Step 2: Prepare Mesh
   Step 3: Create Armature
   Step 4: Edit Armature
   Step 5: Add Constraints
   Step 6: Parent Mesh
   Step 7: Weight Paint
   Step 8: Test & Refine

📚 ADVANCED RIGGING GUIDE (5 Steps)
   Step 1: Control Rigs
   Step 2: IK/FK Switching
   Step 3: Facial Rig Setup
   Step 4: Custom Properties
   Step 5: Bone Organization

📚 FACIAL RIGGING GUIDE (6 Steps)
   Step 1: Topology Analysis
   Step 2: Eye Rig
   Step 3: Mouth & Lips
   Step 4: Expression Controls
   Step 5: Bone Constraints
   Step 6: Testing & Refinement

ADDON TOOLS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Create Armature (One Click)
✓ Parent Mesh to Armature
✓ Quick Mode Switching
✓ Weight Paint Guidance
✓ Constraint Setup Helper
✓ Testing Checklist
✓ Best Practices Reference
""",

    "WORKFLOW": """
╔════════════════════════════════════════════════════════════╗
║              RECOMMENDED RIGGING WORKFLOW                  ║
╚════════════════════════════════════════════════════════════╝

BASIC CHARACTER RIG (2-4 Hours):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. PREPARE
   • Open Blender
   • Import/Create Model
   • Press Ctrl+A → Apply Transforms
   • Select All + Alt+M → Merge Duplicates

2. OPEN ADDON
   • Press N → Open Addon Panel
   • Select "Basic" Guide
   • Read Step 1

3. CREATE ARMATURE
   • Shift+A → Armature → Human
   • OR Use Addon Button
   • Position Armature

4. EDIT BONES
   • Press Tab → Edit Mode
   • Move Bones to Match Model
   • Follow Addon Step 4 Guide

5. ADD CONSTRAINTS
   • Tab → Back to Object
   • Ctrl+Tab → Pose Mode
   • Select Bone → Add Constraints
   • Follow Addon Step 5

6. PARENT MESH
   • Select Mesh → Select Armature (Shift+Click)
   • Press Ctrl+P → Armature Deform
   • OR Use Addon Button

7. WEIGHT PAINT
   • Tab → Weight Paint Mode
   • Select Bone
   • Paint Influence
   • Press F to Change Size
   • Follow Addon Step 7

8. TEST
   • Ctrl+Tab → Pose Mode
   • Rotate Bones (R Key)
   • Check Deformations
   • Adjust Weights as Needed

EFFICIENT KEYBOARD WORKFLOW:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Shift+/      → Reference This Guide
N            → Open Addon
Tab          → Edit Mode
Ctrl+Tab     → Pose Mode
G, R, S      → Transform Bones
Ctrl+P       → Parent
F            → Brush Size
Spacebar     → Play Animation
""",

    "TIPS": """
╔════════════════════════════════════════════════════════════╗
║          PRO TIPS & BEST PRACTICES                         ║
╚════════════════════════════════════════════════════════════╝

BEFORE YOU START:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Good topology (quads recommended)
✓ Model centered at origin
✓ All transforms applied
✓ No loose geometry

DURING RIGGING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Name bones clearly
✓ Use bone layers to organize
✓ Test frequently (Ctrl+Tab)
✓ Use symmetry when possible
✓ Save often (Ctrl+S)

WEIGHT PAINTING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Use smooth brush for blending
✓ Start with large brush (F key)
✓ Test each bone after painting
✓ Use mirror tool (M key)
✓ Normalize weights (W + N)

COMMON MISTAKES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✗ Not applying transforms
✗ Poor bone positioning
✗ Unsmooth weight transitions
✗ Missing bone constraints
✗ Not testing extreme poses
✗ Inconsistent bone naming

SHORTCUTS TO REMEMBER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ctrl+Z        → Undo
Ctrl+Y        → Redo
Ctrl+S        → Save
Shift+/       → Show This Help
""",
}

class RiggingAddonHelpOperator(Operator):
    """Display Rigging Addon Help System"""
    bl_idname = "wm.rigging_addon_help"
    bl_label = "Rigging Addon Help"
    
    help_section: StringProperty(default="QUICK_START")
    
    def execute(self, context):
        print("\n" + "="*60)
        print(HELP_CONTENT.get(self.help_section, HELP_CONTENT["QUICK_START"]))
        print("="*60 + "\n")
        return {'FINISHED'}


class RiggingAddonHelpPanel(Panel):
    """Help Panel for Rigging Addon"""
    bl_label = "Rigging Addon Help"
    bl_idname = "VIEW3D_PT_rigging_help"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Rigging Help"
    
    def draw(self, context):
        layout = self.layout
        
        # Title
        layout.label(text="Rigging Addon Help System", icon='HELP')
        layout.separator()
        
        # Quick Access Buttons
        row = layout.row()
        row.operator("wm.rigging_addon_help", text="Quick Start").help_section = "QUICK_START"
        row = layout.row()
        row.operator("wm.rigging_addon_help", text="Navigation").help_section = "NAVIGATION"
        row = layout.row()
        row.operator("wm.rigging_addon_help", text="Transform").help_section = "TRANSFORM"
        row = layout.row()
        row.operator("wm.rigging_addon_help", text="Modes").help_section = "MODES"
        
        layout.separator()
        
        row = layout.row()
        row.operator("wm.rigging_addon_help", text="Rigging Keys").help_section = "RIGGING"
        row = layout.row()
        row.operator("wm.rigging_addon_help", text="Addon Features").help_section = "ADDON"
        row = layout.row()
        row.operator("wm.rigging_addon_help", text="Workflow").help_section = "WORKFLOW"
        row = layout.row()
        row.operator("wm.rigging_addon_help", text="Pro Tips").help_section = "TIPS"


def register_help_system():
    """Register help system classes"""
    bpy.utils.register_class(RiggingAddonHelpOperator)
    bpy.utils.register_class(RiggingAddonHelpPanel)
    
    # Register Shift+/ hotkey
    if not hasattr(bpy.app, 'rigging_addon_keymap_registered'):
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='Screen', space_type='EMPTY')
        kmi = km.keymap_items.new("wm.rigging_addon_help", 'SLASH', 'PRESS', shift=True)
        bpy.app.rigging_addon_keymap_registered = True


def unregister_help_system():
    """Unregister help system classes"""
    bpy.utils.unregister_class(RiggingAddonHelpOperator)
    bpy.utils.unregister_class(RiggingAddonHelpPanel)


if __name__ == "__main__":
    register_help_system()
    print("Rigging Addon Help System loaded!")
    print("Press Shift+/ in Blender to open help!")
