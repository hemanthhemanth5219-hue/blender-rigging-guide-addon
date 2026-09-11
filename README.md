# Blender Rigging Guide Addon

A comprehensive interactive addon for Blender that provides step-by-step guidance for character rigging, from basic to advanced techniques.

![Blender](https://img.shields.io/badge/Blender-3.0+-blue)
![Python](https://img.shields.io/badge/Python-3.9+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ⚡ Quick Access: Press `Shift+/` in Blender!

**See full addon documentation and data right in Blender using `Shift+/` hotkey!**

This opens the help system showing:
- What the addon can do
- All keyboard shortcuts
- Step-by-step guides
- Quick reference materials
- Troubleshooting tips

---

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

⌨️ **Keyboard Integration**
- **`Shift+/`** - Open addon help system (NEW!)
- **`N`** - Open/Close addon panel
- **`Tab`** - Edit Mode
- **`Ctrl+Tab`** - Pose Mode
- See [KEYBOARD_SHORTCUTS.md](KEYBOARD_SHORTCUTS.md) for full list

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

## 🚀 Quick Start

### First Time Users

1. **Open Blender** and create/import a character model
2. **Press `Shift+/`** to see addon help and capabilities
3. **Press `N`** to open the "Rigging Guide" panel in the sidebar
4. **Select a guide type**: Basic, Advanced, or Facial
5. **Follow the step-by-step instructions**
6. **Use `Shift+/` anytime** to reference shortcuts and tips

### Quick Workflow

```
Shift+/      → View addon info and shortcuts
N            → Open addon panel
Select Guide → Choose guide type
Follow Steps → Read and execute each step
Tab          → Enter Edit Mode (Blender shortcut)
Ctrl+Tab     → Enter Pose Mode (Blender shortcut)
Shift+/      → Quick reference while working
```

## 📋 What This Addon Shows You (Press Shift+/)

When you press **`Shift+/`** in Blender, you'll see:

### 🎯 Addon Capabilities
- 3 comprehensive rigging guides
- Smart rigging tools overview
- Step-by-step workflow descriptions
- Time estimates for each task
- Professional tips included

### ⌨️ All Keyboard Shortcuts
- Blender essentials (navigation, selection, transform)
- Mode switching shortcuts
- Edit/Pose/Weight Paint controls
- Addon-specific shortcuts
- Recommended workflow combinations

### 📚 Guide Contents
- **Basic Guide**: 8 steps for character rigging
- **Advanced Guide**: 5 steps for professional rigs
- **Facial Guide**: 6 steps for facial animation
- Each with detailed descriptions and tips

### 🛠️ Tools Included
- Armature creation
- Mesh parenting
- Constraint setup helpers
- Weight painting guidance
- Testing procedures

---

## Usage Guide

### Getting Started

1. **Open the Addon**
   - Open Blender's 3D View
   - Press `N` to toggle sidebar
   - Look for "Rigging Guide" tab

2. **Choose a Guide**
   - **Basic** - For beginners learning rigging fundamentals
   - **Advanced** - For experienced riggers learning advanced techniques
   - **Facial** - Specialized guide for facial rigging

3. **Follow the Steps**
   - Read each step's description
   - Follow the tips provided
   - Use quick action buttons when available
   - Progress through with Next/Previous buttons

### Keyboard Reference While Using Addon

| Shortcut | What It Does |
|----------|------------|
| `Shift+/` | **Show this addon's complete help system** |
| `N` | Open/Close addon panel |
| `Tab` | Toggle Edit Mode |
| `Ctrl+Tab` | Toggle Pose Mode |
| `G` | Grab/Move bones |
| `R` | Rotate bones |
| `S` | Scale bones |
| `Ctrl+P` | Parent objects |
| `F` | Brush size (Weight Paint mode) |
| `Spacebar` | Play animation |

See [KEYBOARD_SHORTCUTS.md](KEYBOARD_SHORTCUTS.md) for complete keyboard reference.

### Basic Rigging Workflow

```
1. Import/Create Model
   ↓
2. Prepare Mesh
   ↓
3. Create Armature (use addon button or Shift+A)
   ↓
4. Edit Armature Bones (follow addon guide)
   ↓
5. Add Constraints (follow addon tips)
   ↓
6. Parent Mesh to Armature (use addon button)
   ↓
7. Weight Paint (follow addon weight guide)
   ↓
8. Test & Refine (follow addon testing checklist)
```

## 📖 Documentation Files

- **[README.md](README.md)** - This file
- **[KEYBOARD_SHORTCUTS.md](KEYBOARD_SHORTCUTS.md)** - Complete keyboard guide + addon capabilities
- **[USAGE_EXAMPLES.md](USAGE_EXAMPLES.md)** - Practical workflow examples
- **[REQUIREMENTS.md](REQUIREMENTS.md)** - System requirements and dependencies
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute to the project
- **[LICENSE](LICENSE)** - MIT License

## 🎯 Addon Structure

```
blender-rigging-guide-addon/
├── __init__.py              # Main addon initialization
├── operators.py             # Operators and rigging guides
├── ui.py                    # UI panels and interface
├── guides.py                # Detailed guide content
├── README.md                # This file
├── KEYBOARD_SHORTCUTS.md    # Keyboard & capabilities guide
├── USAGE_EXAMPLES.md        # Usage examples
├── REQUIREMENTS.md          # Requirements
├── CONTRIBUTING.md          # Contributing guidelines
└── LICENSE                  # MIT License
```

## 📚 Content Overview

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

## 💡 Tips for Best Results

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
- ✓ Press `Shift+/` to reference shortcuts anytime

### After Rigging
- ✓ Weight paint carefully
- ✓ Test extreme poses
- ✓ Blend bone deformation with shapekeys
- ✓ Document your setup
- ✓ Create animation presets

## 🔧 Troubleshooting

### Addon not appearing
- **Solution**: Restart Blender after installation
- Check that addon is enabled in Preferences
- Look for "Rigging Guide" in View3D sidebar (press `N`)

### Can't remember shortcuts
- **Solution**: Press `Shift+/` anytime to see complete keyboard guide
- Check [KEYBOARD_SHORTCUTS.md](KEYBOARD_SHORTCUTS.md) file
- Addon shows tips for each step

### Mesh deforms incorrectly
- **Solution**: Return to Weight Paint mode and adjust weights
- Check that bones are properly positioned
- Test with simpler poses first
- Follow addon's weight painting guide (Step 7)

### Bones won't parent to mesh
- **Solution**: Select mesh first, then armature
- Both objects must be in the same location
- Try "With Automatic Weights" option
- Use addon's parent button for easy setup

## 🎓 Learning Path

### Beginner (New to Rigging)
1. Read [USAGE_EXAMPLES.md](USAGE_EXAMPLES.md) - Example 1
2. Press `Shift+/` to see all shortcuts
3. Follow Basic Guide step-by-step
4. Reference [KEYBOARD_SHORTCUTS.md](KEYBOARD_SHORTCUTS.md) as needed
5. Complete your first rig!

### Intermediate (Have rigged before)
1. Press `Shift+/` for quick reference
2. Select Advanced Guide
3. Follow specialized techniques
4. Reference keyboard shortcuts as needed
5. Create more complex rigs

### Advanced (Professional rigging)
1. Use all three guides as reference
2. Press `Shift+/` for quick lookups
3. Customize techniques for your needs
4. Contribute improvements back!

## ⌨️ Pro Tips

**Keyboard Efficiency**:
- Keep addon panel visible (press `N` once)
- Use `Shift+/` to quickly reference shortcuts
- Combine Blender shortcuts with addon instructions
- Learn shortcuts from the built-in guides

**Workflow Tips**:
- Pin your favorite guide in the panel
- Use multiple guide types for complex rigs
- Reference quick tips while working
- Test frequently using keyboard shortcuts

**Best Practices**:
- Save often while rigging (Ctrl+S)
- Create checkpoints between major steps
- Use separate files for different rig types
- Document custom modifications

## 📞 Support

- 📖 **Documentation**: Check README and guide files
- ⌨️ **Keyboard Help**: Press `Shift+/` in Blender anytime
- 🐛 **Bug Reports**: Open an issue on GitHub
- 💬 **Discussions**: Use GitHub Discussions for questions
- 🌐 **Community**: Share your work in Blender forums

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Bug reporting guidelines
- Feature requests
- Code contributions
- Documentation improvements

## 📄 License

This addon is released under the MIT License. See [LICENSE](LICENSE) file for details.

## 🎉 Getting Started NOW

**Quick Start in 3 Steps**:

1. **Install addon** in Blender preferences
2. **Press `Shift+/`** to see all addon features and shortcuts
3. **Press `N`** to open addon panel and start learning!

---

## Changelog

### Version 1.0.0 (Initial Release)
- ✨ Basic rigging guide with 8 steps
- ✨ Advanced rigging guide with 5 steps
- ✨ Facial rigging guide with 6 steps
- ✨ Interactive UI panels
- ✨ Quick reference materials
- ✨ Essential rigging tools
- ✨ **NEW**: Shift+/ keyboard shortcut for help system
- ✨ **NEW**: Comprehensive keyboard shortcuts guide
- ✨ **NEW**: Complete addon capabilities documentation

## 📞 Credits

Created by: **Hemanth**

Inspired by: Blender community and professional rigging practices

---

## 🚀 Start Rigging Now!

```
1. Open Blender
2. Press Shift+/ → See addon features
3. Press N → Open addon panel
4. Select a guide → Start learning
5. Happy Rigging! 🎨
```

**For the latest updates and to report issues, visit:**
👉 https://github.com/hemanthhemanth5219-hue/blender-rigging-guide-addon

---

**Remember**: Press **`Shift+/`** anytime in Blender to see all addon information and keyboard shortcuts! ⌨️✨
