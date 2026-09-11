# Rigging guides and tutorials

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
            "Remove duplicate vertices (Alt+M > Merge by Distance)",
            "Ensure smooth normals (Shade Smooth)",
            "Check for any holes in the mesh",
            "Apply modifiers before rigging"
        ]
    },
    {
        "title": "Step 3: Create an Armature",
        "description": "Add an armature (skeleton) to your character.",
        "tips": [
            "Use Shift+A > Armature > Human for a quick start",
            "Position the armature at the origin (0, 0, 0)",
            "Scale the armature to fit your character properly",
            "You can also start with a simple Single Bone and build from there"
        ],
        "action": "CREATE_ARMATURE"
    },
    {
        "title": "Step 4: Edit the Armature",
        "description": "Enter edit mode and adjust the bones to match your character's anatomy.",
        "tips": [
            "Press Tab to enter edit mode (while armature is selected)",
            "Use proportional editing (O key) for smooth adjustments",
            "Ensure bones follow the character's joints",
            "Use Shift+D to duplicate bones",
            "Press E to extrude new bones from existing ones",
            "Name your bones clearly (Spine, LeftArm, RightLeg, etc.)"
        ]
    },
    {
        "title": "Step 5: Add Bone Constraints",
        "description": "Add constraints to control bone behavior and improve rigging.",
        "tips": [
            "Use IK (Inverse Kinematics) for limbs - easier to control",
            "Add Pole Targets for elbows and knees to prevent flipping",
            "Use Limit Rotation constraints for realistic movement",
            "Add Copy Rotation constraints for secondary bones",
            "Damped Track is useful for aiming bones"
        ]
    },
    {
        "title": "Step 6: Parent Mesh to Armature",
        "description": "Link your mesh to the armature so it deforms with the bones.",
        "tips": [
            "Select the mesh first, then the armature (Shift+Click)",
            "Press Ctrl+P and choose 'Armature Deform'",
            "Use 'With Automatic Weights' for quick setup",
            "Ensure the mesh and armature have the same location",
            "The mesh will now follow the armature's movements"
        ],
        "action": "PARENT_MESH"
    },
    {
        "title": "Step 7: Weight Painting",
        "description": "Paint weights to control how each bone deforms the mesh.",
        "tips": [
            "Switch to Weight Paint mode (Tab, then select Weight Paint)",
            "Use red for high influence, blue for low influence",
            "Paint where each bone should have the most effect",
            "Use the brush size to control detail (F key)",
            "Test your deformations frequently while painting",
            "Use Blur brush to smooth weight transitions"
        ]
    },
    {
        "title": "Step 8: Test Your Rig",
        "description": "Test your rig by posing the character.",
        "tips": [
            "Switch to Pose mode (Ctrl+Tab)",
            "Rotate bones to test deformation",
            "Check for pinching or stretching in the mesh",
            "Adjust weights if needed (return to Weight Paint)",
            "Test extreme poses to identify problem areas",
            "Rotate the view to see all angles"
        ]
    }
]

ADVANCED_RIGGING_GUIDE = [
    {
        "title": "Advanced: Step 1 - Control Rigs",
        "description": "Create intuitive control objects for animators to use.",
        "tips": [
            "Use curves or custom shapes for visual clarity",
            "Create separate control bones from deformation bones",
            "Use bone layers to organize controls",
            "Add size and color conventions for different control types",
            "Use Limit Rotation for realistic constraints"
        ]
    },
    {
        "title": "Advanced: Step 2 - IK/FK Switching",
        "description": "Set up IK/FK switching for flexible limb control.",
        "tips": [
            "Create both IK and FK chains for limbs",
            "Use a property to blend between IK and FK",
            "Use drivers to automate the switching",
            "Add feedback for the current mode",
            "Test smooth transitions between modes"
        ]
    },
    {
        "title": "Advanced: Step 3 - Facial Rig Setup",
        "description": "Set up a detailed facial rigging system.",
        "tips": [
            "Create individual bones for facial features",
            "Use shapekeys alongside bone deformation",
            "Set up control rigs for eyes, mouth, and expressions",
            "Use constraints to link facial movements",
            "Create presets for common expressions"
        ]
    },
    {
        "title": "Advanced: Step 4 - Custom Properties",
        "description": "Add custom properties for better control.",
        "tips": [
            "Add custom bone properties for animation control",
            "Use drivers to link properties to multiple bones",
            "Create sliders for complex movements",
            "Use min/max values for constraints",
            "Document all custom properties"
        ]
    },
    {
        "title": "Advanced: Step 5 - Bone Groups and Layers",
        "description": "Organize your rig for clarity and efficiency.",
        "tips": [
            "Use bone groups to color-code different types",
            "Organize bones into layers",
            "Hide unnecessary bones during animation",
            "Create separate layers for FK and IK chains",
            "Use naming conventions consistently"
        ]
    }
]

FACIAL_RIGGING_GUIDE = [
    {
        "title": "Facial Rigging: Step 1 - Topology Analysis",
        "description": "Ensure your character has proper facial topology.",
        "tips": [
            "Study facial anatomy and muscle flow",
            "Follow natural expression lines",
            "Ensure dense topology around eyes and mouth",
            "Use loop cuts to define facial features",
            "Test deformation with manual vertex movement first"
        ]
    },
    {
        "title": "Facial Rigging: Step 2 - Eye Rig",
        "description": "Create eye controls and look-at targets.",
        "tips": [
            "Add bones for eye rotation and blink",
            "Create a look-at target bone",
            "Use Track-To constraint for eye aim",
            "Add eyelid bones that follow eye movement",
            "Test eye movement in multiple directions"
        ]
    },
    {
        "title": "Facial Rigging: Step 3 - Mouth and Lips",
        "description": "Set up mouth and lip controls.",
        "tips": [
            "Create bones for jaw, upper lip, and lower lip",
            "Add individual controls for each lip corner",
            "Use shapekeys for phoneme visemes",
            "Blend bone deformation with shapekeys",
            "Test common mouth shapes (smile, frown, etc.)"
        ]
    },
    {
        "title": "Facial Rigging: Step 4 - Expression Controls",
        "description": "Set up controls for facial expressions.",
        "tips": [
            "Create controls for eyebrow movement",
            "Add cheek and cheekbone deformation",
            "Set up nose controls",
            "Use shapekeys for micro-expressions",
            "Create expression presets for animators"
        ]
    },
    {
        "title": "Facial Rigging: Step 5 - Bone Constraints",
        "description": "Add constraints to create natural facial movement.",
        "tips": [
            "Use Parent constraint for hierarchical control",
            "Add Limit Rotation for realistic movement ranges",
            "Use Track-To for targeted features",
            "Add Copy Rotation for symmetrical expressions",
            "Test all constraints in combination"
        ]
    },
    {
        "title": "Facial Rigging: Step 6 - Testing and Refinement",
        "description": "Test your facial rig thoroughly.",
        "tips": [
            "Create all common expressions",
            "Test eye blinking and look-around",
            "Test lip sync with vowel and consonant sounds",
            "Check for flipping or distortion",
            "Refine weights and constraints as needed"
        ]
    }
]

QUICK_REFERENCE = {
    "Shortcuts": [
        ("Tab", "Enter/Exit Edit Mode"),
        ("Ctrl+Tab", "Toggle Pose Mode"),
        ("Ctrl+P", "Set Parent"),
        ("Shift+D", "Duplicate"),
        ("E", "Extrude"),
        ("G", "Grab/Move"),
        ("R", "Rotate"),
        ("S", "Scale"),
        ("Alt+A", "Play/Stop Timeline"),
    ],
    "Common Mistakes": [
        "Not applying transforms before rigging",
        "Poor mesh topology causing bad deformation",
        "Uneven bone weights creating pinching",
        "Forgetting to test extreme poses",
        "Not naming bones clearly",
        "Using too few or too many bones",
        "Parenting mesh before finishing armature",
    ],
    "Pro Tips": [
        "Always work on a mirror if possible",
        "Use bone layers to organize your rig",
        "Name bones clearly and consistently",
        "Create test poses to verify deformation",
        "Use constraints to simplify complex movements",
        "Document your rigging decisions",
        "Keep separate control and deformation bones",
    ]
}

def get_guide_by_type(guide_type):
    """Get guide content by type"""
    guides = {
        "basic": BASIC_RIGGING_GUIDE,
        "advanced": ADVANCED_RIGGING_GUIDE,
        "facial": FACIAL_RIGGING_GUIDE,
    }
    return guides.get(guide_type, BASIC_RIGGING_GUIDE)

def get_quick_reference(reference_type):
    """Get quick reference information"""
    return QUICK_REFERENCE.get(reference_type, [])

def get_guide_count(guide_type):
    """Get total steps in a guide"""
    return len(get_guide_by_type(guide_type))

def get_guide_step(guide_type, step_index):
    """Get a specific step from a guide"""
    guide = get_guide_by_type(guide_type)
    if 0 <= step_index < len(guide):
        return guide[step_index]
    return None
