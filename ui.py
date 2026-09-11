import bpy
from bpy.types import Panel, Operator
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
        
        # Guide Selection with proper buttons
        layout.label(text="Select Guide Type:", icon='HELP')
        col = layout.column(align=True)
        
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator("rigging_guide.select_guide", text="BASIC", icon='BONE_DATA').guide_type = "basic"
        row.operator("rigging_guide.select_guide", text="ADVANCED", icon='PREFERENCES').guide_type = "advanced"
        
        row = col.row(align=True)
        row.scale_y = 1.2
        row.operator("rigging_guide.select_guide", text="FACIAL", icon='FACE_MAP').guide_type = "facial"
        
        layout.separator()
        
        # Current Guide Display
        guides = operators.get_current_guide(scene)
        current_step = scene.rigging_guide_index
        guide_type = scene.rigging_guide_type
        
        if guides:
            # Guide Title
            guide_title = {
                "basic": "BASIC RIGGING GUIDE",
                "advanced": "ADVANCED RIGGING GUIDE",
                "facial": "FACIAL RIGGING GUIDE"
            }.get(guide_type, "RIGGING GUIDE")
            
            box = layout.box()
            box.label(text=guide_title, icon='INFO')
            box.label(text=f"Step {current_step + 1} / {len(guides)}")
            
            if current_step < len(guides):
                guide = guides[current_step]
                
                # Step Title
                layout.separator()
                layout.label(text=guide['title'], icon='ARROW_LEFTRIGHT')
                
                # Description
                layout.separator()
                layout.label(text="Description:", icon='TEXT')
                desc_box = layout.box()
                for line in guide['description'].split('\n'):
                    if line.strip():
                        desc_box.label(text=line)
                
                # Tips
                if 'tips' in guide and guide['tips']:
                    layout.separator()
                    layout.label(text="💡 Tips:", icon='HELP')
                    tips_box = layout.box()
                    for tip in guide['tips']:
                        tips_box.label(text=f"• {tip}")
                
                # Action buttons
                if 'action' in guide:
                    action = guide['action']
                    layout.separator()
                    layout.label(text="Quick Action:", icon='TOOL_SETTINGS')
                    if action == "CREATE_ARMATURE":
                        layout.operator("rigging_guide.create_armature", 
                                      text="CREATE ARMATURE", 
                                      icon='ADD').text = "Create Armature"
                    elif action == "PARENT_MESH":
                        layout.operator("rigging_guide.parent_mesh", 
                                      text="PARENT MESH", 
                                      icon='LINKED')
                
                # Navigation
                layout.separator()
                nav_col = layout.column(align=True)
                row = nav_col.row(align=True)
                row.scale_y = 1.3
                
                if current_step > 0:
                    row.operator("rigging_guide.previous_step", icon='BACK', text="◀ Previous")
                else:
                    row.label(text="Start")
                
                row.operator("rigging_guide.next_step", icon='FORWARD', text="Next ▶")
                
                nav_col.operator("rigging_guide.reset", icon='LOOP_BACK', text="↻ Reset Guide")
            else:
                # Guide completed
                layout.separator()
                complete_box = layout.box()
                complete_box.label(text="✓ GUIDE COMPLETED!", icon='CHECKMARK')
                layout.operator("rigging_guide.reset", text="Start Over", icon='LOOP_BACK')
        else:
            layout.label(text="Select a guide type to start!", icon='INFO')


class SelectGuideOperator(Operator):
    """Operator to select guide type"""
    bl_idname = "rigging_guide.select_guide"
    bl_label = "Select Guide"
    
    guide_type: bpy.props.StringProperty(default="basic")
    
    def execute(self, context):
        context.scene.rigging_guide_type = self.guide_type
        context.scene.rigging_guide_index = 0
        return {'FINISHED'}


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
        col.operator("rigging_guide.create_armature", icon='ADD', text="Create Armature")
        col.operator("object.editmode_toggle", text="Edit Armature", icon='EDIT')
        
        layout.separator()
        
        # Mesh tools
        layout.label(text="Mesh:", icon='MESH_DATA')
        col = layout.column(align=True)
        col.operator("rigging_guide.select_mesh", icon='RESTRICT_SELECT_OFF', text="Select Mesh")
        col.operator("rigging_guide.parent_mesh", icon='LINKED', text="Parent Mesh")
        
        layout.separator()
        
        # Mode switching
        layout.label(text="Mode Switching:", icon='EDIT')
        row = layout.row(align=True)
        row.operator("object.mode_set", text="Object").mode = 'OBJECT'
        row.operator("object.mode_set", text="Edit").mode = 'EDIT'
        row = layout.row(align=True)
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
            row = box.row()
            row.label(text=title, icon='CHECKMARK')
            box.label(text=tip)


class HelpAccessPanel(Panel):
    """Quick access to help system"""
    bl_label = "Help & Shortcuts"
    bl_idname = "VIEW3D_PT_rigging_help_access"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Rigging Guide'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        layout.label(text="Help System", icon='HELP')
        layout.separator()
        
        layout.label(text="Press Shift+/ to open help", icon='INFO')
        layout.label(text="with all keyboard shortcuts")
        
        layout.separator()
        layout.label(text="Quick Access Buttons:", icon='HAND')
        
        col = layout.column(align=True)
        col.operator("wm.rigging_addon_help", text="Quick Start").help_section = "QUICK_START"
        col.operator("wm.rigging_addon_help", text="Keyboard Shortcuts").help_section = "RIGGING"
        col.operator("wm.rigging_addon_help", text="Workflow").help_section = "WORKFLOW"
        col.operator("wm.rigging_addon_help", text="Pro Tips").help_section = "TIPS"
