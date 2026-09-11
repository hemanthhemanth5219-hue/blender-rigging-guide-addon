import bpy
from bpy.types import Operator, PropertyGroup
from bpy.props import StringProperty, IntProperty

class RiggingGuideProperties(PropertyGroup):
    """Properties for rigging guides"""
    current_step: IntProperty(
        name="Current Step",
        description="Current step index",
        default=0
    )
    guide_name: StringProperty(
        name="Guide Name",
        description="Name of the current guide",
        default="Basic Rigging"
    )

class NextStepOperator(Operator):
    """Move to the next step in the rigging guide"""
    bl_idname = "rigging_guide.next_step"
    bl_label = "Next Step"
    
    def execute(self, context):
        scene = context.scene
        guides = get_current_guide(scene)
        
        if scene.rigging_guide_index < len(guides) - 1:
            scene.rigging_guide_index += 1
            self.report({'INFO'}, f"Step {scene.rigging_guide_index + 1} of {len(guides)}")
        else:
            self.report({'INFO'}, "You've completed this guide!")
        
        return {'FINISHED'}

class PreviousStepOperator(Operator):
    """Move to the previous step in the rigging guide"""
    bl_idname = "rigging_guide.previous_step"
    bl_label = "Previous Step"
    
    def execute(self, context):
        scene = context.scene
        guides = get_current_guide(scene)
        
        if scene.rigging_guide_index > 0:
            scene.rigging_guide_index -= 1
            self.report({'INFO'}, f"Step {scene.rigging_guide_index + 1} of {len(guides)}")
        else:
            self.report({'INFO'}, "You're at the first step")
        
        return {'FINISHED'}

class ResetGuideOperator(Operator):
    """Reset the guide to the beginning"""
    bl_idname = "rigging_guide.reset"
    bl_label = "Reset Guide"
    
    def execute(self, context):
        context.scene.rigging_guide_index = 0
        self.report({'INFO'}, "Guide reset to the beginning")
        return {'FINISHED'}

class CreateArmatureOperator(Operator):
    """Create a basic armature for rigging"""
    bl_idname = "rigging_guide.create_armature"
    bl_label = "Create Armature"
    
    def execute(self, context):
        bpy.ops.object.armature_add(enter_editmode=False, location=(0, 0, 0))
        self.report({'INFO'}, "Armature created. Ready for rigging!")
        return {'FINISHED'}

class SelectMeshOperator(Operator):
    """Select the mesh object for rigging"""
    bl_idname = "rigging_guide.select_mesh"
    bl_label = "Select Mesh"
    
    def execute(self, context):
        # Deselect all
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select mesh objects
        mesh_count = 0
        for obj in context.scene.objects:
            if obj.type == 'MESH':
                obj.select_set(True)
                context.view_layer.objects.active = obj
                mesh_count += 1
        
        if mesh_count > 0:
            self.report({'INFO'}, f"Selected {mesh_count} mesh object(s)")
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "No mesh objects found in scene")
            return {'CANCELLED'}

class ParentMeshToArmatureOperator(Operator):
    """Parent the mesh to the armature with automatic weights"""
    bl_idname = "rigging_guide.parent_mesh"
    bl_label = "Parent Mesh to Armature"
    
    def execute(self, context):
        # Check if we have both mesh and armature selected
        mesh_obj = None
        armature_obj = None
        
        for obj in context.selected_objects:
            if obj.type == 'MESH':
                mesh_obj = obj
            elif obj.type == 'ARMATURE':
                armature_obj = obj
        
        if not mesh_obj or not armature_obj:
            self.report({'ERROR'}, "Please select both mesh and armature")
            return {'CANCELLED'}
        
        # Set armature as active
        context.view_layer.objects.active = armature_obj
        
        # Parent with automatic weights
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')
        self.report({'INFO'}, "Mesh parented to armature with automatic weights")
        return {'FINISHED'}

def get_current_guide(scene):
    """Get the current guide based on scene settings"""
    guide_type = scene.rigging_guide_type
    
    if guide_type == "basic":
        return BASIC_RIGGING_GUIDE
    elif guide_type == "advanced":
        return ADVANCED_RIGGING_GUIDE
    elif guide_type == "facial":
        return FACIAL_RIGGING_GUIDE
    
    return BASIC_RIGGING_GUIDE

# Guide definitions
BASIC_RIGGING_GUIDE = [
    {
        "title": "Step 1: Import or Create a Model",
        "description": "Import your character model or create a simple mesh in Blender.",
        "tips": [
            "Ensure your model has proper topology",
            "Check that the model is centered at the origin",
            "Apply all transforms (Ctrl+A) before rigging"
        ]
    },
    {
        "title": "Step 2: Prepare the Mesh",
        "description": "Clean up your mesh and ensure it's properly prepared for rigging.",
        "tips": [
            "Remove duplicate vertices",
            "Ensure smooth normals",
            "Check for any holes in the mesh"
        ]
    },
    {
        "title": "Step 3: Create an Armature",
        "description": "Add an armature (skeleton) to your character.",
        "tips": [
            "Use Shift+A > Armature > Human",
            "Position the armature at the origin",
            "Scale the armature to fit your character"
        ],
        "action": "CREATE_ARMATURE"
    },
    {
        "title": "Step 4: Edit the Armature",
        "description": "Enter edit mode and adjust the bones to match your character's anatomy.",
        "tips": [
            "Press Tab to enter edit mode",
            "Use the proportional editing tool",
            "Ensure bones follow the character's joints"
        ]
    },
    {
        "title": "Step 5: Add Bone Constraints",
        "description": "Add constraints to control bone behavior.",
        "tips": [
            "Use IK (Inverse Kinematics) for limbs",
            "Add pole targets for better control",
            "Use limit constraints for realistic movement"
        ]
    },
    {
        "title": "Step 6: Parent Mesh to Armature",
        "description": "Link your mesh to the armature so it deforms with the bones.",
        "tips": [
            "Select mesh, then armature",
            "Press Ctrl+P and choose 'Armature Deform'",
            "Use automatic weights for quick setup"
        ],
        "action": "PARENT_MESH"
    },
    {
        "title": "Step 7: Weight Painting",
        "description": "Paint weights to control how each bone deforms the mesh.",
        "tips": [
            "Switch to Weight Paint mode",
            "Use red for high influence, blue for low",
            "Test your deformations as you paint"
        ]
    },
    {
        "title": "Step 8: Test Your Rig",
        "description": "Test your rig by posing the character.",
        "tips": [
            "Switch to Pose mode (Ctrl+Tab)",
            "Rotate bones to test deformation",
            "Adjust weights if needed"
        ]
    }
]

ADVANCED_RIGGING_GUIDE = [
    {
        "title": "Advanced: Step 1 - Facial Rig Setup",
        "description": "Set up a detailed facial rigging system.",
        "tips": ["Create control rigs for each facial feature"]
    },
    {
        "title": "Advanced: Step 2 - IK/FK Switching",
        "description": "Set up IK/FK switching for limbs.",
        "tips": ["Use drivers for smooth IK/FK blending"]
    },
    {
        "title": "Advanced: Step 3 - Control Rigs",
        "description": "Create intuitive control objects.",
        "tips": ["Use curves or custom shapes for controls"]
    }
]

FACIAL_RIGGING_GUIDE = [
    {
        "title": "Facial Rigging: Step 1 - Topology",
        "description": "Ensure your character has proper facial topology.",
        "tips": ["Follow natural muscle flow lines"]
    },
    {
        "title": "Facial Rigging: Step 2 - Eye Rig",
        "description": "Create eye controls and look-at targets.",
        "tips": ["Add bones for eye rotation and blink"]
    },
    {
        "title": "Facial Rigging: Step 3 - Mouth Rig",
        "description": "Set up mouth and lip controls.",
        "tips": ["Create blend shapes for phonemes"]
    }
]
