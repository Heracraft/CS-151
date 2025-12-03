# CS 151 Final Project Report
## The Breathing Lake: 500 Years of Change

**Student Name**: Nehemia Kaaya  
**Course**: CS 151 - Section B  
**Semester**: Fall 2025  
**Project**: Interactive Environmental Art - Final Project

---

## Abstract of Interactive Environmental Artwork and Your Theme

**Project Title**: The Breathing Lake: 500 Years of Change

**Theme**: Climate Change Visualization Through Lake Masoko Geochemical Data

This interactive environmental artwork uses 500 years of sediment core data from Lake Masoko, Tanzania (1511-2002 AD) to visualize three interconnected climate stories: the Little Ice Age dry period (1550-1850), solar activity cycles reflected in lake levels, and recent anthropogenic impact (last 60 years). 

The project presents three distinct computational art scenes:
1. **The Sediment Core**: A data-driven visualization using Fe/Ti ratios to show erosion patterns
2. **The Changing Forest**: An L-system based representation of vegetation changes driven by Si/Ti aridity data
3. **The Solar Ripples**: A recursive visualization of magnetic susceptibility data representing solar activity

Each scene allows viewers to interact with the data through clicking, year selection, or temporal progression, making 500 years of climate history tangible and explorable.

---

## Environmental Artwork Design Sketch Image

*(From Jill Pelto lab - Include your original sketch or concept diagram here)*

[PLACEHOLDER FOR SKETCH IMAGE]

---

## Scene 1: The Sediment Core

### Image
[PLACEHOLDER FOR SCENE 1 SCREENSHOT]

### Description

**Visual Design**: The scene presents a vertical "core" of stacked rectangular layers, each representing a sediment layer from Lake Masoko. The layers are colored based on their Fe/Ti (Iron/Titanium) ratio, creating a barcode-like visualization of 491 years of lake history.

**Data Mapping**:
- **Y-Axis**: Time progression from 2002 AD (top) to 1511 AD (bottom)
- **Color**: Fe/Ti ratio intensity
  - Darker brown/red = High Fe/Ti (wet periods, increased erosion and runoff)
  - Lighter tan/gray = Low Fe/Ti (dry periods, likely Little Ice Age)
- **Each layer**: Represents approximately 7-15 years of sediment accumulation

**Interaction**: Users can click on any sediment layer to reveal:
- Exact year (AD)
- Fe/Ti ratio value
- Sediment depth in the core (cm)
- Interpretation of climate conditions

**Course Concepts Used**:
- **Complex Objects**: `SedimentLayer` class with `__init__`, accessor/mutator methods
- **Inheritance**: `SedimentLayer` inherits from `EnvironmentalFeature` parent class
- **Encapsulation**: Private attributes (`_year`, `_value`, `_depth`) with public accessor methods
- **Data Structures**: Lists to store and iterate through sediment layer objects
- **Event Handling**: Mouse click detection using `getMouse()` and `contains_point()` method
- **Color Mapping**: Mathematical normalization of data values to RGB color space
- **Modular Functions**: `create_sediment_layers()`, `draw_sediment_core()`, `create_info_display()`

**Scientific Insight**: The visualization reveals the "Little Ice Age" period (approximately 1550-1850) as lighter-colored layers, showing reduced iron content due to lower rainfall and erosion. The return to darker layers in recent centuries shows increased precipitation and human-driven landscape changes.

---

## Scene 2: The Changing Forest

### Image
[PLACEHOLDER FOR SCENE 2 SCREENSHOT]

### Description

**Visual Design**: An L-system generated tree whose complexity and branching patterns change based on historical climate data. The tree grows from the bottom of the screen upward, with branch structure determined by the Si/Ti (Silicon/Titanium) ratio of the selected year.

**Data Mapping**:
- **Si/Ti Ratio**: Proxy for aridity (dryness/wetness)
  - High Si/Ti (>16) = Wet/windy period → Lush tree (4-5 L-system iterations)
  - Medium Si/Ti (14-16) = Moderate climate → Regular tree (3 iterations)
  - Low Si/Ti (<14) = Dry period → Sparse vegetation (2 iterations)
- **L-system Iterations**: Directly controlled by normalized Si/Ti value
- **Branching Rules**: Different L-system rules for different complexity levels
- **Color**: Green leaves, brown trunk/branches

**Interaction**: Users input a year between 1511-2002 AD, and the program:
1. Finds the closest data record
2. Reads the Si/Ti value
3. Calculates appropriate L-system complexity
4. Generates and displays the corresponding forest

**Course Concepts Used**:
- **L-System Class**: String generation using replacement rules (`buildString()` method)
- **TurtleInterpreter Class**: Converts L-system strings to visual turtle graphics
- **Inheritance**: `ClimateTree` inherits from `EnvironmentalFeature`
- **User Input**: Year validation with recursive error handling
- **Command-line Arguments**: `python scene2_forest.py 1750` runs directly
- **Conditionals**: If/elif/else to determine tree complexity level
- **String Processing**: L-system rule application and string building
- **Modular Functions**: `create_tree_lsystem()`, `get_climate_description()`, `draw_forest_for_year()`

**Scientific Insight**: The scene demonstrates how the Little Ice Age (dry period) manifests as simpler vegetation patterns, while wetter periods show more complex forest structures. The Si/Ti ratio is a proxy for windiness and aridity, with higher values indicating increased weathering and transport of silica-rich materials.

---

## Scene 3: The Solar Ripples

### Image
[PLACEHOLDER FOR SCENE 3 SCREENSHOT]

### Description

**Visual Design**: A top-down view of Lake Masoko represented as concentric circular ripples. The number and intensity of ripples vary based on magnetic susceptibility data, creating a pulsing, breathing effect as users progress through time.

**Data Mapping**:
- **MagSus (Magnetic Susceptibility)**: Correlates with solar activity and lake levels
  - High MagSus = More recursion depth (6-7 levels of ripples)
  - Low MagSus = Fewer ripples (3-4 levels)
- **Ripple Color**: Blue gradient with intensity based on recursion depth
- **Recursion Depth**: Each level draws a circle 75% smaller than previous
- **Time Progression**: Click to advance through chronological data points

**Interaction**: Users click the window to progress through time from 1511 to 2002 AD, watching the lake "breathe" as solar activity changes. The info panel displays:
- Current year
- Magnetic susceptibility value
- Recursion intensity level (1-7)
- Interpretation of solar activity

**Course Concepts Used**:
- **Recursion**: `_draw_recursive_ripples()` function with proper base case and recursive case
- **Base Case**: `if depth <= 0 or radius < 5: return`
- **Recursive Case**: Calls itself with `radius * 0.75` and `depth - 1`
- **Inheritance**: `SolarRipple` inherits from `EnvironmentalFeature`
- **Data Normalization**: MagSus values normalized to 0-1 range for visualization
- **Lists**: Sorted list of `SolarRipple` objects for temporal animation
- **Color Interpolation**: RGB values calculated based on recursion depth
- **Modular Functions**: `create_ripple_objects()`, `animate_through_time()`, `update_info_panel()`

**Scientific Insight**: Magnetic susceptibility in lake sediments can reflect solar activity cycles and lake level changes. Higher magnetic susceptibility often correlates with periods of higher lake levels and increased magnetic mineral deposition, which may be influenced by solar forcing on climate.

---

## Extension Scenes (Optional)

*(None implemented in base project - potential future work)*

---

## Personal Reflection

### How does this project demonstrate how much you have learned about introductory CS concepts, good programming practices, and computational problem solving?

This final project represents the culmination of everything I've learned in CS 151. At the beginning of the semester, I could barely write a simple function. Now I've created a complete application with multiple interconnected modules, object-oriented design, and sophisticated data visualization.

**Key Learning Demonstrations**:

1. **Object-Oriented Programming**: I successfully implemented inheritance with an `EnvironmentalFeature` parent class and three child classes (`SedimentLayer`, `ClimateTree`, `SolarRipple`). Each class properly uses encapsulation with private attributes and public accessor/mutator methods. The polymorphic `draw()` method shows I understand how different objects can have the same interface but different behaviors.

2. **Problem Decomposition**: Instead of writing one massive script, I broke the problem into logical modules: data handling, class definitions, individual scenes, and a main controller. This modular approach made development, testing, and debugging much more manageable.

3. **Algorithm Implementation**: I successfully implemented three different algorithmic approaches:
   - Data normalization and color mapping for Scene 1
   - L-system string generation and interpretation for Scene 2
   - Recursive drawing with proper base and recursive cases for Scene 3

4. **User-Centered Design**: I thought carefully about user experience, creating both an interactive menu system and command-line interface. Each scene provides clear instructions and meaningful feedback.

5. **Best Practices**: Every function has a docstring, complex logic has inline comments, and I used meaningful variable names throughout. The code follows the single responsibility principle—each function does one thing well.

**Computational Problem Solving**: The project required solving multiple computational challenges:
- How to map continuous data values to discrete visual properties (colors, iterations, recursion depth)
- How to handle missing data (marked as "-" in the dataset)
- How to create intuitive interactions for exploring temporal data
- How to integrate multiple visualization libraries (Zelle graphics and turtle graphics)

This project proves I can take a complex real-world problem (understanding climate change through scientific data) and create a working computational solution that makes the data accessible and engaging.

---

### Knowing what you know now, is there anything you might have done differently in this course during the semester?

**What I Would Do Differently**:

1. **Start Projects Earlier**: I often started projects close to the deadline, which created unnecessary stress. Starting earlier would give me more time to experiment, refine, and truly understand the concepts rather than just completing requirements.

2. **Practice More Regularly**: I would do more practice problems beyond the assigned work. The concepts I struggled with most (like recursion) were the ones I didn't practice enough outside of class.

3. **Ask More Questions**: Sometimes I spent hours debugging something that could have been resolved with a quick question in office hours. I should have been less hesitant to ask for help.

4. **Read More Documentation**: I often relied on examples rather than reading the actual documentation for libraries and methods. Reading documentation more carefully would have deepened my understanding.

5. **Plan Before Coding**: For this final project, I spent time planning the class hierarchy and module structure before writing code. I wish I had done this for earlier projects too—it would have saved time and resulted in cleaner code.

6. **Test More Incrementally**: Instead of writing a large chunk of code and then testing, I learned to test each function as I write it. I should have adopted this practice earlier in the semester.

**What Went Well**:

- Taking good notes during lectures
- Working through the lab exercises carefully
- Collaborating with classmates (while maintaining academic integrity)
- Using version control (Git) to track changes
- Breaking large problems into smaller, manageable pieces

**Key Takeaway**: Programming is a skill that requires consistent practice and patience. The growth mindset I developed in this course—viewing errors as learning opportunities rather than failures—will serve me well in future CS courses and beyond.

---

## Sources of Support for This Project and the Course

### Technical Support

**Course Resources**:
- CS 151 lecture notes and example code
- Lab exercises and previous project assignments
- Zelle Graphics library documentation
- Python official documentation

**External Resources**:
- Stack Overflow for debugging specific errors
- Python documentation for standard library functions
- GeeksforGeeks for algorithm explanations

### Data Source

**Lake Masoko Geochemical Dataset**:
- Original research data from sediment core analysis
- Scientific context from environmental studies literature
- Data interpretation guidance from course materials

### Personal Support

**People Who Helped**:

1. **[Course Instructor Name]**: For excellent lectures, clear explanations, and helpful feedback on assignments throughout the semester.

2. **Teaching Assistants**: For patient help during lab sessions and office hours, especially when I was stuck on debugging issues.

3. **Study Group Members**: [Names if appropriate] - For collaborative problem-solving and mutual encouragement throughout the semester.

4. **Friends and Family**: For understanding when I needed to focus on coding and for encouraging me through challenging moments.

**Acknowledgment**: This project wouldn't have been possible without the supportive learning environment created by the entire CS 151 teaching team. Their enthusiasm for computer science is contagious, and their dedication to student success is evident in every interaction.

---

## Technical Appendix

### Files Submitted
- `main.py` - Main controller with menu system
- `masoko_data_handler.py` - Data loading and processing
- `environmental_features.py` - Parent and child classes
- `scene1_sediment.py` - Scene 1 implementation
- `scene2_forest.py` - Scene 2 implementation
- `scene3_ripples.py` - Scene 3 implementation
- `data.json` - Lake Masoko dataset
- `graphics.py` - Zelle graphics library
- `lib/lsystem.py` - L-System class
- `lib/turtle_interpreter.py` - TurtleInterpreter class
- `README.md` - Project documentation

### How to Run
```bash
cd "Final Project"
python3 main.py
```

### System Requirements
- Python 3.12+
- Tkinter (python3-tk)
- 800x800 minimum screen resolution recommended

---

*End of Report*
