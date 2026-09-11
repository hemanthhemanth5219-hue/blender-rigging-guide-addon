# Example Usage Guide

This guide shows common workflows and how to use the Blender Rigging Guide Addon effectively.

## Quick Start Example

### Scenario: Rigging a Simple Character

**Step 1: Prepare Your Scene**
```
1. Open Blender
2. Import or create your character model
3. Select the mesh and apply transforms (Ctrl+A → All Transforms)
4. Remove any duplicate vertices (Select All → Merge by Distance)
```

**Step 2: Open the Rigging Guide**
```
1. Look for "Rigging Guide" in the View3D sidebar (press N if not visible)
2. Select "Basic" guide type
3. Read Step 1 instructions
```

**Step 3: Follow the Guide Step by Step**
```
1. Press "Next" to go to Step 2
2. Read the description and tips
3. Perform the described action
4. Use "Previous" if you need to review
5. Continue through all 8 steps
```

## Workflow Examples

### Example 1: Basic Character Rigging

**Time Required**: 2-4 hours

1. **Import Model** (Step 1)
   - File → Import → Choose your model format
   - Set to origin if needed

2. **Clean Mesh** (Step 2)
   - Remove duplicates
   - Apply modifiers
   - Check for holes

3. **Create Armature** (Step 3)
   - Click "Create Armature" button in addon
   - Or manually: Shift+A → Armature

4. **Edit Bones** (Step 4)
   - Press Tab to enter edit mode
   - Position bones to match character
   - Create proper bone hierarchy

5. **Add Constraints** (Step 5)
   - Select bone → Properties panel
   - Add IK constraints for limbs
   - Add Limit Rotation for joints

6. **Parent Mesh** (Step 6)
   - Select mesh, then armature
   - Press Ctrl+P → Armature Deform
   - Or use addon button

7. **Weight Paint** (Step 7)
   - Tab → Weight Paint mode
   - Paint influence of each bone
   - Use brush size F key

8. **Test Rig** (Step 8)
   - Ctrl+Tab → Pose mode
   - Rotate bones to test
   - Adjust weights as needed

### Example 2: Facial Rigging Setup

**Time Required**: 3-6 hours

1. **Select Facial Guide**
   - Choose "Facial" from guide types

2. **Follow Facial Workflow**
   - Create eye bones
   - Create eyelid controls
   - Create mouth/lip bones
   - Add expression controls

3. **Add Constraints**
   - Track-To for eye gaze
   - Limit Rotation for expressions
   - Parent constraints for consistency

4. **Weight Paint Face**
   - Focus on smooth transitions
   - Test expressions frequently
   - Blend with shapekeys for phonemes

### Example 3: Advanced IK/FK Setup

**Time Required**: 4-8 hours

1. **Select Advanced Guide**
   - Choose "Advanced" from guide types

2. **Create Dual Chains**
   - Create FK chain (Forward Kinematics)
   - Create IK chain (Inverse Kinematics)
   - Create master control

3. **Add IK Constraints**
   - Add IK Solver to IK chain
   - Create pole targets
   - Set up blend control

4. **Create Control Rigs**
   - Use curves or custom shapes
   - Organize in bone layers
   - Color code for clarity

## Tips for Common Scenarios

### Scenario: Mesh deforms wrong in certain areas

**Solution**:
1. Go to Weight Paint mode
2. Select the problem bone
3. Use red (high influence) to fix deformation
4. Use smooth brush to blend transitions
5. Test by rotating the bone

### Scenario: Character's arm rotates the wrong direction

**Solution**:
1. Go to Pose mode
2. Select the arm bone
3. Add Limit Rotation constraint
4. Set min/max values appropriately
5. Test the new rotation limits

### Scenario: Fingers don't move with hand

**Solution**:
1. Edit mode: Select finger bones
2. Parent them to hand bone (Ctrl+P → Bone)
3. In weight paint: Ensure proper influence
4. Test finger movement with hand rotation

## Best Practices Checklist

Before considering your rig complete:

- [ ] All bones are named clearly
- [ ] Rig can perform extreme poses without breaking
- [ ] Weight painting is smooth with no artifacts
- [ ] Constraints are properly configured
- [ ] Bone layers are organized
- [ ] Control rigs are intuitive for animators
- [ ] Documentation is complete
- [ ] Rig has been tested thoroughly

## Performance Optimization Tips

### Keep Frame Rate High While Animating

1. **Reduce Viewport Display**
   - Hide unnecessary geometry layers
   - Use simplified meshes during animation
   - Enable "Fast Viewport" options

2. **Optimize Rig Complexity**
   - Use fewer bones where possible
   - Combine bones where appropriate
   - Minimize constraint count

3. **Use Bone Layers**
   - Create layers for different rig parts
   - Hide unused layers during work
   - Toggle visibility as needed

## Keyboard Shortcuts Cheatsheet

### Essential Shortcuts for Rigging

```
Tab              - Toggle Edit/Object Mode
Ctrl+Tab         - Toggle Pose Mode
G                - Grab/Move
R                - Rotate
S                - Scale
E                - Extrude (Edit mode)
Shift+D          - Duplicate
X                - Delete
Alt+M            - Merge vertices
Ctrl+P           - Set Parent
Alt+P            - Clear Parent
Ctrl+A           - Apply Transforms
F                - Brush Size (Paint modes)
O                - Proportional Editing
Right Click      - Select
Box Select       - B
Circle Select    - C
```

## Video Reference

While the addon doesn't include videos yet, consider watching:
- Blender official rigging tutorials
- Community rigging walkthroughs
- Character rigging masterclasses

## Troubleshooting Common Issues

### Issue: "Addon not working after Blender update"
- **Fix**: Reinstall the addon, restart Blender

### Issue: "Can't see the rigging guide panel"
- **Fix**: Press N to toggle sidebar, look for "Rigging Guide" tab

### Issue: "Mesh jumps when parenting to armature"
- **Fix**: Ensure mesh and armature are at same location (0,0,0)

### Issue: "Weight painting changes aren't showing"
- **Fix**: Make sure you're in Weight Paint mode and looking at correct bone

## Next Steps After Rigging

1. **Animation Ready**
   - Your rig is ready for animation
   - Create animation rig file
   - Document rig setup for animators

2. **Refinement**
   - Continue adjusting weights
   - Add facial blend shapes
   - Create animation presets

3. **Integration**
   - Export rig for other tools
   - Set up scene for rendering
   - Test animation workflows

4. **Documentation**
   - Create rig sheet
   - Document constraints
   - List custom properties
   - Provide animation guidelines

---

**Happy Rigging! Questions? Check the README or open an issue on GitHub.**
