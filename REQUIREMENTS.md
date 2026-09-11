# Blender Rigging Guide Addon - Requirements

## Blender Version
- Blender 3.0.0 or higher
- Recommended: Blender 3.6 LTS or later for best compatibility

## Python Version
- Python 3.9 or higher
- Usually bundled with Blender

## Dependencies
This addon uses only Blender's built-in modules:
- `bpy` - Blender Python API
- `bpy.props` - Property system
- `bpy.types` - Type definitions

No external packages required!

## System Requirements

### Minimum Specifications
- **RAM**: 4 GB
- **Disk Space**: 50 MB
- **GPU**: Any dedicated GPU recommended for 3D work

### Recommended Specifications
- **RAM**: 8 GB or more
- **GPU**: NVIDIA CUDA, AMD HIP, or Intel OneAPI for GPU rendering
- **Processor**: 4+ cores recommended

## Installation Verification

After installation, verify everything works:

1. Open Blender
2. Go to Edit → Preferences → Add-ons
3. Search for "Rigging Guide"
4. Check if it appears in the list
5. Enable it by clicking the checkbox
6. Close Preferences
7. Look for "Rigging Guide" tab in View3D sidebar

## Troubleshooting Installation

### Addon not appearing
- Restart Blender after installation
- Check that .py files are in correct format (UTF-8)
- Verify folder structure is correct

### Import errors
- Check Python console for error messages (Window → Toggle System Console)
- Ensure Blender version is 3.0 or higher
- Try reinstalling the addon

### UI not showing
- Press 'N' to toggle sidebar
- Look for "Rigging Guide" tab
- Check that addon is enabled in Preferences

## Platform-Specific Notes

### Windows
- Extract ZIP to: `C:\Users\<username>\AppData\Roaming\Blender Foundation\Blender\<version>\scripts\addons`
- Use forward slashes (/) in file paths

### macOS
- Extract ZIP to: `~/Library/Application Support/Blender/<version>/scripts/addons`
- May need to give permissions to the folder

### Linux
- Extract ZIP to: `~/.config/blender/<version>/scripts/addons`
- Ensure read/execute permissions on files

## Performance Notes

- Addon has minimal memory footprint
- No performance impact when not in use
- UI updates only when needed
- Suitable for all hardware configurations

## Known Limitations

- Requires manual rigging setup (not fully automated)
- Best results with models that have good topology
- Weight painting still requires manual adjustment
- IK/FK switching setup requires manual configuration

## Future Requirements

Planned features that may require additional dependencies:
- Video tutorials (may need external hosting)
- Advanced weight painting (potentially using NumPy)
- Rig quality analysis (may use additional math libraries)

## Support

For installation issues:
- Check GitHub Issues: https://github.com/hemanthhemanth5219-hue/blender-rigging-guide-addon/issues
- Refer to Blender manual: https://docs.blender.org/manual/en/latest/
