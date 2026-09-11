import bpy
from bpy.types import Panel
from . import operators

class RiggingGuidePanel(Panel):
    """Main panel for the Rigging Guide addon"""
    bl_label = "Rigging Guide"
    bl_idname = "VIEW3D_PT_rigging_guide"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Rigging Guide'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        
        # Title
        layout.label(text="Character Rigging Guide", icon='ARMATURE_DATA')
        layout.separator()
        
        # Guide Selection
        layout.label(text="Select Guide Type:")
        row = layout.row()
        row.prop_enum(scene, "rigging_guide_type", 'basic', icon='BONE_DATA')
        row.prop_enum(scene, "rigging_guide_type", 'advanced', icon='PREFERENCES')
        row = layout.row()
        row.prop_enum(scene, "rigging_guide_type", 'facial', icon='FACE_MAP')
        
        layout.separator()
        
        # Get current guide
        guides = operators.get_current_guide(scene)
        current_step = scene.rigging_guide_index
        
        if current_step < len(guides):
            guide = guides[current_step]
            
            # Display current step
            layout.label(text=f"Step {current_step + 1} of {len(guides)}", icon='INFO')
            layout.label(text=guide['title'])
            
            layout.separator()
            
            # Description
            layout.label(text="Description:")
            for line in guide['description'].split('\n'):
                layout.label(text=line, icon='DOT')
            
            layout.separator()
            
            # Tips
            if 'tips' in guide:
                layout.label(text="Tips:")
                for tip in guide['tips']:
                    layout.label(text=f"• {tip}", icon='HELP')
            
            layout.separator()
            
            # Action buttons
            if 'action' in guide:
                action = guide['action']
                layout.label(text="Quick Action:")
                if action == "CREATE_ARMATURE":
                    layout.operator("rigging_guide.create_armature", icon='ARMATURE_DATA')
                elif action == "PARENT_MESH":
                    layout.operator("rigging_guide.parent_mesh", icon='LINKED')
            
            layout.separator()
            
            # Navigation buttons
            col = layout.column(align=True)
            row = col.row(align=True)
            row.operator("rigging_guide.previous_step", icon='BACK', text="Previous")
            row.operator("rigging_guide.next_step", icon='FORWARD', text="Next")
            col.operator("rigging_guide.reset", icon='LOOP_BACK', text="Reset Guide")
        else:
            layout.label(text="Guide completed!", icon='CHECKMARK')
            layout.operator("rigging_guide.reset", text="Start Over")

class RiggingToolsPanel(Panel):
    """Quick access tools for rigging"""
    bl_label = "Rigging Tools"
    bl_idname = "VIEW3D_PT_rigging_tools"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Rigging Guide'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Quick Tools", icon='TOOL_SETTINGS')
        layout.separator()
        
        # Armature tools
        layout.label(text="Armature:", icon='ARMATURE_DATA')
        col = layout.column(align=True)
        col.operator("rigging_guide.create_armature", icon='ADD')
        col.operator("object.editmode_toggle", text="Edit Armature", icon='EDIT')
        
        layout.separator()
        
        # Mesh tools
        layout.label(text="Mesh:", icon='MESH_DATA')
        col = layout.column(align=True)
        col.operator("rigging_guide.select_mesh", icon='RESTRICT_SELECT_OFF')
        col.operator("rigging_guide.parent_mesh", icon='LINKED')
        
        layout.separator()
        
        # Mode switching
        layout.label(text="Mode Switching:", icon='EDIT')
        row = layout.row()
        row.operator("object.mode_set", text="Object").mode = 'OBJECT'
        row.operator("object.mode_set", text="Edit").mode = 'EDIT'
        row = layout.row()
        row.operator("object.mode_set", text="Pose").mode = 'POSE'
        row.operator("object.mode_set", text="Weight").mode = 'WEIGHT_PAINT'

class RiggingTipsPanel(Panel):
    """Tips and best practices for rigging"""
    bl_label = "Rigging Tips"
    bl_idname = "VIEW3D_PT_rigging_tips"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Rigging Guide'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Best Practices", icon='LIGHTPROBE_GRID')
        layout.separator()
        
        tips = [
            ("Topology", "Good mesh topology is crucial for deformation"),
            ("Origin", "Always center your character at the origin"),
            ("Naming", "Use clear naming conventions for bones"),
            ("Symmetry", "Use symmetric bone setups when possible"),
            ("Testing", "Test your rig frequently during creation"),
            ("Constraints", "Use constraints for complex rigging"),
            ("Weight Paint", "Paint weights carefully for smooth deformation"),
            ("Documentation", "Document your rig setup for future reference"),
        ]
        
        for title, tip in tips:
            box = layout.box()
            box.label(text=title, icon='CHECKMARK')
            box.label(text=tip)
