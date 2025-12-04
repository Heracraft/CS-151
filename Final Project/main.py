"""
Nehemia Kaaya
CS 151
Section B
Final Project - The Breathing Lake

Main controller for interactive environmental art project
"""

import sys

def runScene1():
    """Run Scene 1: The Sediment Core"""
    import scene1_sediment
    scene1_sediment.runScene()

def runScene2(year=None):
    """Run Scene 2: The Changing Forest"""
    import scene2_forest
    if year:
        scene2_forest.runSceneWithYear(year)
    else:
        scene2_forest.runSceneInteractive()

def runScene3():
    """Run Scene 3: The Solar Ripples"""
    import scene3_ripples
    scene3_ripples.runScene()

def runHome():
    """Run graphical home page"""
    from views.home import runHomePage
    
    while True:
        scene = runHomePage()
        
        if scene == 0:
            break
        elif scene == 1:
            runScene1()
        elif scene == 2:
            runScene2()
        elif scene == 3:
            runScene3()

def main(argv):
    if len(argv) > 1:
        scene = argv[1].lower()
        
        if scene == 'scene1':
            runScene1()
        elif scene == 'scene2':
            if len(argv) > 2:
                runScene2(int(argv[2]))
            else:
                runScene2()
        elif scene == 'scene3':
            runScene3()
    else:
        runHome()

if __name__ == "__main__":
    main(sys.argv)
