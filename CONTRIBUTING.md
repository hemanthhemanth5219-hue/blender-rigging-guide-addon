# Contributing to Blender Rigging Guide Addon

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Welcome all levels of experience
- Provide constructive feedback
- Focus on the code, not the person

## Ways to Contribute

### 1. Report Bugs

If you find a bug, please create an issue with:
- **Clear title**: Describe the bug concisely
- **Detailed description**: What happened and what you expected
- **Steps to reproduce**: How to recreate the issue
- **Environment**: Blender version, OS, Python version
- **Screenshots**: If applicable

**Example Issue Template:**
```
## Bug Report
**Title**: Addon crashes when selecting multiple bones

**Description**:
When I select multiple bones in edit mode and try to navigate steps, 
the addon crashes with an error.

**Steps to Reproduce**:
1. Open Blender
2. Create an armature with multiple bones
3. Enter edit mode
4. Select multiple bones (Shift+Click)
5. Try to press "Next" in the addon panel

**Environment**:
- Blender Version: 3.4
- OS: Windows 11
- Python: 3.10

**Error Message**:
[paste error from console]
```

### 2. Suggest Features

Have an idea for improvement? Submit a feature request:
- **Clear title**: "Add [feature]" or "Improve [aspect]"
- **Description**: What would this add and why it's useful
- **Example usage**: How users would use this feature
- **Related issues**: Link to related discussions

**Example Feature Request:**
```
## Feature Request
**Title**: Add video tutorials integration

**Description**:
Include embedded video tutorials for each step to help visual learners.

**Use Case**:
Users could watch a video demonstration alongside the text guide.

**Example**:
- Step 1 has text instructions
- User clicks "Watch Video" 
- Tutorial video appears (or opens in browser)
```

### 3. Improve Documentation

Documentation improvements are always welcome:
- Fix typos and grammar
- Clarify confusing sections
- Add examples
- Update outdated information

**How to contribute docs:**
1. Fork the repository
2. Edit markdown files
3. Submit a pull request with changes

### 4. Enhance the Guide Content

Help improve the rigging guides:
- Add new tips
- Improve step descriptions
- Add troubleshooting sections
- Include professional insights

**Contribution guidelines for guides:**
- Keep language clear and beginner-friendly
- Test instructions in Blender
- Provide practical examples
- Include warnings for common mistakes

### 5. Code Contributions

Want to improve the code? Great!

**Development Setup:**
```bash
# 1. Clone the repository
git clone https://github.com/hemanthhemanth5219-hue/blender-rigging-guide-addon.git

# 2. Create a feature branch
git checkout -b feature/your-feature-name

# 3. Make your changes
# 4. Test in Blender
# 5. Commit and push
git add .
git commit -m "Add your description"
git push origin feature/your-feature-name
```

**Code Style Guidelines:**
- Follow PEP 8 for Python code
- Use descriptive variable names
- Comment complex logic
- Keep functions focused and small
- Use type hints where applicable

**Example Code Contribution:**
```python
def get_guide_by_type(guide_type):
    """
    Get guide content by type.
    
    Args:
        guide_type (str): Type of guide ('basic', 'advanced', 'facial')
        
    Returns:
        list: List of guide steps
    """
    guides = {
        "basic": BASIC_RIGGING_GUIDE,
        "advanced": ADVANCED_RIGGING_GUIDE,
        "facial": FACIAL_RIGGING_GUIDE,
    }
    return guides.get(guide_type, BASIC_RIGGING_GUIDE)
```

## Pull Request Process

### Before Submitting

1. **Fork the repository** on GitHub
2. **Create a feature branch** from `main`
3. **Make your changes** with clear commits
4. **Test thoroughly** in Blender
5. **Update documentation** if needed

### Submitting a Pull Request

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request on GitHub**
   - Title: Clear, descriptive title
   - Description: Explain what changes you made and why
   - Link any related issues

3. **PR Template Example:**
   ```
   ## Description
   Brief explanation of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Documentation update
   - [ ] Code improvement
   
   ## Related Issues
   Fixes #[issue number]
   
   ## Testing
   How to test these changes:
   1. Step 1
   2. Step 2
   3. Step 3
   
   ## Screenshots
   [If applicable, add screenshots]
   
   ## Checklist
   - [ ] My code follows PEP 8 style
   - [ ] I have tested in Blender
   - [ ] I have updated documentation
   - [ ] Comments are clear and helpful
   ```

### Review Process

- Maintainers will review your PR
- You may be asked to make changes
- Be open to feedback
- Once approved, PR will be merged

## Project Structure

```
blender-rigging-guide-addon/
├── __init__.py              # Main addon initialization
├── operators.py             # Operators and functions
├── ui.py                    # UI panels and interface
├── guides.py                # Guide content and data
├── README.md                # Main documentation
├── REQUIREMENTS.md          # Requirements and setup
├── USAGE_EXAMPLES.md        # Usage examples
├── CONTRIBUTING.md          # This file
└── LICENSE                  # MIT License
```

## Important Files to Know

| File | Purpose |
|------|---------|
| `__init__.py` | Addon metadata, registration |
| `operators.py` | Operator classes and logic |
| `ui.py` | UI panels and layout |
| `guides.py` | Guide content and reference data |

## Testing Your Changes

### In Blender

1. Install your modified addon
2. Test in a fresh Blender session
3. Try all guide types
4. Test all buttons and operators
5. Check error console for messages

### Test Scenarios

- [ ] Open each guide type
- [ ] Navigate through all steps
- [ ] Use quick action buttons
- [ ] Switch between guides
- [ ] Reset guide at different steps
- [ ] Test on different Blender versions

## Reporting a Security Issue

Do not open a public issue for security vulnerabilities. Instead, email the maintainers privately.

## Getting Help

- **Questions?** Open a Discussion on GitHub
- **Need guidance?** Check existing issues and PRs
- **Want to chat?** Join the Blender community forums
- **Bug help?** Include error logs and reproduction steps

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Feel free to:
- Open an issue with tag "question"
- Comment on existing issues
- Start a discussion
- Email the maintainers

---

**Thank you for helping make this addon better! 🎨**

Happy contributing!
