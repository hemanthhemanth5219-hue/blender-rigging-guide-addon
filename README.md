# Blender Rigging Guide Addon

A comprehensive interactive addon for Blender that provides step-by-step guidance for character rigging, from basic to advanced techniques.

![Blender](https://img.shields.io/badge/Blender-3.0+-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Features

✨ **Interactive Rigging Guides**
- Basic rigging tutorial (8 steps)
- Advanced rigging techniques (5 steps)
- Facial rigging guide (6 steps)
- Quick reference materials

🎯 **Smart Tools**
- Create armature with one click
- Automatic mesh selection
- Parent mesh to armature
- Quick mode switching

📚 **Educational Content**
- Detailed step-by-step instructions
- Professional tips for each step
- Best practices and common mistakes
- Keyboard shortcuts reference

🎨 **User-Friendly Interface**
- Organized sidebar panels
- Progress tracking
- Visual icons and hierarchy
- Easy navigation between steps

## Installation

### Method 1: From ZIP File

1. Download the addon as a ZIP file
2. Open Blender → Edit → Preferences → Add-ons
3. Click "Install" and select the ZIP file
4. Enable the addon by checking the checkbox
5. Close Preferences

### Method 2: Manual Installation

1. Clone or download the repository
2. Locate your Blender addons folder:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\<version>\scripts\addons`
   - **macOS**: `~/Library/Application Support/Blender/<version>/scripts/addons`
   - **Linux**: `~/.config/blender/<version>/scripts/addons`
3. Copy the addon folder into the addons directory
4. Restart Blender and enable in Preferences

## Usage

### Getting Started

1. **Open the Addon**
   - Open Blender's 3D View
   - Look for "Rigging Guide" in the sidebar (press `N` if not visible)
   - Select it from the tabs on the right panel

2. **Choose a Guide**
   - **Basic** - For beginners learning rigging fundamentals
   - **Advanced** - For experienced riggers learning advanced techniques
   - **Facial** - Specialized guide for facial rigging

3. **Follow the Steps**
   - Read each step's description
   - Follow the tips provided
   - Use quick action buttons when available
   - Progress through with Next/Previous buttons

### Basic Rigging Workflow

```
1. Import/Create Model
   ↓
2. Prepare Mesh
   ↓
3. Create Armature
   ↓
4. Edit Armature Bones
   ↓
5. Add Constraints
   ↓
6. Parent Mesh to Armature
   ↓
7. Weight Paint
   ↓
8. Test & Refine
```

## Quick Reference

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Tab` | Enter/Exit Edit Mode |
| `Ctrl+Tab` | Toggle Pose Mode |
| `Ctrl+P` | Set Parent |
| `Shift+D` | Duplicate |
| `E` | Extrude |
| `G` | Grab/Move |
| `R` | Rotate |
| `S` | Scale |
| `Alt+A` | Play/Stop Timeline |
| `F` | Brush Size (Paint Modes) |

### Panel Features

**Rigging Guide Panel**
- Main guide viewer with step-by-step instructions
- Guide type selection (Basic/Advanced/Facial)
- Navigation buttons
- Quick action buttons

**Rigging Tools Panel**
- Quick armature creation
- Mesh selection tools
- Parent/linking tools
- Mode switching shortcuts

**Rigging Tips Panel**
- Best practices guide
- Common mistakes to avoid
- Professional tips

## Addon Structure

```
blender-rigging-guide-addon/
├── __init__.py          # Main addon initialization
├── operators.py         # Operators and rigging guides
├── ui.py               # UI panels and interface
├── guides.py           # Detailed guide content
└── README.md           # This file
```

## Content Overview

### Basic Rigging Guide (8 Steps)
1. Import or Create a Model
2. Prepare the Mesh
3. Create an Armature
4. Edit the Armature
5. Add Bone Constraints
6. Parent Mesh to Armature
7. Weight Painting
8. Test Your Rig

### Advanced Rigging Guide (5 Steps)
1. Control Rigs
2. IK/FK Switching
3. Facial Rig Setup
4. Custom Properties
5. Bone Groups and Layers

### Facial Rigging Guide (6 Steps)
1. Topology Analysis
2. Eye Rig
3. Mouth and Lips
4. Expression Controls
5. Bone Constraints
6. Testing and Refinement

## Tips for Best Results

### Before You Start
- ✓ Ensure your model has good topology
- ✓ Center your character at the origin
- ✓ Apply all transforms (Ctrl+A → All Transforms)
- ✓ Remove loose geometry and duplicates

### During Rigging
- ✓ Name bones clearly and consistently
- ✓ Use bone layers to organize
- ✓ Test frequently while working
- ✓ Use symmetry when possible
- ✓ Create test poses regularly

### After Rigging
- ✓ Weight paint carefully
- ✓ Test extreme poses
- ✓ Blend bone deformation with shapekeys
- ✓ Document your setup
- ✓ Create animation presets

## Troubleshooting

### Mesh deforms incorrectly
- **Solution**: Return to Weight Paint mode and adjust weights
- Check that bones are properly positioned
- Test with simpler poses first

### Bones don't show
- **Solution**: Check bone visibility settings
- Ensure bones are on visible layer
- Toggle "Show All Bones" in outliner

### Armature won't parent to mesh
- **Solution**: Select mesh first, then armature
- Both objects must be in the same location
- Try "With Automatic Weights" option

### Addon not appearing
- **Solution**: Restart Blender after installation
- Check that addon is enabled in Preferences
- Look for "Rigging Guide" in View3D sidebar

## Features in Development

- [ ] Video tutorials integration
- [ ] Rigging quality checker
- [ ] Automatic weight painting preview
- [ ] Rigging template library
- [ ] Custom rig builder wizard
- [ ] Animation controller presets
- [ ] Multi-language support

## Contributing

Contributions are welcome! Here's how you can help:

1. **Report Bugs**: Open an issue with detailed description
2. **Suggest Features**: Share your ideas for improvements
3. **Improve Guides**: Help enhance the tutorial content
4. **Translations**: Help translate to other languages

## License

This addon is released under the MIT License. See LICENSE file for details.

## Support

- 📖 **Documentation**: Check the README and guide content
- 🐛 **Bug Reports**: Open an issue on GitHub
- 💬 **Discussions**: Use GitHub Discussions for questions
- 🌐 **Blender Forum**: Share your work and get feedback

## Changelog

### Version 1.0.0 (Initial Release)
- ✨ Basic rigging guide with 8 steps
- ✨ Advanced rigging guide with 5 steps
- ✨ Facial rigging guide with 6 steps
- ✨ Interactive UI panels
- ✨ Quick reference materials
- ✨ Essential rigging tools

## Credits

Created by: Hemanth

Inspired by: Blender community and rigging best practices

## Disclaimer

This addon is provided as-is for educational purposes. Always test your rigs thoroughly before using them in production. Results may vary based on model topology and complexity.

---

**Happy Rigging! 🎨**

For the latest updates and to report issues, visit: https://github.com/hemanthhemanth5219-hue/blender-rigging-guide-addon
