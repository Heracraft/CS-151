# Quick Start Guide
## The Breathing Lake: Interactive Environmental Art

### Installation (One-time Setup)

1. **Install Python dependencies:**
   ```bash
   sudo apt-get update
   sudo apt-get install python3-tk
   ```

2. **Navigate to project directory:**
   ```bash
   cd "Final Project"
   ```

### Running the Project

#### Option 1: Graphical Home Page (New! Recommended)
```bash
python3 main.py
```
This launches a beautiful 1200x900 graphical interface with:
- Three large, clickable scene buttons
- Color-coded by theme (brown, green, blue)
- Scene descriptions and hints
- Easy point-and-click navigation

#### Option 2: Text Menu Mode
```bash
python3 main.py --text
```
Use this for terminal-only environments or if you prefer text menus.

#### Option 3: Direct Scene Access

**Scene 1 - The Sediment Core (1000x1300 - 2x scale):**
```bash
python3 main.py scene1
```
- Click on sediment layers to see year and chemical data
- All visuals scaled 2x for better visibility
- Close window to exit

**Scene 2 - The Changing Forest (1600x1600 - 2x scale):**
```bash
python3 main.py scene2
```
- Enter a year between 1511-2002 AD
- Watch the forest change based on climate
- Trees render at double scale
- Press 'q' and click to exit

**Scene 2 - Specific Year:**
```bash
python3 main.py scene2 1750
```
- Directly visualize forest for year 1750

**Scene 3 - The Solar Ripples (1600x1200 - 2x scale):**
```bash
python3 main.py scene3
```
- Click to progress through time
- Ripples and lake at 2x scale
- Press 'q' to quit
- Close window to exit

### Troubleshooting

**"ModuleNotFoundError: No module named 'tkinter'"**
- Run: `sudo apt-get install python3-tk`

**"TclError: no display name and no $DISPLAY environment variable"**
- You're in a headless environment (no GUI)
- This project requires a graphical display
- Run on a system with X11/Wayland display server

**Window appears but nothing draws**
- Make sure `data.json` is in the same directory as the scripts
- Check that all files from the project are present

### Testing Individual Modules

Test data handling:
```bash
python3 masoko_data_handler.py
```

Test classes (polymorphism demo):
```bash
python3 environmental_features.py
```

Test individual scenes:
```bash
python3 scene1_sediment.py
python3 scene2_forest.py
python3 scene3_ripples.py
```

### Project Structure Quick Reference

- `main.py` - Start here! Main menu controller
- `data.json` - Lake Masoko data (1511-2002 AD)
- `masoko_data_handler.py` - Data loading functions
- `environmental_features.py` - Classes (inheritance & polymorphism)
- `scene1_sediment.py` - Scene 1: Sediment visualization
- `scene2_forest.py` - Scene 2: L-system trees
- `scene3_ripples.py` - Scene 3: Recursive ripples
- `README.md` - Full documentation
- `PROJECT_REPORT.md` - Academic report template

### For Help

See `README.md` for detailed documentation.
