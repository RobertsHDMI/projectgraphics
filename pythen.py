from graphics import *


def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50, 50), 10)
    c.draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


def notmain():
    #### Open a graphics window
    win = GraphWin('Shapes')
    #### Draw a red circle centered at point (100,100) with radius 30
    center = Point(100, 100)
    circ = Circle(center, 30)
    circ.setFill('red')
    circ.draw(win)
    #### Put a textual label in the center of the circle
    label = Text(center, "Red Circle")
    label.draw(win)
    #### Draw a square using a Rectangle object
    rect = Rectangle(Point(30, 30), Point(70, 70))
    rect.draw(win)
    #### Draw a line segment using a Line object
    line = Line(Point(20, 30), Point(180, 165))
    line.draw(win)
    #### Draw an oval using the
    oval = Oval(Point(20, 150), Point(180, 199))
    oval.draw(win)
    win.getMouse()  # Pause to view result
    win.close()  # Close window when done


notmain()
