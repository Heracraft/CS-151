# The Breathing Lake: 500 Years of Change

**Interactive Environmental Art Project**  
*CS 151 - Fall 2025 - Final Project*  
By Nehemia Kaaya

## Project Overview

"The Breathing Lake" is an interactive environmental artwork that visualizes 500 years of climate change using geochemical data from Lake Masoko, Tanzania (1511-2002 AD). The project presents three distinct scenes that explore different aspects of environmental data through creative computational visualization.

### Theme: Climate Change Through Time

The Lake Masoko sediment core data reveals three key environmental stories:
1. **The Little Ice Age** (dry period 1550-1850)
2. **Solar Activity Cycles** (reflected in lake levels)
3. **Anthropogenic Impact** (human disturbance in the last 60 years)

## Technical Highlights

This project demonstrates mastery of CS 151 course objectives:

### Core CS Concepts Implemented

✅ **Inheritance & Polymorphism**
- Parent class `EnvironmentalFeature` with three child classes
- Polymorphic `draw()` method across different object types
- Accessor and mutator methods for encapsulation

✅ **L-System & Interpreter Classes**
- Dynamic forest generation based on climate data
- Custom L-system rules for different vegetation complexity
- Integration with TurtleInterpreter for visualization

✅ **Recursion**
- Recursive ripple drawing for solar activity visualization
- Variable recursion depth based on magnetic susceptibility data
- Base case and recursive case properly implemented

### Programming Best Practices

- **Modularity**: Small, reusable functions with keyword parameters
- **User Interaction**: Menu system, command-line arguments, interactive prompts
- **Documentation**: Comprehensive docstrings and inline comments
- **File Organization**: Separate modules for data handling, classes, and scenes
- **Testing**: Each module includes test functions

## Installation & Setup

### Requirements

- Python 3.12 or higher
- Tkinter (for graphics)
- Standard Python libraries (json, sys, math)

### Installing Dependencies

On Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

### Project Structure

```
Final Project/
├── main.py                    # Main controller with graphical home page
├── data.json                  # Lake Masoko geochemical data (1511-2002 AD)
├── masoko_data_handler.py     # Data loading and processing functions
├── environmental_features.py  # Parent and child classes (OOP)
├── scene1_sediment.py         # Scene 1: Sediment Core (Zelle graphics, 1000x1300)
├── scene2_forest.py           # Scene 2: Changing Forest (L-systems, 1600x1600)
├── scene3_ripples.py          # Scene 3: Solar Ripples (Recursion, 1600x1200)
├── graphics.py                # Zelle graphics library
├── lib/
│   ├── lsystem.py            # L-System class
│   └── turtle_interpreter.py  # TurtleInterpreter class
└── views/
    └── home.py               # Graphical home page/scene selector (1200x900)
```

## Usage

### Graphical Home Page (Default - Recommended)

```bash
cd "Final Project"
python3 main.py
```

This launches a beautiful graphical home page (1200x900) with:
- Three large, color-coded scene buttons
- Scene descriptions and interaction hints
- Easy click-to-launch navigation
- Professional visual layout

### Text Menu Mode

```bash
python3 main.py --text
```

This launches the traditional text-based menu for terminal-only environments.

### Command-Line Mode

Run specific scenes directly:

```bash
# Scene 1: The Sediment Core
python3 main.py scene1

# Scene 2: The Changing Forest (interactive year selection)
python3 main.py scene2

# Scene 2: The Changing Forest (specific year)
python3 main.py scene2 1750

# Scene 3: The Solar Ripples
python3 main.py scene3
```

### Running Individual Scenes

Each scene can also be run independently:

```bash
python3 scene1_sediment.py
python3 scene2_forest.py
python3 scene3_ripples.py
```

## The Home Page

**Window Size**: 1200 x 900 pixels  
**Features**:
- Interactive scene selector with three large buttons
- Color-coded by theme:
  - Scene 1: Brown (sediment/earth)
  - Scene 2: Green (forest/vegetation)
  - Scene 3: Blue (water/lake)
- Clear scene descriptions
- Exit button for clean shutdown
- Professional typography and layout

## The Three Scenes

### Scene 1: The Sediment Core 📊

**Window Size**: 1000 x 1300 pixels (2x scale)  
**Concept**: Data-driven visualization of lake sediment layers  
**Data Used**: Fe/Ti ratio (Iron/Titanium)  
**Visualization**: Stacked rectangles representing sediment layers  
**Interaction**: Click on layers to see year and chemical composition

**How it works:**
- Each layer represents a time period from the sediment core
- Color intensity indicates Fe/Ti ratio:
  - Darker brown = High iron (wet period, increased erosion)
  - Lighter tan = Low iron (dry period, possibly Little Ice Age)
- Click any layer to display detailed information

**CS Concepts:**
- Complex Objects (SedimentLayer class)
- Zelle graphics primitives
- Event handling (mouse clicks)
- Data normalization and color mapping

### Scene 2: The Changing Forest 🌳

**Window Size**: 1600 x 1600 pixels (2x scale)  
**Concept**: Climate-driven forest visualization using L-systems  
**Data Used**: Si/Ti ratio (Silicon/Titanium - aridity proxy)  
**Visualization**: L-system generated trees with varying complexity  
**Interaction**: Enter a year to see the corresponding forest

**How it works:**
- Si/Ti ratio indicates climate conditions:
  - High Si/Ti = Wet/windy period → Lush, complex trees
  - Low Si/Ti = Dry period → Sparse, simple vegetation
- L-system iterations vary from 2-5 based on data
- Different branching rules for different complexity levels
- All trees render at double the original scale

**CS Concepts:**
- L-system string generation
- TurtleInterpreter for drawing
- User input validation
- Command-line argument parsing

### Scene 3: The Solar Ripples 🌊

**Window Size**: 1600 x 1200 pixels (2x scale)  
**Concept**: Recursive visualization of solar activity cycles  
**Data Used**: MagSus (Magnetic Susceptibility)  
**Visualization**: Concentric ripples with recursive depth  
**Interaction**: Click to progress through time

**How it works:**
- Magnetic susceptibility correlates with solar activity
- Higher MagSus → More recursion depth (brighter, more ripples)
- Lower MagSus → Fewer ripples (dimmer colors)
- Click to advance through time periods chronologically
- Lake visualization more immersive at 2x scale

**CS Concepts:**
- Recursive function implementation
- Base case and recursive case
- Color interpolation based on recursion depth
- Time-based animation

## Data Description

### Lake Masoko Dataset

The project uses geochemical data from a sediment core taken from Lake Masoko, Tanzania. The data spans 491 years (1511-2002 AD) and includes:

- **Depth (cm)**: Position in sediment core
- **Age (AD)**: Calibrated year
- **MagSus (m³/kg)**: Magnetic susceptibility (solar activity proxy)
- **Si/Ti**: Silicon/Titanium ratio (aridity proxy)
- **Fe/Ti**: Iron/Titanium ratio (erosion/runoff indicator)
- **Other measurements**: Al/Ti, LOI, N total, C total, C/N

## Code Organization & Design

### Object-Oriented Design

```
EnvironmentalFeature (Parent Class)
├── Attributes: year, value, data_type, color
├── Methods: get/set accessors and mutators
└── Abstract: draw() method

    ├── SedimentLayer (Child)
    │   └── draw() → Zelle rectangles
    │
    ├── ClimateTree (Child)
    │   └── draw() → L-system trees
    │
    └── SolarRipple (Child)
        └── draw() → Recursive circles
```

### Modularity Example

The `create_sediment_layers()` function demonstrates modularity:
- Takes data and optional keyword parameters
- Returns reusable list of objects
- Can be called with different parameters for different visualizations

```python
layers = create_sediment_layers(data, x=250, y_start=50, layer_height=8)
```

### Data Processing Pipeline

1. **Load**: `read_data("data.json")` → List of dictionaries
2. **Query**: `get_data_by_year(data, 1750)` → Specific record
3. **Normalize**: `normalize_value(value, min, max)` → 0-1 range
4. **Create Objects**: `SedimentLayer(year, value, ...)` → Visualization object
5. **Draw**: `layer.draw(win, x, y)` → Rendered graphics

## Testing

Each module includes a `main()` test function that can be run independently:

```bash
# Test data handler
python3 masoko_data_handler.py

# Test environmental features classes
python3 environmental_features.py

# Test individual scenes
python3 scene1_sediment.py
python3 scene2_forest.py
python3 scene3_ripples.py
```

## Educational Value

This project demonstrates:

1. **Problem Decomposition**: Breaking a complex visualization into modular components
2. **Abstraction**: Using classes to represent real-world environmental data
3. **Algorithm Design**: Implementing L-systems and recursion for visual patterns
4. **User-Centered Design**: Creating intuitive interactions for exploring data
5. **Scientific Communication**: Translating data into accessible visual narratives

## Future Enhancements

Potential extensions for this project:

- [ ] Add animation transitions between scenes
- [ ] Include more data parameters (LOI, C/N ratios)
- [ ] Export visualizations as images
- [ ] Add sound design based on data patterns
- [ ] Implement data filtering by time period
- [ ] Create comparative views (side-by-side years)

## Credits & Sources

**Data Source**: Lake Masoko Sediment Core Geochemical Analysis  
**Graphics Library**: Zelle Graphics (adapted from CS 151 course materials)  
**Course**: CS 151 - Introduction to Computer Science  
**Instructor**: [Course Instructor Name]  
**Semester**: Fall 2025

## License

This project is created for educational purposes as part of CS 151 coursework.

---

*"The lake breathes with the rhythms of climate, solar cycles, and human impact—each layer a whisper from the past, each ripple a echo of cosmic forces."*
